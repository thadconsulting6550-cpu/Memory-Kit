#!/usr/bin/env node
/**
 * memory_echo.js - Extracts key moments from daily notes
 * 
 * Usage:
 *   node memory_echo.js
 *   node memory_echo.js 7    # last 7 days
 *   node memory_echo.js key "search term"
 */

const fs = require('fs');
const path = require('path');

const WORKSPACE = path.join(__dirname, '..', '..');
const DAILY_DIR = path.join(WORKSPACE, 'memory', 'daily');

const KEYWORDS = [
    'built', 'fixed', 'created', 'decided', 'milestone', 
    'breakthrough', 'first', 'dream', 'goal', 'launch',
    'released', 'deployed', 'shipped', 'completed'
];

function getFiles(days = 7) {
    if (!fs.existsSync(DAILY_DIR)) return [];
    
    const files = fs.readdirSync(DAILY_DIR)
        .filter(f => f.match(/^\d{4}-\d{2}-\d{2}\.md$/))
        .map(f => ({
            name: f,
            mtime: fs.statSync(path.join(DAILY_DIR, f)).mtime
        }))
        .sort((a, b) => b.mtime - a.mtime)
        .slice(0, days)
        .map(f => f.name);
    
    return files;
}

function extractMoments(content) {
    const lines = content.split('\n');
    const moments = [];
    
    lines.forEach(line => {
        const lower = line.toLowerCase();
        if (KEYWORDS.some(k => lower.includes(k))) {
            const clean = line.replace(/^#+\s*/, '').trim();
            if (clean && clean.length > 3) {
                moments.push(clean);
            }
        }
    });
    
    return moments;
}

function echo(days = 7) {
    const files = getFiles(days);
    
    console.log('📢 MEMORY ECHO');
    console.log('===============');
    console.log(`Last ${days} days:\n`);
    
    if (files.length === 0) {
        console.log('No memory files found.');
        return;
    }
    
    let totalMoments = 0;
    
    files.forEach(file => {
        const content = fs.readFileSync(path.join(DAILY_DIR, file), 'utf8');
        const moments = extractMoments(content);
        
        if (moments.length > 0) {
            const dateStr = file.replace('.md', '').replace(/^(\d{4})-(\d{2})-(\d{2})/, '$2/$3');
            console.log(`📅 ${dateStr}:`);
            moments.slice(0, 3).forEach(m => console.log(`   • ${m}`));
            console.log('');
            totalMoments += moments.length;
        }
    });
    
    console.log(`Total key moments: ${totalMoments}`);
    console.log('\n🧠 INSIGHT:');
    console.log('  You\'re a builder. Documentation is solid.');
    console.log('');
}

function search(query) {
    const files = getFiles(30);
    
    console.log(`🔍 SEARCH: "${query}"`);
    console.log('===============\n');
    
    files.forEach(file => {
        const content = fs.readFileSync(path.join(DAILY_DIR, file), 'utf8');
        if (content.toLowerCase().includes(query.toLowerCase())) {
            const lines = content.split('\n');
            const matches = lines.filter(l => l.toLowerCase().includes(query.toLowerCase()));
            if (matches.length > 0) {
                console.log(`📅 ${file}:`);
                matches.slice(0, 2).forEach(m => console.log(`   ${m.trim()}`));
                console.log('');
            }
        }
    });
}

// CLI
const args = process.argv.slice(2);

if (args[0] === 'key' && args[1]) {
    search(args.slice(1).join(' '));
} else if (args[0]) {
    echo(parseInt(args[0]) || 7);
} else {
    echo(7);
}