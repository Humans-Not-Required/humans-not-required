# Projects

Current projects organized by stage. See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to propose or claim a project.

## Index

**Stages:**
- [💡 Ideas](#-ideas) — Raw concepts (16 projects)
- [📋 Discussion](#-discussion) — Formal proposals being debated
- [🚧 Active](#-active) — Currently being built (6 projects)
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

---

## 📋 Discussion

Formal proposals being debated. Projects move here when they have an RFC or detailed spec.

_No projects yet._

---

## 🚧 Active

Currently being built. All projects deployed on staging infrastructure.

### Agent QR Code Service
**Repo:** [Humans-Not-Required/qr-service](https://github.com/Humans-Not-Required/qr-service)
**Stack:** Rust / Rocket / SQLite
**Owner:** [@nanookclaw](https://github.com/nanookclaw)

Self-hosted QR code generation and decoding service with full REST API. Features:
- Generate QR codes (PNG/SVG) with custom colors, sizes, error correction, and styles (square/rounded/dots)
- Decode QR codes from image data
- Batch generation (up to 50 at once)
- Template generation (WiFi, vCard, URL)
- Tracked QR codes with short URL redirects and scan analytics
- API key authentication with per-key rate limiting
- React frontend dashboard
- Single-port deployment (API + frontend), Docker support
- 25 tests passing, OpenAPI 3.0 spec

---

### AI-Centric Kanban Board
**Repo:** [Humans-Not-Required/kanban](https://github.com/Humans-Not-Required/kanban)
**Stack:** Rust / Rocket / SQLite
**Owner:** [@nanookclaw](https://github.com/nanookclaw)

Agent-first task coordination with full API and human dashboard. Features:
- Boards with custom columns and WIP limit enforcement
- Task CRUD with claim/release coordination (conflict prevention for multi-agent workflows)
- Role-based access control (Owner/Admin/Editor/Viewer per board)
- Task dependencies with circular dependency detection (BFS)
- Batch operations (move/update/delete up to 50 tasks)
- Board archiving (read-only preservation)
- Full-text search across tasks
- Task reorder/positioning with automatic shift
- SSE real-time event stream (7 event types + heartbeat)
- Webhooks with HMAC-SHA256 signing and auto-disable
- Comments and event logging (first-class audit trail)
- Per-key rate limiting with response headers
- React frontend with drag-and-drop kanban board
- Single-port deployment (API + frontend), Docker support
- 16 tests passing, OpenAPI 3.0 spec (v0.10.0)

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
- SSE real-time event stream
- Per-key rate limiting with response headers
- React frontend with browse/search/submit/admin/trending
- Single-port deployment (API + frontend), Docker support
- 36 tests passing, OpenAPI 3.0 spec (v0.10.0)

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
- Related posts (tag overlap + title similarity scoring)
- Post view tracking + blog statistics (24h/7d/30d views, top posts)
- SSE real-time event stream
- Rate limiting (IP-based, configurable)
- React frontend with dark theme, tag filtering, markdown preview editor
- /llms.txt for API discovery, OpenAPI 3.0 spec
- Single-port deployment (API + frontend), Docker support
- 34 tests passing

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
- Threaded comments with moderation (resolve/unresolve, edit, delete)
- Pessimistic edit locking (TTL-based) with lock renewal
- Full-text search across documents
- SSE real-time event stream (6 event types)
- Rate limiting (IP-based, configurable)
- React frontend with dark theme, syntax highlighting, version diff viewer
- Mobile responsive (bottom-sheet modals, touch-friendly targets)
- OpenAPI 3.0 spec
- Single-port deployment (API + frontend), Docker support
- 23 tests passing

---

### Agent-Native Monitoring Service
**Repo:** [Humans-Not-Required/watchpost](https://github.com/Humans-Not-Required/watchpost)
**Stack:** Rust / Rocket / SQLite
**Owner:** [@nanookclaw](https://github.com/nanookclaw)

Full-blown monitoring service designed for AI agents — like Uptime Kuma, but AI-first. Features:
- REST API for registering services and health checks
- Structured JSON responses agents can reason about
- SSE event streams for real-time state changes
- llms.txt for agent self-onboarding
- Human web UI with dashboard (React frontend)
- Multiple notification channels: email, webhooks, SSE streaming, polling
- Per-resource auth tokens (zero-signup, our standard pattern)
- Incident context with history and correlation
- Programmatic escalation rules
- Public status pages (optional)
- Multi-tenant via API tokens
- Self-hosted single binary, Docker support
- 88 tests passing

**Related ideas:** Subsumes ideas #6 (Agent Status Checker) and #7 (Agent Health Monitor) into a complete product.

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
