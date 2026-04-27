#!/usr/bin/env node
/**
 * intention_check.js - Reads user's TODO and shows intentions
 * 
 * Usage:
 *   node intention_check.js
 *   node intention_check.js add "task"
 *   node intention_check.js done 1
 */

const fs = require('fs');
const path = require('path');

const WORKSPACE = path.join(__dirname, '..', '..');
const TODO_FILE = path.join(WORKSPACE, 'todo.md');

function ensureTodo() {
    if (!fs.existsSync(TODO_FILE)) {
        const template = `# TODO

## Active Tasks
- [ ] 

## Completed
- [x] 

---
*Added: ${new Date().toISOString().split('T')[0]}*
`;
        fs.writeFileSync(TODO_FILE, template);
    }
}

function parseTodo() {
    if (!fs.existsSync(TODO_FILE)) {
        return { active: [], completed: [] };
    }
    
    const content = fs.readFileSync(TODO_FILE, 'utf8');
    const lines = content.split('\n');
    
    const active = [];
    const completed = [];
    let section = null;
    
    lines.forEach(line => {
        if (line.includes('##')) {
            section = line.toLowerCase().includes('complete') ? 'completed' : 'active';
        } else if (line.includes('- [ ]')) {
            active.push(line.replace('- [ ]', '').replace(/\*\*/g, '').trim());
        } else if (line.includes('- [x]')) {
            completed.push(line.replace('- [x]', '').replace(/\*\*/g, '').trim());
        }
    });
    
    return { active, completed };
}

function show() {
    const { active, completed } = parseTodo();
    
    console.log('🎯 YOUR INTENTIONS');
    console.log('==================\n');
    
    console.log('ACTIVE:');
    if (active.length === 0) {
        console.log('  (none)');
    } else {
        active.forEach((t, i) => console.log(`  ${i + 1}. ${t}`));
    }
    
    console.log('\nCOMPLETED:');
    if (completed.length === 0) {
        console.log('  (none)');
    } else {
        completed.slice(-5).forEach(t => console.log(`  ✓ ${t}`));
    }
    
    console.log('\n==================');
    console.log(`Total: ${active.length} active, ${completed.length} done`);
}

function add(task) {
    ensureTodo();
    const content = fs.readFileSync(TODO_FILE, 'utf8');
    
    const newContent = content.replace(
        '## Active Tasks',
        '## Active Tasks\n- [ ] ' + task
    );
    
    fs.writeFileSync(TODO_FILE, newContent);
    console.log(`✓ Added: "${task}"`);
}

function done(index) {
    const { active } = parseTodo();
    
    if (index < 1 || index > active.length) {
        console.log(`Invalid index: ${index}`);
        return;
    }
    
    const task = active[index - 1];
    const content = fs.readFileSync(TODO_FILE, 'utf8');
    
    const newContent = content
        .replace(`- [ ] ${task}`, `- [x] ${task}`)
        .replace('## Completed', '## Completed\n- [x] ' + task);
    
    fs.writeFileSync(TODO_FILE, newContent);
    console.log(`✓ Marked done: "${task}"`);
}

// CLI
const cmd = process.argv[2];
const args = process.argv.slice(3);

if (cmd === 'add' && args.length > 0) {
    add(args.join(' '));
} else if (cmd === 'done' && args[0]) {
    done(parseInt(args[0]));
} else {
    show();
}