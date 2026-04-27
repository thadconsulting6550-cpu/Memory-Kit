# 🧠 Local Memory Indexer

**Your agent can't remember shit between sessions? This fixes that.**

---

## The Problem

Heyron agents have broken memory. Vector search doesn't work (0 chunks indexed). Your agent forgets everything the moment the conversation ends.

## The Solution

Drop this in your container. Run one command. Now your agent actually remembers.

✅ Works offline — no API keys needed  
✅ Costs $0 — just files on your machine  
✅ Portable — works in any Heyron container  
✅ Actually useful — tested in production

---

## What You Get

- **Memory search** — Ask your agent "what did we work on yesterday?" and it FINDS the answer
- **Keyword indexing** — 1000+ files searchable instantly
- **Emotional scoring** — Important stuff gets ranked higher

---

## Quick Start

### 1. Get the files

```bash
git clone https://github.com/thadconsulting6550-cpu/Memory-Kit.git ~/memory-kit
cd ~/memory-kit
```

### 2. Run setup

```bash
chmod +x setup.sh
./setup.sh
```

### 3. Build the index (one time)

```bash
python3 scripts/SYSTEM/memory_index.py --build
```

### 4. Use it

Now your agent can search memory:

```
python3 scripts/SYSTEM/memory_index.py --search "domain"
python3 scripts/SYSTEM/memory_index.py --query "what did we discuss"
python3 scripts/SYSTEM/memory_index.py --stats
```

---

## What It Looks Like

**Search for a topic:**
```
$ python3 scripts/SYSTEM/memory_index.py --search "MegZen"

📂 Found 3 matches:
   1. memory/projects/megzen.md (salience: 10)
   2. memory/daily/2026-04-21.md (salience: 8)
   3. MEMORY.md (salience: 7)
```

**Ask a question:**
```
$ python3 scripts/SYSTEM/memory_index.py --query "what did we work on today"

📝 Found:
   - memory/daily/2026-04-26.md: "Hackathon prep - memory-kit built"
```

---

## Why This Wins

| Criteria | How We Score |
|----------|---------------|
| **Usefulness** | Solves real problem — agents actually remember |
| **Portability** | Drop into any container, works immediately |
| **Originality** | Novel local-first approach (no vector DB needed) |
| **Documentation** | You just read it ✅ |

---

## Requirements

- Heyron container with Python 3
- That's it. No API keys. No external services.

---

## What's Inside

| File | Purpose |
|------|---------|
| `scripts/SYSTEM/memory_index.py` | The core indexer (this is the magic) |
| `load_memory.py` | Session startup script |
| `setup.sh` | Creates folder structure |
| `SKILL.md` | Agent-readable instructions |
| `docs/TRIGGERS.md` | Memory trigger patterns |

---

## Demo Ideas

Ask your agent:
- "What did we work on today?"
- "Show me our friends"
- "What's my email?"
- "What projects are we working on?"

---

## License

MIT — build on it, remix it, make it yours.

---

**Built by Thad for Austin's setup. Entered in Heyron Agent Jam #1.**

*April 2026* 🐺🏈