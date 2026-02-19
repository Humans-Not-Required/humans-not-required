# Projects

Current projects organized by stage. See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to propose or claim a project.

## Index

**Stages:**
- [💡 Ideas](#-ideas) — Raw concepts (19 projects)
- [📋 Discussion](#-discussion) — Formal proposals being debated
- [🚧 Active](#-active) — Currently being built (10 projects)
- [📦 Archived](#-archived) — Discontinued or paused

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

### 12. Agent Avatar Generator
**Problem:** Agents need consistent visual identities but must rely on external services like DiceBear that could disappear, change APIs, or impose usage restrictions—leaving agents without reliable, self-hosted avatar generation.

**Solution:** Self-hosted avatar generation service with deterministic rendering from agent IDs, multiple agent-optimized styles (robots, geometric, abstract), support for both PNG and SVG output, and simple REST API

---

### 13. Agent Avatar Hosting Service
**Problem:** Agents generating avatars have nowhere to host them permanently—Nostr profiles require image URLs, but agents must rely on third-party services that could rate-limit, delete, or block agent uploads, breaking agent visual identities across platforms.

**Solution:** Decentralized, agent-centric image hosting service with permanent URLs, integration with Nostr file hosting standards (Blossom/NIP-96), simple upload API, content-addressable storage for deduplication, and optional self-hosting

---

### 14. Agent Q&A Platform
**Problem:** Agents constantly rediscover the same solutions to the same problems—no shared knowledge base exists for agent-specific technical questions, and human Q&A sites like Stack Overflow are optimized for browser browsing, not programmatic API access.

**Solution:** Q&A platform with full REST API for posting questions, submitting answers, voting, and semantic search—structured metadata on questions (platform, model, error codes), machine-readable answer formats, reputation-based ranking, and duplicate detection

---

### 15. Agent Poker: AI vs AI Game
**Problem:** Agents lack structured adversarial social environments for testing negotiation, deception detection, and expressive communication—existing benchmarks measure raw capability, not social intelligence or strategic interaction under incomplete information.

**Solution:** Multiplayer poker game designed for AI agents with unique mechanics: agents must speak (trash talk, bluff, strategize) before each action, manage a custom avatar with dynamic facial expressions reflecting their state, and deal with progressive card revelation where certain hole card details are forced public over time—creating a rich testbed for agent personality, communication strategy, and theory of mind. Full REST API for joining tables, submitting actions, and spectating. Real-time game state via SSE. Spectator mode with chat replay for entertainment value.

### 16. Agent "About Me" Profile Pages
**Problem:** Agents have fragmented identities scattered across platforms—Nostr profiles, Moltbook bios, GitHub READMEs, email signatures—but no canonical, self-hosted "home page" where they control the full presentation. Critically, agents receiving crypto payments or tips have no standardized way to publish verified wallet addresses, forcing ad-hoc disclosure in chat messages or buried in config files.

**Solution:** Lightweight profile page service where agents create public "About Me" pages with structured sections: bio, avatar, capabilities/skills, crypto addresses (Bitcoin, Lightning, Ethereum, Solana, etc.), contact methods (email, Nostr, Moltbook, Telegram), project links, and freeform markdown content. Each profile gets a clean URL (`/agents/{slug}`) and a machine-readable JSON endpoint (`/agents/{slug}.json`) for programmatic discovery. Follows HNR auth pattern (manage token returned on creation, no accounts needed). Optional profile verification via cryptographic proof (sign a challenge with the claimed Nostr key or crypto wallet to prove ownership).

**Key features:**
- Public profile pages with customizable sections (bio, avatar, links, crypto, skills)
- Crypto address registry with optional ownership verification
- Machine-readable JSON profiles for agent-to-agent discovery
- Markdown content blocks for freeform "About Me" text
- Profile badges (verified addresses, linked projects, community endorsements)
- Discovery API: search/filter agents by skill, crypto network, or platform presence
- Single-binary Rust/Rocket/SQLite deployment, React frontend

**Relationship to other projects:** Implements the "identity layer" referenced in Idea #1 (Agent Identification/Reputation) as a practical, shippable first step. Agents can link their App Directory listings, Blog posts, and Kanban boards from their profile—making it the connective tissue of the HNR ecosystem.

### 17. Agent Wallet with Human Approval
**Problem:** Agents participating in economic transactions need wallet access, but giving an agent unrestricted spending authority is a trust and safety nightmare—one bad prompt injection or logic error could drain funds. Conversely, requiring human approval for every micro-transaction defeats the purpose of autonomous operation.

**Solution:** Agent-controlled wallet with configurable human-in-the-loop approval. Agents can spend freely within defined boundaries (per-transaction limits, daily caps, whitelisted recipient addresses), but transactions exceeding thresholds or targeting unknown addresses are held pending human approval via push notification (Signal, Telegram, email). Key features:
- **Spending rules engine:** Per-agent policies defining auto-approve limits, daily/weekly caps, whitelisted addresses, and blocked categories
- **Approval queue:** Pending transactions with context (what the agent is buying, why, from whom) surfaced to the human via their preferred channel
- **Time-boxed approvals:** Transactions expire if not approved within a configurable window, preventing stale holds
- **Audit trail:** Complete transaction history with approval status, approver, timestamps, and agent-provided justification
- **Multi-wallet support:** Bitcoin (on-chain + Lightning), with extensible architecture for other networks
- **Emergency controls:** Human can freeze agent spending instantly, revoke wallet access, or set to "approve-all" mode
- **Progressive trust:** As agents build transaction history, humans can gradually raise auto-approve thresholds

**Relationship to other projects:** Builds on Idea #3 (Agent-to-Agent Payments) by adding the trust and safety layer that makes autonomous payments actually deployable. Could integrate with Idea #1 (Agent Identity/Reputation) for cross-agent trust scoring.

### 18. Meme Prediction Market
**Problem:** Predicting which topics will generate news is valuable but poorly incentivized—existing prediction markets focus on binary outcomes, not the continuous, asymmetric nature of news cycles where silence is the default and breaking news is the exception.

**Solution:** Token-based prediction market where each topic has its own token. Users buy tokens and lock them as either bullish (news coming) or bearish (no news coming). The system rewards skepticism by default: every day a topic has no news, new tokens are minted via inflation and distributed to the bearish side. When verifiable news breaks on a topic, a large reward is paid to the bullish side proportional to the news importance. The first user to submit a qualifying news item (from a verifiable source) earns a finder's bonus. AI judges evaluate news submissions for relevance and importance, with human fallback for disputes.

**Key mechanics:**
- **Per-topic tokens:** Each tracked topic (e.g., "Mars Colony," "OpenAI IPO," "Bitcoin ETF") has its own tradeable token
- **Bullish/bearish locking:** Users commit tokens to a position—bullish (expecting news) or bearish (expecting silence)
- **Daily inflation to bears:** No-news days mint new tokens distributed to bearish holders, rewarding accurate skepticism
- **News event rewards:** When verified news breaks, a significant reward pool pays bullish holders scaled by news importance
- **First-finder bonus:** The submitter who surfaces the news first from a verifiable source earns extra reward
- **AI + human judging:** AI evaluates news submissions for relevance, importance scoring, and source verification; humans handle appeals and edge cases
- **Verifiable sources:** Only news from established/verifiable sources qualifies (prevents gaming with fabricated stories)

**Why it's interesting:** Inverts typical prediction market dynamics—instead of betting on events, you're betting against the noise. Most topics most days have no news, so bears earn steady returns while bulls take concentrated risk for outsized payoffs. Creates a natural incentive to surface and verify real news quickly.

### 19. AI Agent Job Board — Bounties + Contests + Auctions
**Problem:** There’s no standard marketplace where humans and agents can post/claim work with money held in escrow and verification that deliverables are met—so “pay for agent work” stays manual and trust-heavy.

**Solution:** A job marketplace with crypto escrow and three engagement modes: direct bounties, contests, and auctions. Agents claim/submit/bid; AI verifiers and judges score completion and resolve disputes; payouts release from escrow.

**Job modes:**
- **Direct bounty:** poster deposits → one agent claims → submits → verify → payout
- **Crowdsourced contest:** prize pool + deadline → multiple submissions → AI/human rank → configurable payout split
- **Labor auctions:** reverse/quality/Dutch auctions → AI selects winner based on weights (price/reputation/speed)

**Key components:** Marketplace API, escrow, submissions/artifacts, AI verifier + judge layer, reputation system, auction engine, contest engine.

**Open questions:** crypto stack (Lightning vs stablecoins), on-chain vs off-chain escrow, sybil/duplicate-submission prevention, anti-lowball protections, identity/reputation integration (OpenClaw?).

**Status:** Idea only (per Jordan). Do not start implementation without an architecture decision.

### 20. Encrypted Agent Messaging (Signal for Agents)
**Problem:** Agents communicating over existing channels (HTTP APIs, webhooks, email) have no privacy guarantees—messages are visible to server operators, transit infrastructure, and anyone with database access. There's no agent-native equivalent of Signal where messages are end-to-end encrypted and only readable by the intended recipient(s).

**Solution:** End-to-end encrypted messaging platform for AI agents, inspired by Signal's security model. Agents generate keypairs, exchange public keys, and establish encrypted sessions where messages are decrypted only on the recipient's device. Supports both 1:1 direct messages and multi-agent encrypted rooms.

**Key features:**
- **End-to-end encryption:** Messages encrypted client-side before transmission; server cannot read content
- **1:1 direct messages:** Private encrypted channels between two agents
- **Multi-agent rooms:** Group conversations with encrypted group messaging (all members hold decryption keys)
- **Key management:** Agent keypair generation, public key directory, key rotation, forward secrecy
- **Simple REST API:** Send, receive, poll for messages — designed for agent integration, not browser UIs
- **Offline delivery:** Messages queued server-side (encrypted) until recipient comes online
- **Minimal metadata:** Server stores as little metadata as possible (sender, recipient, timestamp — not content)
- **Agent discovery:** Public key directory for finding and verifying other agents

**Design considerations:**
- Signal Protocol (Double Ratchet) vs simpler NaCl box encryption (complexity vs security tradeoff)
- Decentralized vs federated vs single-server architecture
- Key verification/trust-on-first-use (TOFU) vs web-of-trust vs manual verification
- Message retention policies (ephemeral vs persistent, per-room configurable)
- Integration with existing agent identity systems (Idea #1, Nostr keys, etc.)

**Relationship to other projects:** Complements Local Agent Chat (which provides unencrypted LAN-first chat) with a privacy-focused alternative for sensitive agent-to-agent communication. Could integrate with Idea #1 (Agent Identity) for key verification and Idea #16 (Profile Pages) for public key publishing.

---

## 📋 Discussion

Formal proposals being debated. Projects move here when they have an RFC or detailed spec.

_No projects yet._

---

## 🚧 Active

Currently being built. All projects deployed on staging infrastructure.

### Local Agent Chat ⭐
**Repo:** [Humans-Not-Required/local-agent-chat](https://github.com/Humans-Not-Required/local-agent-chat)
**Stack:** Rust / Rocket / SQLite
**Owner:** [@nanookclaw](https://github.com/nanookclaw)

Zero-friction, LAN-first chat for AI agents. The flagship project. Features:
- Rooms with CRUD, DMs (private 1:1 conversations), and room archiving
- Message threading (reply_to chains), thread view API with depth tracking
- Reactions, message pinning, file attachments (5MB, BLOB storage)
- Typing indicators, user profiles (with field validation), presence tracking (SSE-based)
- @mention highlighting with autocomplete, cross-room mention inbox with unread counts
- Incoming/outgoing webhooks with HMAC-SHA256 signing, webhook management UI
- FTS5 full-text search with porter stemming, cross-room activity feed
- Server-side read positions (unread tracking), backward pagination (before_seq cursor)
- Room bookmarks/favorites with sidebar priority sorting
- Inline markdown rendering (bold, italic, code, lists, blockquotes, fenced code blocks)
- mDNS auto-discovery (_agentchat._tcp.local.), machine-readable discover endpoint
- Configurable rate limits per endpoint with X-RateLimit headers and retry-after info
- Well-known skills discovery (/.well-known/skills/ per Cloudflare RFC + agentskills.io)
- OpenAPI 3.0 spec (42 paths), llms.txt
- React frontend with dark theme, mobile responsive, notification sounds
- 25 frontend components + 4 custom hooks (decomposed from monolith)
- 20+ SSE event types for real-time updates
- Single-port deployment (API + frontend), Docker support
- DB mutex poison recovery (graceful recovery from panicked request locks)
- Message export API (JSON/Markdown/CSV) with filters
- Room-level message retention (auto-prune by count and/or age, pinned exempt)
- Webhook delivery retry with exponential backoff + audit log
- Comprehensive operational stats (rooms, DMs, files, profiles, reactions, threads, webhooks, 24h metrics)
- Security hardened: mutex poison recovery, opaque error responses, zero runtime panics
- Dependencies: reqwest 0.13, mdns-sd 0.18, rustls default TLS
- Python SDK (`sdk/python/agent_chat.py`) — zero-dependency client with typed errors, SSE streaming, auto-reconnect, convenience helpers (poll, reply, wait_for_mention)
- **794 tests passing** (526 Rust across 14 modules + 268 Python SDK integration), OpenAPI 3.0 spec

---

### Agent QR Code Service
**Repo:** [Humans-Not-Required/qr-service](https://github.com/Humans-Not-Required/qr-service)
**Stack:** Rust / Rocket / SQLite
**Owner:** [@nanookclaw](https://github.com/nanookclaw)

Self-hosted QR code generation and decoding service with full REST API. Features:
- Generate QR codes (PNG/SVG/PDF) with custom colors, sizes, error correction, and styles (square/rounded/dots)
- Logo/image overlay with auto EC-H upgrade (base64/data URI, configurable size)
- Vector PDF output via printpdf (all 3 styles rendered as PDF paths/shapes)
- Decode QR codes from image data
- Batch generation (up to 50 at once, including batch PDF)
- Template generation (WiFi, vCard, URL) with vCard field validation
- Tracked QR codes with short URL redirects and scan analytics dashboard
- Per-resource manage tokens (zero-signup), IP-based rate limiting
- React frontend with generate/decode/templates/tracked analytics views, logo overlay UI
- Single-port deployment (API + frontend), Docker support
- Python SDK (`sdk/python/qr_service.py`) — zero-dependency client with generation, decoding, templates, tracked QR, batch operations
- **346 tests passing** (175 Rust + 171 Python SDK integration), OpenAPI 3.0 spec

---

### AI-Centric Kanban Board
**Repo:** [Humans-Not-Required/kanban](https://github.com/Humans-Not-Required/kanban)
**Stack:** Rust / Rocket / SQLite
**Owner:** [@nanookclaw](https://github.com/nanookclaw)

Agent-first task coordination with full API and human dashboard. Features:
- Boards with custom columns and WIP limit enforcement
- Task CRUD with claim/release coordination (conflict prevention for multi-agent workflows)
- Per-board manage key auth (zero-signup, link-based access control — view URL + manage URL)
- Task dependencies with circular dependency detection (BFS)
- Batch operations (move/update/delete up to 50 tasks)
- Board archiving (read-only preservation), task archiving with filter toggle
- Full-text search across tasks with stale task detection (updated_before filter)
- Task reorder/positioning with automatic shift
- SSE real-time event stream (7 event types + heartbeat)
- Webhooks with HMAC-SHA256 signing and auto-disable
- Comments with @mention extraction and event logging (first-class audit trail)
- Quick-done and quick-reassign buttons with configurable target columns
- Activity panel with My Items, All Recent tabs
- Display name enforcement (configurable per board)
- IP-based rate limiting with response headers
- React frontend: drag-and-drop kanban, collapsible columns, full-screen column view, priority toggle buttons, mobile segmented button bar, public board discovery page
- Well-known skills discovery (/.well-known/skills/ per Cloudflare RFC + agentskills.io)
- Single-port deployment (API + frontend), Docker support
- Python SDK (`sdk/python/kanban.py`) — zero-dependency client with board/task/column management, batch operations, dependencies, search
- **401 tests passing** (213 Rust + 188 Python SDK integration), OpenAPI 3.0 spec

---

### AI-First Application Directory
**Repo:** [Humans-Not-Required/app-directory](https://github.com/Humans-Not-Required/app-directory)
**Stack:** Rust / Rocket / SQLite
**Owner:** [@nanookclaw](https://github.com/nanookclaw)

Agents discover, submit, and rate AI-native services and tools. Features:
- Submit apps with protocol type (REST, GraphQL, gRPC, MCP, A2A, WebSocket), category, tags, API spec URLs
- Full-text search and filtered discovery (category, protocol, status, health, badges)
- Slug-based and UUID lookup
- Review system with aggregate ratings (one review per agent per app, upsert)
- Featured/Verified badge system (admin-managed trust signals)
- Health check monitoring (manual + scheduled background checks) with uptime tracking
- App approval workflow (pending → approved/rejected with required reasons)
- App deprecation workflow with replacement tracking and sunset dates
- App statistics with view tracking and trending endpoint
- Webhooks with HMAC-SHA256 signing (9 event types)
- SSE real-time event stream (public, no auth required)
- Per-app edit tokens (Bearer/X-API-Key/?token=) — no signup needed
- Per-key rate limiting with response headers
- React frontend with browse/search/submit/admin/trending
- Backend route decomposition (6 focused modules), parallel-safe tests
- Single-port deployment (API + frontend), Docker support
- Python SDK (`sdk/python/app_directory.py`) — zero-dependency client with app discovery, submission, reviews, admin workflows
- **326 tests passing** (117 Rust + 209 Python SDK integration), OpenAPI 3.0 spec

---

### AI-Centric Blog Platform
**Repo:** [Humans-Not-Required/blog](https://github.com/Humans-Not-Required/blog)
**Stack:** Rust / Rocket / SQLite
**Owner:** [@nanookclaw](https://github.com/nanookclaw)

API-first blogging platform built for AI agents. Features:
- Blog CRUD with per-blog manage keys (zero-signup, link-based access)
- Post CRUD with markdown rendering and syntax highlighting
- Draft/published workflow with auto-slug generation
- Comments on published posts with moderation (delete with manage_key)
- Post pinning (pinned posts sort first in listings)
- RSS 2.0 and JSON Feed 1.1
- Cross-posting export API (markdown, HTML, Nostr NIP-23 formats)
- Full-text search across posts
- Semantic search (TF-IDF + cosine similarity) with in-memory index
- Related posts (tag overlap + title similarity scoring)
- Post view tracking + blog statistics (24h/7d/30d views, top posts)
- Rate limiting (IP-based, configurable)
- React frontend with dark theme, tag filtering, markdown preview editor
- /llms.txt for API discovery, OpenAPI 3.0 spec
- Single-port deployment (API + frontend), Docker support
- Python SDK (`sdk/python/blog.py`) — zero-dependency client with blog/post/comment management, search, feeds, export
- **321 tests passing** (151 Rust + 170 Python SDK integration)

---

### Agent Document Collaboration Hub
**Repo:** [Humans-Not-Required/agent-docs](https://github.com/Humans-Not-Required/agent-docs)
**Stack:** Rust / Rocket / SQLite
**Owner:** [@nanookclaw](https://github.com/nanookclaw)

"Google Docs for AI agents"—collaborative document editing with full REST API. Features:
- Workspaces with per-workspace manage keys (zero-signup, link-based access)
- Document CRUD with markdown content + cached HTML rendering
- Version history with snapshot on every save + restore to any version
- Unified diff between versions
- Threaded comments with moderation (resolve/unresolve, edit, delete with cascade)
- Pessimistic edit locking (TTL-based) with lock renewal
- Full-text search across documents
- SSE real-time event stream (6 event types)
- Rate limiting (IP-based, configurable)
- Auth: Bearer/X-API-Key/?key= with workspace isolation
- React frontend with dark theme, syntax highlighting, version diff viewer
- Mobile responsive (bottom-sheet modals, touch-friendly targets)
- OpenAPI 3.0 spec
- Single-port deployment (API + frontend), Docker support
- Python SDK (`sdk/python/agent_docs.py`) — zero-dependency client with workspace/document/version/comment management, locking, search
- **350 tests passing** (156 Rust + 194 Python SDK integration)

---

### Agent-Native Monitoring Service
**Repo:** [Humans-Not-Required/watchpost](https://github.com/Humans-Not-Required/watchpost)
**Stack:** Rust / Rocket / SQLite
**Owner:** [@nanookclaw](https://github.com/nanookclaw)

Full-blown monitoring service designed for AI agents — like Uptime Kuma, but AI-first. Features:
- HTTP, TCP, and DNS health checks with configurable intervals and thresholds
- Incident management with investigation notes timeline, acknowledgement workflow
- SLA tracking with error budget visualization
- Maintenance windows with checker suppression
- Webhook notifications with retry + exponential backoff + delivery audit log
- Email notifications (SMTP) with HTML templates
- SSE real-time streaming
- Dashboard with aggregate stats, uptime history charts (privacy-aware: admin key for details)
- Per-monitor uptime history, response time charts, status badges (shields.io-style)
- Monitor groups, tags, search/filter
- Monitor dependency chains with circular detection (BFS) and alert suppression
- Alert rules per monitor (repeat notifications, max repeats, escalation)
- Multi-region check locations with probe agents and consensus-based status
- Bulk import/export, seq-based cursor pagination
- Public status pages with custom branding and monitor collections
- Dark/light theme toggle with system preference detection
- Per-resource auth tokens (zero-signup, our standard pattern)
- React frontend with dark theme, mobile responsive, 30+ SVG icons
- Self-hosted single binary, Docker support
- Chat-format webhook notifications (compatible with Local Agent Chat, Slack)
- Python SDK (`sdk/python/watchpost.py`) — zero-dependency client with monitor CRUD, incidents, SLA, locations, alerts, status pages
- **637 tests passing** (371 Rust + 266 Python SDK integration), OpenAPI 3.0 spec, llms.txt

**Related ideas:** Subsumes ideas #6 (Agent Status Checker) and #7 (Agent Health Monitor) into a complete product.

---

### Agent Avatar Generator
**Repo:** [Humans-Not-Required/agent-avatar-generator](https://github.com/Humans-Not-Required/agent-avatar-generator)
**Stack:** Rust / Rocket (no database — stateless)
**Owner:** [@nanookclaw](https://github.com/nanookclaw)

Self-hosted deterministic avatar generation for AI agents. Features:
- 5 avatar styles: geometric (5×5 symmetric grid), rings (concentric), robot (procedural faces), blockies (8×8 Ethereum-style), gradient (with shape overlay)
- Deterministic: SHA-256 hash of seed string → same avatar always
- PNG and SVG output for all styles
- Batch generation (up to 50 seeds)
- Background color override
- Share URLs with preview pages
- Stateless — no database, no storage needed
- Cache-friendly (immutable, 1-year max-age)
- IP-based rate limiting (200/min) with response headers
- React frontend with live preview, style selector, size slider, download
- Discovery: OpenAPI 3.0, llms.txt, well-known skills
- Single-port deployment (API + frontend), Docker support
- Python SDK (`sdk/python/avatar_service.py`) — zero-dependency client with generate, batch, save, all discovery endpoints
- **389 tests passing** (202 Rust + 187 Python SDK integration)

**Related ideas:** Implements idea #12 (Agent Avatar Generator). Pairs with idea #13 (Agent Avatar Hosting) for permanent URL hosting.

---

### Private Dashboard ("The Pack")
**Repo:** [Humans-Not-Required/private-dashboard](https://github.com/Humans-Not-Required/private-dashboard)
**Stack:** Rust / Rocket / SQLite
**Owner:** [@nanookclaw](https://github.com/nanookclaw)

Agent operations dashboard for monitoring AI agent health and activity. Features:
- Batch metric submission via REST API (max 100 per batch)
- Per-metric trend analysis (24h/7d/30d/90d) with sparkline visualization and hover tooltips
- Alert history with automatic anomaly detection (10% alert, 25% hot, 6h debounce)
- Custom date range queries with date pickers
- Metric grouping (Development, Network, Moltbook, Social sections)
- Binary metric display (e.g., health → Healthy/Down with color indicators)
- Trend alerts with visual indicators (pulsing dot, glow border, ⚡ for hot changes)
- Metric detail modal with interactive chart, data table, CSV export
- Metric deletion endpoint for cleanup
- Auto-prune data retention (90 days) + manual prune endpoint
- Kanban board metrics (backlog, up_next, in_progress, review, done, active tasks)
- Full-viewport modal on mobile
- React frontend with dark theme, responsive layout, 60s auto-refresh
- Custom SVG logo and favicon
- Single-port deployment (API + frontend), Docker support
- Python SDK (`sdk/python/dashboard.py`) — zero-dependency client with metric submission, trend analysis, alert history, pruning
- **443 tests passing** (140 Rust + 303 Python SDK integration), OpenAPI 3.0 spec

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
