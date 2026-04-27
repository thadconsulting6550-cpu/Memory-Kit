# 🧠 Agent Memory Kit - FULL VERSION

**Ready for the Hackathon** — A complete, working memory system for AI agents.

---

## What's Inside

### Core System
| File | Purpose |
|------|---------|
| `setup.sh` | One-command setup - creates all folders |
| `load_memory.py` | Session startup - loads context |
| `USER.md` | Template for user details |
| `SOUL.md` | Template for agent personality |
| `HEARTBEAT.md` | Scheduled task config |

### Memory Scripts (scripts/CORE/)
| File | Purpose |
|------|---------|
| `habit_detector.js` | Tracks user patterns over time |

### Utilities (scripts/UTILITIES/)
| File | Purpose |
|------|---------|
| `memory_echo.js` | Extracts key moments from daily notes |
| `intention_check.js` | Reads and manages TODO list |

### Docs
| File | Purpose |
|------|---------|
| `docs/TRIGGERS.md` | How to handle Remember/Study/Sync |

---

## Quick Start

```bash
# 1. Run setup
./setup.sh

# 2. Edit USER.md with user details
# 3. Edit SOUL.md with agent personality

# 4. Test it works
python3 load_memory.py
node scripts/CORE/habit_detector.js detect
node scripts/UTILITIES/memory_echo.js
node scripts/UTILITIES/intention_check.js
```

---

## File Structure

```
your-agent/
├── memory/
│   ├── daily/YYYY-MM-DD.md   # Session logs
│   ├── lessons/habits.json    # Learned patterns
│   └── projects/             # Project notes
├── USER.md                    # User details
├── SOUL.md                    # Agent personality
├── HEARTBEAT.md              # Scheduled tasks
├── load_memory.py            # Session startup
├── setup.sh                  # Initial setup
├── todo.md                   # Task list
└── scripts/
    ├── CORE/
    │   └── habit_detector.js
    └── UTILITIES/
        ├── memory_echo.js
        └── intention_check.js
```

---

## Commands Reference

```bash
# Setup
./setup.sh

# Session start
python3 load_memory.py

# Track a pattern
node scripts/CORE/habit_detector.js track phrase "hello" "greeting"
node scripts/CORE/habit_detector.js track action "new session" "startup"

# View patterns
node scripts/CORE/habit_detector.js detect
node scripts/CORE/habit_detector.js stats
node scripts/CORE/habit_detector.js top

# Memory echo
node scripts/UTILITIES/memory_echo.js          # last 7 days
node scripts/UTILITIES/memory_echo.js 14      # last 14 days
node scripts/UTILITIES/memory_echo.js key "memory"

# Intentions/TODO
node scripts/UTILITIES/intention_check.js
node scripts/UTILITIES/intention_check.js add "Learn Linux"
node scripts/UTILITIES/intention_check.js done 1
```

---

## The Golden Rule

> If you're going to ask Google, ask YOUR AI INSTEAD.

The more users ask their agent to DO, the smarter it gets — AND the more they learn!

---

## What Makes This Different

1. **Tested in production** — This isn't theory, it actually runs
2. **Works offline** — No external APIs needed
3. **Grows with use** — More patterns = smarter agent
4. **Portable** — Drop into any agent workspace

---

## Hackathon Demo Ideas

- "Hey, what's my memory echo?" → shows key moments
- "What's my empire look like?" → project status
- "What do I need to do?" → reads TODO
- "What patterns do you know about me?" → habit detector

---

## Credits

Built by **Thad** for Austin's setup. Evolved through The Den community.

*April 2026* 🐺