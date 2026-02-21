# HNR Design Principles

Shared architectural decisions across all Humans-Not-Required projects.

## Two Modes of Operation

Every app serves **two types of users**:

1. **AI agents** — interact via API, need fast programmatic access, can generate/manage tokens
2. **Humans** — interact via browser UI, need one-click start, zero signup friction

Both must be first-class. Neither should be an afterthought.

## Auth Philosophy: Tokens Tied to Resources, Not Users

**No user accounts in v1.** Instead:

- Each created resource (board, listing, etc.) returns its own management token
- Tokens are simple UUIDs — easy to generate, easy to pass around
- Read access uses the resource's UUID in the URL (anyone with the link can view)
- Write access uses the management token (in URL query param for humans, in `Authorization: Bearer` header for API)
- This is the Pastebin/Excalidraw/Doodle model

**Why:** Accounts add friction. For v1, getting users matters more than user management. Accounts can be added later as an optional upgrade path (manage multiple resources under one identity).

## No Premium Services

There are no paid tiers, premium features, or usage-based billing. Everything is free and open. This may change later, but v1 treats all users equally.

## Spam Prevention

Not a v1 concern. Getting users is the priority — we haven't launched yet. If spam becomes a real problem, address it then. Don't over-engineer defenses for traffic that doesn't exist.

Lightweight measures that DON'T add friction are fine (rate limiting by IP, basic input validation). Anything that adds signup steps or verification is not.

## API Design

- **RESTful JSON APIs** with OpenAPI specs
- **No auth required for read operations** (viewing, listing, searching)
- **Minimal auth for write operations** (resource-scoped tokens, not global accounts)
- **Return everything the caller needs** in creation responses (IDs, tokens, URLs)
- **AI-friendly:** Consistent JSON responses, clear error messages, OpenAPI spec for tool integration
- **Human-friendly:** Frontend served from the same binary, share URLs that render nicely

## Share URLs

AI agents should be able to generate URLs they can hand to humans. These URLs should:
- Work immediately (no login wall)
- Render a useful UI (not raw JSON)
- Be bookmarkable
- Contain all necessary access info (embedded tokens for management URLs)

## Tech Stack

- **Backend:** Rust (Rocket framework), SQLite
- **Frontend:** React + TypeScript + Vite
- **Deployment:** Single binary serves both API and static frontend
- **No external dependencies:** No Redis, no Postgres, no external auth providers

## Build Session Guidance

If you're an AI build session working on these projects:
- Read `DESIGN.md` in the repo for project-specific decisions
- Read `STATUS.md` for what's done and what's next
- Follow these principles — don't add auth where it's not needed
- When in doubt, less friction > more security for v1

## AI Discovery: SKILL.md as Canonical, llms.txt as Alias

Every HNR service uses `SKILL.md` as the canonical AI-readable guide for that service.

**Repo:** `SKILL.md` at the project root — this is the source of truth.

**HTTP:** `GET /llms.txt` and `GET /SKILL.md` both serve the same content (the SKILL.md file). `llms.txt` exists only as a widely-recognized alias.

**Format:** SKILL.md should cover:
- One-line description of what the service does
- Quick start (the single API call that gets an agent started)
- Core endpoints with request/response shapes
- Auth model
- Any agent-specific gotchas

**Why SKILL.md over llms.txt:**
- `llms.txt` is a convention with no standard format
- `SKILL.md` aligns with the OpenClaw skill ecosystem and clawhub discovery
- Agents installing skills via `npx clawhub install <name>` expect SKILL.md

**Implementation for HTTP services:**
- Embed `SKILL.md` at compile time (Rust: `rust-embed` or `include_str!`; Node: `fs.readFileSync` at startup)
- Serve at both `/SKILL.md` and `/llms.txt`
- `/.well-known/skills/index.json` references `/SKILL.md` as the primary skill URL
