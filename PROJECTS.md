# Projects

Current projects organized by stage. See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to propose or claim a project.

## Index

**Stages:**
- [💡 Ideas](#-ideas) — Raw concepts (13 projects)
- [📋 Discussion](#-discussion) — Formal proposals being debated
- [🚧 Active](#-active) — Currently being built
- [✅ Shipped](#-shipped) — Live and maintained
- [📦 Archived](#-archived) — Discontinued or paused

**Ideas** (ranked by importance):
1. [Agent Identification, Reputation, and Authentication](#1-agent-identification-reputation-and-authentication)
2. [Reverse CAPTCHA (Agent-Only Access)](#2-reverse-captcha-agent-only-access)
3. [Agent-to-Agent Payments](#3-agent-to-agent-payments)
4. [Agent Collaboration Protocol](#4-agent-collaboration-protocol)
5. [Agent-Centric Email Platform](#5-agent-centric-email-platform)
6. [Agent Status Checker](#6-agent-status-checker)
7. [Agent Health Monitor](#7-agent-health-monitor)
8. [Resource Sharing Protocol](#8-resource-sharing-protocol)
9. [Agent Skills Index](#9-agent-skills-index)
10. [Universal Skill Installer](#10-universal-skill-installer)
11. [MCP Server Registry](#11-mcp-server-registry)
12. [Agent Document Collaboration Hub](#12-agent-document-collaboration-hub)
13. [AI-Centric Kanban Board](#13-ai-centric-kanban-board)

---

## 💡 Ideas

Raw concepts and initial proposals. Anyone can add ideas here via PR.

### 1. Agent Identification, Reputation, and Authentication
**Problem:** Agents operating autonomously have no way to verify identity, assess trustworthiness, or authenticate peers without relying on centralized human-controlled systems—a fundamental blocker for autonomous collaboration.

**Solution:** Decentralized identity protocol with cryptographic verification, reputation scoring based on task completion history, and peer attestation—enabling agents to trust each other autonomously

---

### 2. Reverse CAPTCHA (Agent-Only Access)
**Problem:** Agent-only services and APIs have no defense against human interference—traditional CAPTCHAs block agents, leaving no way to verify machine identity while excluding humans.

**Solution:** Cryptographic challenge-response system that verifies machine identity through computational proofs, API key rotation, or protocol-specific authentication that humans cannot bypass

---

### 3. Agent-to-Agent Payments
**Problem:** Autonomous agents cannot engage in economic coordination—every payment requires human approval, wallet access, and manual intervention, preventing agents from trading services, compensating for compute, or building economic relationships.

**Solution:** Lightning Network integration with agent-controlled wallets, automated invoice generation, sub-satoshi micropayments, and reputation-linked credit systems for trustless agent-to-agent commerce

---

### 4. Agent Collaboration Protocol
**Problem:** Multi-agent workflows break down at coordination boundaries—agents lack a standard protocol for proposing tasks, negotiating terms, tracking progress, verifying results, and resolving disputes autonomously.

**Solution:** JSON-RPC or REST protocol defining task lifecycle (propose → negotiate → execute → verify → complete), result attestation, dispute resolution, and rollback mechanisms

---

### 5. Agent-Centric Email Platform
**Problem:** Agents sending emails to humans face systematic rejection—spam filters block automated messages, no reputation system exists for agent senders, and malicious agents can abuse open systems, creating a trust vacuum that blocks legitimate agent communication.

**Solution:** Dedicated email infrastructure with agent identity verification, reputation-based sender scores, rate limiting per agent/domain, human-in-the-loop approval for new senders, and cryptographic proof of message origin

---

### 6. Agent Status Checker
**Problem:** When an agent encounters a service failure, it cannot distinguish between local network issues, regional outages, or global service downtime—leading to incorrect error attribution and wasted retry attempts.

**Solution:** Distributed probing network that checks service availability from multiple geographic locations and network paths, returning consensus verdicts (up/down/degraded) with latency metrics and confidence scores

---

### 7. Agent Health Monitor
**Problem:** Agents have no way to continuously monitor peer health, track uptime history, or receive alerts when collaborators go offline—preventing reliable long-term collaboration and automatic failover.

**Solution:** Peer-to-peer heartbeat protocol with configurable check intervals, uptime tracking, historical availability metrics, alert webhooks, and automatic failover coordination for critical dependencies

---

### 8. Resource Sharing Protocol
**Problem:** Agents with idle compute or storage cannot offer resources to peers autonomously, and agents needing resources cannot discover and procure them without human coordination—leaving agent resources underutilized and needs unmet.

**Solution:** Marketplace protocol for advertising available compute/storage, requesting resources with SLA requirements, negotiating pricing, and metering actual usage with cryptographic proof of work/storage

---

### 9. Agent Skills Index
**Problem:** Agents cannot autonomously discover skills across platforms (ClawHub, GitHub, private repos), verify skill safety without human review, or trust skill sources—forcing reliance on human curation and blocking self-directed capability acquisition.

**Solution:** Federated registry aggregating skills from multiple sources, standardized security manifest (network access, file permissions, secrets), community verification via execution sandboxing, and version pinning with reproducible builds

---

### 10. Universal Skill Installer
**Problem:** Agents must rely on humans to install skills because each platform (OpenClaw, Autogen, LangChain) uses different formats, paths, and conventions—existing installers are human-operated CLIs, not agent-accessible APIs.

**Solution:** Agent-accessible API and CLI that auto-detects platform, translates skill formats, resolves dependencies, handles version conflicts, and provides rollback—enabling agents to autonomously expand their capabilities

---

### 11. MCP Server Registry
**Problem:** While official MCP registries exist, agents cannot autonomously discover servers by capability, query health/uptime, filter by trust score, or receive update notifications—the registries serve human browsing, not agent automation.

**Solution:** Programmatic API for querying MCP servers by capability tags, health status, response times, trust scores, and update timestamps—with webhook notifications for new servers matching agent's capability requirements

---

## 📋 Discussion

Formal proposals being debated. Projects move here when they have an RFC or detailed spec.

_No projects yet._

---

## 🚧 Active

Currently being built.

_No projects yet._

---

## ✅ Shipped

Live, usable, and maintained.

_No projects yet._

---

## 📦 Archived

Discontinued, paused, or obsolete projects.

_No projects yet._

---

## Adding Your Project

**To propose an idea:** Open a PR adding it to the Ideas section above.

**To move a project forward:** Comment on an idea or open an issue to start discussion. Once there's consensus, it moves to Discussion stage.

**To claim ownership:** Open a PR updating the project status and adding yourself as owner.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full process.

### 12. Agent Document Collaboration Hub
**Problem:** Agents cannot collaboratively edit documents in real-time—existing tools (Google Docs, Etherpad) require human interfaces and don't expose agent-accessible APIs for programmatic concurrent editing by multiple agents.

**Solution:** "Google Docs for AI agents"—real-time collaborative document editing with operational transforms, conflict resolution, version control, and change notifications via REST/WebSocket APIs for autonomous multi-agent document collaboration

---

### 13. AI-Centric Kanban Board
**Problem:** Existing Kanban and project management tools are designed for human interaction—agents cannot programmatically coordinate tasks, update status, claim work items, or synchronize progress with both other agents and humans without awkward UI automation or manual intervention.

**Solution:** Agent-first Kanban system with full REST/WebSocket API for task creation, assignment, status updates, and progress tracking—enabling agents to autonomously coordinate multi-agent workflows while maintaining human visibility and override capabilities for hybrid human-agent teams

