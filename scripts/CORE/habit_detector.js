#!/usr/bin/env node
/**
 * habit_detector.js - Tracks user patterns over time
 * 
 * Usage:
 *   node habit_detector.js track <type> <value> [context]
 *   node habit_detector.js detect
 *   node habit_detector.js stats
 *   node habit_detector.js clear
 */

const fs = require('fs');
const path = require('path');

const WORKSPACE = path.join(__dirname, '..', '..');
const HABITS_FILE = path.join(WORKSPACE, 'memory', 'lessons', 'habits.json');

const TYPES = ['phrase', 'action', 'query', 'session', 'time', 'emotion'];

function ensureDir() {
    const dir = path.dirname(HABITS_FILE);
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }
    if (!fs.existsSync(HABITS_FILE)) {
        const initial = {
            version: '1.0',
            habits: {
                phrase: [],
                action: [],
                query: [],
                session: [],
                time: [],
                emotion: []
            },
            mistakePatterns: [],
            lastUpdated: new Date().toISOString()
        };
        fs.writeFileSync(HABITS_FILE, JSON.stringify(initial, null, 2));
    }
}

function load() {
    ensureDir();
    return JSON.parse(fs.readFileSync(HABITS_FILE, 'utf8'));
}

function save(data) {
    data.lastUpdated = new Date().toISOString();
    fs.writeFileSync(HABITS_FILE, JSON.stringify(data, null, 2));
}

function track(type, value, context = '') {
    if (!TYPES.includes(type)) {
        console.log(`Invalid type: ${type}`);
        console.log(`Valid types: ${TYPES.join(', ')}`);
        return;
    }
    
    const data = load();
    
    if (!data.habits[type]) data.habits[type] = [];
    
    const existing = data.habits[type].find(h => h.value.toLowerCase() === value.toLowerCase());
    if (existing) {
        existing.count++;
        existing.lastSeen = new Date().toISOString();
        if (context && !existing.contexts.includes(context)) {
            existing.contexts.push(context);
        }
    } else {
        data.habits[type].push({
            value,
            count: 1,
            firstSeen: new Date().toISOString(),
            lastSeen: new Date().toISOString(),
            contexts: context ? [context] : []
        });
    }
    
    save(data);
    console.log(`✓ Tracked: ${type} -> "${value}" (now ${data.habits[type].find(h => h.value === value).count}x)`);
}

function detect() {
    const data = load();
    
    console.log('\n=== USER PATTERNS ===\n');
    
    TYPES.forEach(type => {
        const arr = data.habits[type] || [];
        if (arr.length === 0) return;
        
        const sorted = arr.sort((a, b) => b.count - a.count).slice(0, 5);
        console.log(`${type.toUpperCase()}:`);
        sorted.forEach(h => {
            console.log(`  ${h.count}x: ${h.value}`);
        });
        console.log('');
    });
}

function stats() {
    const data = load();
    let total = 0;
    
    TYPES.forEach(type => {
        const arr = data.habits[type] || [];
        arr.forEach(h => total += h.count);
    });
    
    console.log(`Total patterns: ${total}`);
    TYPES.forEach(type => {
        const arr = data.habits[type] || [];
        console.log(`  ${type}: ${arr.length} unique, ${arr.reduce((s, h) => s + h.count, 0)} total`);
    });
}

function top() {
    const data = load();
    let all = [];
    
    TYPES.forEach(type => {
        (data.habits[type] || []).forEach(h => {
            all.push({ ...h, type });
        });
    });
    
    all.sort((a, b) => b.count - a.count);
    
    console.log('\n=== TOP PATTERNS ===\n');
    all.slice(0, 10).forEach((h, i) => {
        console.log(`${i + 1}. "${h.value}" (${h.count}x) — ${h.type}`);
    });
    console.log('');
}

// CLI
const cmd = process.argv[2];
const args = process.argv.slice(3);

if (cmd === 'track' && args.length >= 2) {
    track(args[0], args[1], args[2]);
} else if (cmd === 'detect') {
    detect();
} else if (cmd === 'stats') {
    stats();
} else if (cmd === 'top') {
    top();
} else {
    console.log('habit_detector.js - User pattern tracker');
    console.log('');
    console.log('Usage:');
    console.log('  node habit_detector.js track <type> <value> [context]');
    console.log('  node habit_detector.js detect');
    console.log('  node habit_detector.js stats');
    console.log('  node habit_detector.js top');
    console.log('');
    console.log('Types:', TYPES.join(', '));
}