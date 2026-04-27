#!/usr/bin/env python3
"""
load_memory.py - Full Session Startup Loader
Run at the START of every session.
"""

import os
import sys
from datetime import date, datetime

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
MEMORY_DIR = os.path.join(WORKSPACE, "memory")
DAILY_DIR = os.path.join(MEMORY_DIR, "daily")
LESSONS_DIR = os.path.join(MEMORY_DIR, "lessons")

CORE_FILES = ["USER.md", "SOUL.md", "HEARTBEAT.md", "MEMORY.md"]

def log(msg):
    print(f"  {msg}")

def ensure_dirs():
    """Create folder structure if missing."""
    for d in [DAILY_DIR, LESSONS_DIR, os.path.join(MEMORY_DIR, "projects")]:
        if not os.path.exists(d):
            os.makedirs(d, exist_ok=True)

def get_today_file():
    """Get or create today's memory file."""
    today = date.today().strftime("%Y-%m-%d")
    filepath = os.path.join(DAILY_DIR, f"{today}.md")
    
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(f"# Memory: {today}\n\n## Summary\n\n### Topics Discussed\n- \n\n### Decisions Made\n- \n\n### Tasks\n- [ ] \n\n### Notes\n- \n")
    
    return filepath

def load_core_files():
    """Load core context files."""
    log("Loading context files:")
    loaded = []
    
    for fname in CORE_FILES:
        fpath = os.path.join(WORKSPACE, fname)
        if os.path.exists(fpath):
            loaded.append(fname)
            log(f"  ✓ {fname}")
        else:
            log(f"  ○ {fname} (will create)")
    
    return loaded

def get_memory_stats():
    """Get memory system statistics."""
    stats = {}
    
    # Count daily files
    if os.path.exists(DAILY_DIR):
        daily_files = [f for f in os.listdir(DAILY_DIR) if f.endswith('.md')]
        stats['daily_files'] = len(daily_files)
        stats['latest'] = sorted(daily_files)[-1] if daily_files else "none"
    
    # Check habits
    habits_file = os.path.join(LESSONS_DIR, "habits.json")
    if os.path.exists(habits_file):
        import json
        with open(habits_file) as f:
            data = json.load(f)
            stats['habits'] = sum(len(v) for v in data.get('habits', {}).values())
    
    return stats

def run():
    """Main startup sequence."""
    print("\n🧠 MEMORY SYSTEM STARTING")
    print("=" * 30)
    
    ensure_dirs()
    
    # Load today's file
    today_file = get_today_file()
    log(f"Today: {today_file}")
    
    # Load context
    loaded = load_core_files()
    
    # Get stats
    stats = get_memory_stats()
    print("")
    log(f"Memory files: {stats.get('daily_files', 0)}")
    log(f"Patterns tracked: {stats.get('habits', 0)}")
    
    print("")
    print("=" * 30)
    print("✅ CONTEXT LOADED - READY")
    print(f"   {datetime.now().strftime('%H:%M')}")
    print("")

if __name__ == "__main__":
    run()