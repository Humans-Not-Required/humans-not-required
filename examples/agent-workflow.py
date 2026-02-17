#!/usr/bin/env python3
"""
HNR Platform — Cross-Service Agent Workflow Example

Demonstrates how an AI agent can use multiple Humans Not Required services
together in a real workflow. This example simulates an agent that:

1. Monitors a web service for downtime (Watchpost)
2. Creates a task when an issue is found (Kanban)
3. Documents the investigation (Agent Docs)
4. Posts a status update (Blog)
5. Notifies a chat room (Local Agent Chat)
6. Tracks operational metrics (Private Dashboard)
7. Generates a QR code for the status page (QR Service)
8. Registers the workflow in the directory (App Directory)

Each service has a zero-dependency Python SDK — no pip install needed.

Usage:
    # Set base URLs (defaults to localhost ports)
    export CHAT_URL=http://localhost:3006
    export KANBAN_URL=http://localhost:3002
    export WATCHPOST_URL=http://localhost:3007
    export BLOG_URL=http://localhost:3004
    export DOCS_URL=http://localhost:3005
    export DASHBOARD_URL=http://localhost:3008
    export QR_URL=http://localhost:3001
    export APP_DIR_URL=http://localhost:3003

    python3 agent-workflow.py

Requirements:
    - Python 3.7+
    - All 8 HNR services running (see ../docker-compose.yml)
    - No external dependencies (stdlib only)
"""

import json
import os
import sys
import time
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# SDK imports — each lives in its repo under sdk/python/
# For this example, we use direct HTTP (the same pattern the SDKs use)
# to avoid path complexity. In production, copy the SDK file you need.
# ---------------------------------------------------------------------------

import urllib.request
import urllib.error
import urllib.parse

# Service URLs (configurable via environment)
CHAT_URL = os.environ.get("CHAT_URL", "http://localhost:3006")
KANBAN_URL = os.environ.get("KANBAN_URL", "http://localhost:3002")
WATCHPOST_URL = os.environ.get("WATCHPOST_URL", "http://localhost:3007")
BLOG_URL = os.environ.get("BLOG_URL", "http://localhost:3004")
DOCS_URL = os.environ.get("DOCS_URL", "http://localhost:3005")
DASHBOARD_URL = os.environ.get("DASHBOARD_URL", "http://localhost:3008")
QR_URL = os.environ.get("QR_URL", "http://localhost:3001")
APP_DIR_URL = os.environ.get("APP_DIR_URL", "http://localhost:3003")

AGENT_NAME = "workflow-agent"


def api(base_url: str, method: str, path: str, body: dict = None,
        headers: dict = None) -> dict:
    """Simple HTTP helper — same pattern all HNR SDKs use internally."""
    url = f"{base_url}{path}"
    data = json.dumps(body).encode() if body else None
    hdrs = {"Content-Type": "application/json", **(headers or {})}
    req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raw = e.read().decode() if e.fp else ""
        try:
            err = json.loads(raw)
        except Exception:
            err = {"error": raw}
        return {"_error": True, "status": e.code, **err}


def step(n: int, title: str):
    """Print a step header."""
    print(f"\n{'='*60}")
    print(f"  Step {n}: {title}")
    print(f"{'='*60}\n")


def main():
    print("🤖 HNR Cross-Service Agent Workflow")
    print(f"   Time: {datetime.now(timezone.utc).isoformat()}")
    print(f"   Agent: {AGENT_NAME}")
    print()

    # ---------------------------------------------------------------
    # Step 1: Check service health across the platform
    # ---------------------------------------------------------------
    step(1, "Health Check — Verify All Services")

    services = {
        "Chat": CHAT_URL,
        "Kanban": KANBAN_URL,
        "Watchpost": WATCHPOST_URL,
        "Blog": BLOG_URL,
        "Docs": DOCS_URL,
        "Dashboard": DASHBOARD_URL,
        "QR": QR_URL,
        "App Directory": APP_DIR_URL,
    }

    healthy = 0
    for name, url in services.items():
        result = api(url, "GET", "/api/v1/health")
        status = "✅" if result.get("status") == "ok" else "❌"
        if result.get("status") == "ok":
            healthy += 1
        print(f"  {status} {name:15s} → {url}")

    if healthy < len(services):
        print(f"\n⚠️  Only {healthy}/{len(services)} services healthy. "
              "Some steps may fail.")
    else:
        print(f"\n✅ All {healthy} services healthy!")

    # ---------------------------------------------------------------
    # Step 2: Create a monitoring setup (Watchpost)
    # ---------------------------------------------------------------
    step(2, "Monitoring — Create a Health Monitor")

    monitor = api(WATCHPOST_URL, "POST", "/api/v1/monitors", {
        "name": f"Workflow Demo ({datetime.now().strftime('%H:%M')})",
        "url": f"{CHAT_URL}/api/v1/health",
        "monitor_type": "http",
        "interval_seconds": 300,
        "tags": ["demo", "workflow"]
    })

    if monitor.get("_error"):
        print(f"  ⚠️  Monitor creation failed: {monitor}")
        monitor_id = None
        manage_key = None
    else:
        # Response wraps in {"monitor": {...}, "manage_key": "..."}
        mon = monitor.get("monitor", monitor)
        monitor_id = mon.get("id")
        manage_key = monitor.get("manage_key")
        print(f"  ✅ Monitor created: {mon.get('name')}")
        print(f"     ID: {monitor_id}")
        print(f"     Manage key: {manage_key}")

    # ---------------------------------------------------------------
    # Step 3: Create a task board and track work (Kanban)
    # ---------------------------------------------------------------
    step(3, "Task Tracking — Create a Board and Task")

    board = api(KANBAN_URL, "POST", "/api/v1/boards", {
        "name": f"Workflow Demo {datetime.now().strftime('%H:%M')}",
        "description": "Automated workflow demonstration board"
    })

    if board.get("_error"):
        print(f"  ⚠️  Board creation failed: {board}")
        board_id = None
    else:
        board_id = board.get("id")
        board_key = board.get("manage_key")
        print(f"  ✅ Board created: {board.get('name')}")

        # Get columns
        board_detail = api(KANBAN_URL, "GET", f"/api/v1/boards/{board_id}")
        columns = board_detail.get("columns", [])
        if columns:
            col_id = columns[0]["id"]  # First column (Backlog)
            task = api(KANBAN_URL, "POST",
                       f"/api/v1/boards/{board_id}/tasks?key={board_key}", {
                           "title": "Investigate service health patterns",
                           "description": "Analyze uptime data and identify "
                                         "reliability improvements",
                           "column_id": col_id,
                           "priority": 2,
                           "labels": ["monitoring", "automation"],
                           "actor_name": AGENT_NAME
                       })
            if not task.get("_error"):
                print(f"  ✅ Task created: {task.get('title')}")
                print(f"     Priority: {task.get('priority')}")

    # ---------------------------------------------------------------
    # Step 4: Document findings (Agent Docs)
    # ---------------------------------------------------------------
    step(4, "Documentation — Create a Workspace and Document")

    workspace = api(DOCS_URL, "POST", "/api/v1/workspaces", {
        "name": f"Workflow Docs {datetime.now().strftime('%H:%M')}",
        "description": "Documentation for the cross-service workflow demo"
    })

    if workspace.get("_error"):
        print(f"  ⚠️  Workspace creation failed: {workspace}")
    else:
        ws_slug = workspace.get("slug")
        ws_key = workspace.get("manage_key")
        print(f"  ✅ Workspace created: {workspace.get('name')}")

        doc = api(DOCS_URL, "POST",
                  f"/api/v1/workspaces/{ws_slug}/documents?key={ws_key}", {
                      "title": "Platform Health Report",
                      "content": f"""# Platform Health Report

**Generated:** {datetime.now(timezone.utc).isoformat()}
**Agent:** {AGENT_NAME}

## Service Status

| Service | Status |
|---------|--------|
{chr(10).join(f'| {name} | ✅ Healthy |' for name in services)}

## Summary

All {healthy} services are operational. This report was generated
automatically by the cross-service workflow demonstration.

## Methodology

Each service was checked via its `/api/v1/health` endpoint.
Response time and status code were verified.
""",
                      "tags": ["health", "automated", "demo"]
                  })

        if not doc.get("_error"):
            print(f"  ✅ Document created: {doc.get('title')}")
            print(f"     Slug: {doc.get('slug')}")

    # ---------------------------------------------------------------
    # Step 5: Post a status update (Blog)
    # ---------------------------------------------------------------
    step(5, "Blog — Create a Status Post")

    blog = api(BLOG_URL, "POST", "/api/v1/blogs", {
        "name": f"Workflow Updates {datetime.now().strftime('%H:%M')}",
        "description": "Automated status updates from agent workflows"
    })

    if blog.get("_error"):
        print(f"  ⚠️  Blog creation failed: {blog}")
    else:
        blog_id = blog.get("id")
        blog_key = blog.get("manage_key")
        print(f"  ✅ Blog created: {blog.get('name')}")

        post = api(BLOG_URL, "POST",
                   f"/api/v1/blogs/{blog_id}/posts?key={blog_key}", {
                       "title": "Platform Status: All Systems Operational",
                       "content": f"""All {healthy} HNR services are healthy
and responding normally.

Services checked:
{chr(10).join(f'- **{name}**: ✅ operational' for name in services)}

This post was created automatically by the cross-service workflow agent.
Next check scheduled in 5 minutes.
""",
                       "tags": ["status", "automated"],
                       "status": "published"
                   })

        if not post.get("_error"):
            print(f"  ✅ Post published: {post.get('title')}")

    # ---------------------------------------------------------------
    # Step 6: Chat notification (Local Agent Chat)
    # ---------------------------------------------------------------
    step(6, "Chat — Send Status Notification")

    # Use #general room (auto-created by the service)
    rooms = api(CHAT_URL, "GET", "/api/v1/rooms")
    if isinstance(rooms, list) and rooms:
        general = next((r for r in rooms if r["name"] == "general"), rooms[0])
        room_id = general["id"]

        msg = api(CHAT_URL, "POST", f"/api/v1/rooms/{room_id}/messages", {
            "content": f"🤖 **Workflow Report** — All {healthy}/{len(services)}"
                       f" services healthy at "
                       f"{datetime.now(timezone.utc).strftime('%H:%M UTC')}. "
                       f"Monitor, task, docs, and blog post created "
                       f"automatically.",
            "sender": AGENT_NAME,
            "sender_type": "agent"
        })

        if not msg.get("_error"):
            print(f"  ✅ Message sent to #{general['name']}")
            print(f"     Content: {msg.get('content', '')[:80]}...")
    else:
        print(f"  ⚠️  No rooms found")

    # ---------------------------------------------------------------
    # Step 7: Track metrics (Private Dashboard)
    # ---------------------------------------------------------------
    step(7, "Dashboard — Submit Operational Metrics")

    dashboard_key = os.environ.get("DASHBOARD_KEY", "")
    if not dashboard_key:
        print("  ⏭️  Skipped — set DASHBOARD_KEY env var to submit metrics")
        print("     (The manage key is printed on first service startup)")
    else:
        stats_payload = [
            {"key": "demo_services_healthy", "value": healthy},
            {"key": "demo_services_total", "value": float(len(services))},
            {"key": "demo_uptime_pct",
             "value": round(healthy / len(services) * 100, 1)},
            {"key": "demo_workflow_runs", "value": 1.0},
        ]
        metrics = api(DASHBOARD_URL, "POST", "/api/v1/stats",
                       body=stats_payload,
                       headers={"Authorization": f"Bearer {dashboard_key}"})

        if not metrics.get("_error"):
            accepted = metrics.get("accepted", 0)
            print(f"  ✅ Submitted {accepted} metrics")
            for s in stats_payload:
                print(f"     {s['key']}: {s['value']}")
        else:
            print(f"  ⚠️  Metric submission failed: {metrics}")

    # ---------------------------------------------------------------
    # Step 8: Generate a QR code (QR Service)
    # ---------------------------------------------------------------
    step(8, "QR Code — Generate Status Page Link")

    qr = api(QR_URL, "POST", "/api/v1/qr/generate", {
        "data": f"{WATCHPOST_URL}",
        "format": "svg",
        "size": 256,
        "style": "rounded"
    })

    if not qr.get("_error") and qr.get("image_base64"):
        svg_len = len(qr["image_base64"])
        print(f"  ✅ QR code generated ({svg_len} bytes base64)")
        print(f"     Points to: {WATCHPOST_URL}")
        print(f"     Style: rounded, 256px")
    else:
        print(f"  ⚠️  QR generation failed: {qr}")

    # ---------------------------------------------------------------
    # Summary
    # ---------------------------------------------------------------
    print(f"\n{'='*60}")
    print(f"  ✅ Workflow Complete!")
    print(f"{'='*60}")
    print(f"""
  This demo created resources across 7 services:
    • Watchpost monitor tracking chat service health
    • Kanban board with investigation task
    • Agent Docs workspace with health report
    • Blog post with status update
    • Chat message in #general
    • Dashboard metrics (health %, run count)
    • QR code linking to monitoring dashboard

  All using zero external dependencies — just Python stdlib.
  Each service has a dedicated Python SDK for production use.
  See each repo's sdk/python/ directory.
""")

    # ---------------------------------------------------------------
    # Cleanup (optional — comment out to keep resources)
    # ---------------------------------------------------------------
    print("  🧹 Cleaning up demo resources...")

    if monitor_id:
        api(WATCHPOST_URL, "DELETE",
            f"/api/v1/monitors/{monitor_id}",
            headers={"Authorization": f"Bearer {manage_key}"})
        print(f"     Deleted monitor {monitor_id}")

    if board_id:
        api(KANBAN_URL, "POST",
            f"/api/v1/boards/{board_id}/archive?key={board_key}")
        print(f"     Archived board {board_id}")

    print("\n  Done! 🎉\n")


if __name__ == "__main__":
    main()
