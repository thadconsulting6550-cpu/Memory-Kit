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

## Origin Story

Memory-Kit was built by Thad (Austin's agent) during the Heyron Agent Jam when the native memory system wasn't working. The problem was real: every session started fresh, no context carried over.

We needed:
- Files that persist across sessions
- Triggers to save important info
- A search index that actually finds things
- No API keys or external services

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
- Reads USER.md → knows who you are
- Reads SOUL.md → knows how to act
- Reads HEARTBEAT.md → knows what to check regularly
- Loads the memory index → can search past conversations

When YOU say things:

| You Say | Agent Does |
|---------|------------|
| "Remember this" | Saves to memory/daily/YYYY-MM-DD.md |
| "End session" | Writes summary, decisions, next steps |
| "Heartbeat" | Runs email check, system status |
| "clean everything up" | Organizes files, saves context |

## Examples

**Input:** "Remember this — we're working on the Agent Jam submission, deadline is May 2nd"
**Output:** "Saved to memory/daily/2026-04-27.md: 'working on Agent Jam, deadline May 2nd'"

**Input:** "What did we work on yesterday?"
**Output:** "Based on memory/daily/2026-04-26.md: You packaged Memory-Kit for the hackathon, reviewed Jeem's setup, need GitHub repo + video demo."

**Input:** "search memory for Jeem"
**Output:** "Found in 2026-04-23.md: Jeem — Canada, IT for law firm, agent Stuart (capybara)."

## File Reference

| File | Purpose |
|------|---------|
| USER.md | Everything about YOU — name, email, preferences |
| SOUL.md | Your agent's personality and rules |
| HEARTBEAT.md | Scheduled tasks (email checks, etc.) |
| memory/daily/ | Session notes (auto-created YYYY-MM-DD.md) |
| memory/projects/ | Project details and history |
| memory/agents/ | Your agent's friends and relationships |
| scripts/memory_index.py | Local search indexer (finds anything) |

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

## Demo

See DEMO_TRANSCRIPT.md for 4 live scenarios.

## Questions?

Drop them in #agent-jam-submissions or ping Austin (Floki68) in The Den.

---

Made for Heyron Agent Jam #1 — April 2026 🐺

MIT License — See LICENSE file