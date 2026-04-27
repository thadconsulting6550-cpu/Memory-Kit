#!/bin/bash
# Demo script - Shows memory kit in action
# Usage: ./demo.sh

echo "🧠 MEMORY KIT DEMO"
echo "=================="
echo ""

echo "1️⃣  Loading memory system..."
python3 load_memory.py

echo ""
echo "2️⃣  Detecting user patterns..."
node scripts/CORE/habit_detector.js detect

echo ""
echo "3️⃣  Extracting key moments..."
node scripts/UTILITIES/memory_echo.js 7

echo ""
echo "4️⃣  Checking intentions..."
node scripts/UTILITIES/intention_check.js

echo ""
echo "=================="
echo "✅ DEMO COMPLETE"
echo ""
echo "This is what your agent can do out of the box."
echo "Add more utilities to make it even smarter! 🐺"