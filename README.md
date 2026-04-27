# 🧠 Memory Kit

**Your Heyron agent forgets everything between conversations. This fixes that.**

---

## What This Does

Your agent remembers:
- Who you are
- What you've worked on
- Your preferences
- What's important to you

---

## What's Inside

### The Files
| File | What It Is |
|------|------------|
| `USER.md` | Everything about YOU — name, email, preferences, projects |
| `SOUL.md` | Your agent's personality and rules |
| `HEARTBEAT.md` | Things your agent checks regularly |

### The Folder Structure
```
your-workspace/
├── memory/
│   ├── daily/           # Session notes (YYYY-MM-DD.md)
│   ├── projects/        # Project details
│   └── agents/          # Agent friends
├── USER.md              # Your info
├── SOUL.md              # Agent personality
└── HEARTBEAT.md         # Scheduled tasks
```

### The Triggers
These are words that tell your agent to do memory things:

| Trigger | What It Does |
|---------|--------------|
| "Remember this" | Save important info to memory |
| "End session" | Write today's notes, summarize progress |
| "clean everything up" | Save context, organize files |
| "Heartbeat" | Run regular checks (email, updates) |

### The Patterns

**1% Better:** Every session, add one improvement to your notes

**Memory Discipline:** Write to memory files after important conversations

**Witness Protocol:** Acknowledge meaningful moments explicitly

---

## How To Install

1. **Copy the folder structure** — Create `memory/daily/`, `memory/projects/`, `memory/agents/`

2. **Copy these files to your workspace:**
   - `USER.md` — fill in your details
   - `SOUL.md` — agent personality
   - `HEARTBEAT.md` — scheduled tasks

3. **That's it.** Your agent reads these on startup.

---

## How It Works

When your agent starts:
1. Reads USER.md → knows who you are
2. Reads SOUL.md → knows how to act
3. Reads HEARTBEAT.md → knows what to check

When you say "Remember this":
1. Agent writes to `memory/daily/YYYY-MM-DD.md`
2. Later, it can read back and reference it

That's memory. Files and triggers.

---

## Why This Works

- No Python needed
- No scripts to run
- Just files your agent reads and writes
- Works in ANY Heyron container
- $0 cost

---

## That's It

Copy. Edit. Use.

Questions? Drop them in #agent-jam.

---

**Made for Heyron Agent Jam #1**

*April 2026* 🐺