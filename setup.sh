#!/bin/bash
# Memory Kit Setup - Run once to initialize
# Usage: ./setup.sh

echo "🧠 MEMORY KIT SETUP"
echo "===================="

WORKSPACE="$(cd "$(dirname "$0")" && pwd)"

# Create folder structure
echo "Creating folders..."
mkdir -p "$WORKSPACE/memory/daily"
mkdir -p "$WORKSPACE/memory/lessons"
mkdir -p "$WORKSPACE/memory/projects"
mkdir -p "$WORKSPACE/memory/axiom"
mkdir -p "$WORKSPACE/downloads"

# Create core files
echo "Creating core files..."

# USER.md
cat > "$WORKSPACE/USER.md" << 'EOF'
# USER.md - About Your Human

*Fill this in with details about your user.*

- **Name:** 
- **Timezone:** 
- **What they care about:**
- **What annoys them:**
- **Notes:**
EOF

# SOUL.md
cat > "$WORKSPACE/SOUL.md" << 'EOF'
# SOUL.md - Agent Personality

*Define who your agent is.*

## Core Traits
- 
- 

## Rules
- 

## Memory Triggers
- "Remember" → save to daily file
- "Study" → reload context
- "Full Sync" → check status
EOF

# HEARTBEAT.md
cat > "$WORKSPACE/HEARTBEAT.md" << 'EOF'
# HEARTBEAT.md - Scheduled Tasks

# Session Start
- Run: python3 load_memory.py

# Daily
- Check email (if configured)
- Memory cleanup

# Weekly
- Review patterns
- Update MEMORY.md
EOF

# Create today's memory file
TODAY=$(date +%Y-%m-%d)
cat > "$WORKSPACE/memory/daily/${TODAY}.md" << EOF
# Memory: $TODAY

## Summary

### Topics Discussed

### Decisions Made

### Tasks

### Notes
EOF

# Initialize habits.json
echo '{"habits":{},"lastUpdated":"'$(date -Iseconds)'"}' > "$WORKSPACE/memory/lessons/habits.json"

# Make scripts executable
chmod +x "$WORKSPACE"/*.sh 2>/dev/null
chmod +x "$WORKSPACE/scripts/"* 2>/dev/null
chmod +x "$WORKSPACE/scripts/CORE/"* 2>/dev/null
chmod +x "$WORKSPACE/scripts/UTILITIES/"* 2>/dev/null

echo ""
echo "✅ SETUP COMPLETE"
echo ""
echo "Next steps:"
echo "1. Edit USER.md with user details"
echo "2. Edit SOUL.md with agent personality"
echo "3. Run: python3 load_memory.py"
echo ""
echo "Your memory system is ready! 🧠"