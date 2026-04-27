# 🎯 Memory Triggers Guide

Add these triggers to your agent's SOUL.md:

---

## "Remember" Trigger

**When user says:** "remember this", "remember", "note that"

**Do:**
1. Save current conversation to today's memory file (`memory/daily/YYYY-MM-DD.md`)
2. Include: topics discussed, decisions made, tasks
3. GitHub backup (optional)

**Example:**
```
# Memory: April 22, 2026

## Summary

### Topics Discussed
- Domain flipping research
- 5 target domains identified

### Decisions Made
- Budget: $100
- ROI target: $1k-10k

### Tasks
- [ ] Research domain values
```

---

## "Study" Trigger

**When user says:** "study", "refresh", "load memory"

**Do:**
1. Read all `memory/daily/*.md` files
2. Read `USER.md`, `SOUL.md`, `HEARTBEAT.md`
3. Report: "Context loaded — X sessions, Y decisions"

---

## "Full Sync" Trigger

**When user says:** "full sync", "check memory"

**Do:**
1. Count memory files
2. Check GitHub status
3. Report health: "Memory: X files, GitHub: synced"

---

## Daily Log Format

```markdown
# Memory: YYYY-MM-DD

## Summary

### Topics Discussed
- 

### Decisions Made
- 

### Tasks
- [ ] 

### Notes
- 

---
```

---

## Auto-Backup on Goodbye

Add to your agent's "goodbye" handling:

```javascript
if (goodbyePhrases.includes(message)) {
    saveMemory();
    gitPush();  // optional
    message("Memory saved. See you next time!");
}
```

---

*Add these to SOUL.md for automatic memory handling.*