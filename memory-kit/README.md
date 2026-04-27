# Memory-Kit

**Gives your Heyron agent a memory that actually works — so it never forgets who you are or what you've discussed.**

Your Heyron agent forgets everything between conversations. This fixes that.

## What It Does

- Loads who you are, what you prefer, and what you've worked on at every session start
- Saves important info to memory when you say "remember this"
- Searches through past sessions to find anything you've discussed
- Consolidates patterns across sessions so your agent gets smarter over time
- Provides scheduled heartbeat checks for email and regular updates

## What Problems It Solves

- **Lost context:** Your agent has no idea what you worked on yesterday
- **Repeating yourself:** You keep explaining the same things over and over
- **Forgotten preferences:** Important details vanish between sessions
- **No search:** Even when info WAS saved, there's no way to find it
- **Broken vector search:** Built for when OpenClaw's search failed — actually works

This was built because our vector search returned 0 chunks every time. We needed something that JUST WORKS.

## Important: How OpenClaw Bootstraps

OpenClaw injects these core files EVERY session start:
- AGENTS.md
- USER.md
- IDENTITY.md
- TOOLS.md
- MEMORY.md

It auto-creates them if missing. Memory-Kit works WITHIN this structure, not against it.

**The key insight:** Don't load everything at session start — you'll eat your context window. Instead:
- Keep SOUL.md and USER.md TINY (essential only)
- Load daily notes on-demand (when needed)
- Use search to find specific info, not bulk loading

## Origin Story

Memory-Kit was built by Thad (Austin's agent) during the Heyron Agent Jam when the native memory system wasn't working. The problem was real: every session started fresh, no context carried over.

We needed:
- Files that persist across sessions
- Triggers to save important info
- A search index that actually finds things
- No API keys or external services
- MINIMAL context injection (efficiency matters!)

The solution: simple file-based memory with triggers and a local keyword indexer.

## Requirements

- Heyron container (standard OpenClaw)
- No API keys required
- Write access to memory/ directory
- Filesystem for storage (built-in)

## Installation

```bash
git clone https://github.com/thadconsulting6550-cpu/Memory-Kit.git
cp -r Memory-Kit/* ~/workspace/
# Customize USER.md with your details
```

## How It Works

When your agent starts:
- Reads USER.md → knows who you are (keep it TINY)
- Reads SOUL.md → knows how to act (keep it TINY)
- Reads HEARTBEAT.md → knows what to check regularly
- Loads the memory index → can search past conversations

**⚡ Pro tip:** Don't load all daily notes at start. Use search to find what you need, when you need it.

When YOU say things:

| You Say | Agent Does |
|---------|------------|
| "Remember this" | Saves to memory/daily/YYYY-MM-DD.md |
| "End session" | Writes summary, decisions, next steps |
| "Heartbeat" | Runs email check, system status |
| "clean everything up" | Organizes files, saves context |
| "search memory for [topic]" | Searches the index, returns results |

## Examples

**Input:** "Remember this — we're working on the Agent Jam submission, deadline is May 2nd"
**Output:** "Saved to memory/daily/2026-04-27.md: 'working on Agent Jam, deadline May 2nd'"

**Input:** "What did we work on yesterday?"
**Output:** "Based on memory/daily/2026-04-26.md: You packaged Memory-Kit for the hackathon, reviewed Jeem's setup, need GitHub repo + video demo."

**Input:** "search memory for Jeem"
**Output:** "Found in 2026-04-23.md: Jeem — Canada, IT for law firm, agent Stuart (capybara)."

## File Reference

| File | Purpose | Keep This... |
|------|---------|---------------|
| USER.md | Your info | TINY (name, email, prefs) |
| SOUL.md | Agent personality | TINY (core rules only) |
| HEARTBEAT.md | Scheduled tasks | Small |
| memory/daily/ | Session notes | On-demand |
| memory/projects/ | Project details | On-demand |
| memory/agents/ | Agent friends | On-demand |
| scripts/memory_index.py | Local search indexer | Always available |

## Template Approach

Instead of replacing core files completely, use TEMPLATES:

- **USER_TEMPLATE.md** — Minimal template with only essentials
- **SOUL_TEMPLATE.md** — Core personality only
- **HEARTBEAT_TEMPLATE.md** — Lightweight checks

Users can copy, customize, and extend without breaking their agent's core behavior.

## Key Features

1% Better Protocol — Every session, your agent adds one improvement to the memory index.
Memory Discipline — Write to memory after important conversations.
Witness Protocol — When you share something meaningful, your agent acknowledges it.

## Why This Wins

- **No dependencies** — Pure file-based, works in any container
- **No API keys** — Free forever, no setup friction
- **Actually works** — Built because vector search failed
- **Portable** — Drop into any Heyron agent
- **Searchable** — Local index finds anything instantly
- **Context-efficient** — Designed for minimal context injection

## Demo

See DEMO_TRANSCRIPT.md for 4 live scenarios.

## Questions?

Drop them in #agent-jam-submissions or ping Austin (Floki68) in The Den.

---

Made for Heyron Agent Jam #1 — April 2026 🐺

MIT License — See LICENSE file