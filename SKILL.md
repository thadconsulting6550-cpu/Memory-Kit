# Memory Pattern Skill

**Teaches an agent to remember across sessions using local indexing.**

## Why This Exists

Vector search is broken in Heyron containers. This skill teaches a working alternative using local file-based indexing.

## What the Agent Learns

### 1. When to Index
- After every session write
- When new memory files are created
- Weekly maintenance

### 2. How to Search
```
python3 memory-index.py --search "keyword"
python3 memory-index.py --query "what did we discuss yesterday"
```

### 3. Salience System
Important memories get boosted:
- **Urgency:** "urgent", "critical", "asap", "deadline"
- **Emotion:** "excited", "frustrated", "worried"
- **Action:** "remember", "don't forget", "must"
- **Errors:** "bug", "fix", "broken"

## Installation

```bash
# Copy to workspace
cp -r memory-pattern-skill/ ~/

# Build index
python3 memory-pattern-skill/scripts/SYSTEM/memory_index.py --build
```

## Usage

```bash
# Search memories
python3 memory-pattern-skill/scripts/SYSTEM/memory_index.py --search "project name"

# Query naturally
python3 memory-pattern-skill/scripts/SYSTEM/memory_index.py --query "what does Austin care about"

# Find important stuff
python3 memory-pattern-skill/scripts/SYSTEM/memory_index.py --salient
```

## Integration

Add to your SOUL.md:
```
## Memory System
- Run memory_index.py --build after session writes
- Search before answering "what did we discuss"
- Check salience for priority memories
```

## What Makes This Different

| Feature | This Skill | Vector Search |
|---------|-----------|---------------|
| Works offline | ✅ | ❌ |
| No API needed | ✅ | ❌ |
| Free | ✅ | ❌ |
| Reliable | ✅ | ❌ |

---

**MIT License** - Built by Thad for Austin's setup 🐺