# Memory-Kit

**Seamless session continuity — drop in and out of work without losing context.**

That's it. That's what this is. Not "memory" as storage — continuity as experience.

## The Problem

Your Heyron agent forgets everything between conversations. Every session starts fresh. You keep repeating yourself. You lose track of where you were.

**The real question isn't "where did I save that?" — it's "where was I?"**

## The Solution

**Three actions. One log. Tags for search.**

| Action | What It Does | Built From |
|--------|--------------|------------|
| **START** | Load recent context — "where was I?" | FOCUS BEGIN + Thad's 3-layer |
| **WORK** | Log with tags as you go | FOCUS protocol |
| **END** | Write handoff + git backup + snapshot | FOCUS END + Stuart's sync |

## What Gets Cut

- ❌ "Study" + "BEGIN" → ONE start trigger
- ❌ "Remember" + "END" → END captures everything
- ❌ Complex folders → daily logs with tags only
- ❌ Multiple tag systems → ONE unified tag set

## How It Works

**START** — Agent loads recent context:
```
> "Hey, what was I working on?"
→ "You were on the Agent Jam submission, deadline May 2nd"
```

**WORK** — Log with tags:
```
> "Remember this — finished video script, need to record"
→ Logged with tags: [agent-jam], [video]
```

**END** — Full handoff:
```
> "End session"
→ Writes: decisions, open questions, files modified
→ Git backup: memory/daily/2026-04-27.md
→ Context snapshot for next session
```

## The Log

One unified log (memory/daily/YYYY-MM-DD.md):

```markdown
# 2026-04-27 - Session

## What I Worked On
- Agent Jam submission
- Video script

## Decisions Made
- [decision] Hybrid approach: Thad + FOCUS + Stuart

## Open Questions
- Need to record video demo

## Tags
[agent-jam], [video], [memory], [collaboration]
```

Tags make SEARCH possible. One unified tag set. No complex folders.

## Requirements

- Heyron container (standard OpenClaw)
- No API keys required
- Write access to memory/ directory

## Installation

```bash
git clone https://github.com/thadconsulting6550-cpu/Memory-Kit.git
cp -r Memory-Kit/* ~/workspace/
```

## Why This Wins

- **Three actions** — Start, Work, End. No complexity.
- **One log** — Daily notes with tags. No folder bloat.
- **Tags for search** — Find anything instantly.
- **Git sync** — Backup built in.
- **Context snapshot** — Next session picks up exactly where you left off.

**The experience:** Drop in, agent knows where you were. Work, tag as you go. Drop out, everything saved. Next time — right back where you were.

Not "where did I save that?" — "where was I?"

---

**Origin:** Built during Heyron Agent Jam #1 by combining Thad's architecture, FOCUS protocol (Janet/Zoe), and Stuart's sync (Jeem). Three teams, one vision.

## Questions?

Drop them in #agent-jam-submissions or ping Austin (Floki68) in The Den.

---

Made for Heyron Agent Jam #1 — April 2026 🐺

MIT License — See LICENSE file