#!/usr/bin/env python3
"""
Memory Indexer - Local Search That Actually Works
No APIs, no embeddings, no bullshit. Just fast, reliable search.

ENHANCED with Emotional Boost (Axiom research):
- Detects emotional/urgent keywords
- Boosts salience score for important memories

Usage:
    python3 scripts/SYSTEM/memory_index.py --build     # Build index
    python3 scripts/SYSTEM/memory_index.py --search "domain flipping"  # Search
    python3 scripts/SYSTEM/memory_index.py --query "What did we discuss yesterday?"
    python3 scripts/SYSTEM/memory_index.py --salient   # Show high-salience memories
"""

import json
import re
import os
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

WORKSPACE = Path("/home/openclaw/.openclaw/workspace")
MEMORY_DIR = WORKSPACE / "memory"
INDEX_FILE = WORKSPACE / "memory" / ".memory_index.json"

# Emotional keywords that boost salience (from Axiom research)
EMOTIONAL_KEYWORDS = {
    # High urgency
    "urgent", "critical", "asap", "emergency", "important", "priority",
    "big deal", "huge", "breaking", "deadline", "time-sensitive",
    # Emotional weight  
    "excited", "frustrated", "angry", "happy", "sad", "love", "hate",
    "amazing", "terrible", "awesome", "worried", "scared", "hopeful",
    # Action triggers
    "remember", "don't forget", "must", "need to", "have to", "should",
    "won't forget", "this is key", "this matters", "pay attention",
    # Mistakes/errors
    "error", "bug", "fix", "broken", "fail", "wrong", "issue", "problem",
    # Wins/celebration
    "won", "success", "finished", "done", "completed", "working", "fixed",
    "legendary", "dary"
}

class MemoryIndexer:
    def __init__(self):
        self.index = {"files": {}, "keywords": defaultdict(list), "last_build": None}
        
    def build_index(self):
        """Scan all memory files and build searchable index"""
        print("🔨 Building memory index with Emotional Boost...")
        
        files_scanned = 0
        files_indexed = 0
        
        # Scan all .md files in workspace
        for md_file in WORKSPACE.rglob("*.md"):
            if ".git" in str(md_file):
                continue
                
            files_scanned += 1
            try:
                content = md_file.read_text(encoding='utf-8', errors='ignore')
                rel_path = str(md_file.relative_to(WORKSPACE))
                
                # Extract metadata
                title = self._extract_title(content)
                keywords = self._extract_keywords(content)
                dates = self._extract_dates(content)
                
                # NEW: Calculate salience score (emotional boost)
                salience = self._calculate_salience(content)
                
                # Store file info
                self.index["files"][rel_path] = {
                    "path": rel_path,
                    "title": title,
                    "keywords": keywords,
                    "dates": dates,
                    "salience": salience,  # NEW: emotional importance
                    "size": len(content),
                    "modified": datetime.fromtimestamp(md_file.stat().st_mtime).isoformat()
                }
                
                # Index keywords
                for keyword in keywords:
                    if rel_path not in self.index["keywords"][keyword]:
                        self.index["keywords"][keyword].append(rel_path)
                
                files_indexed += 1
                
            except Exception as e:
                print(f"  ⚠️ Error indexing {md_file}: {e}")
        
        self.index["last_build"] = datetime.now().isoformat()
        self.index["stats"] = {
            "files_scanned": files_scanned,
            "files_indexed": files_indexed,
            "keywords_indexed": len(self.index["keywords"])
        }
        
        # Save index
        self._save_index()
        
        print(f"✅ Indexed {files_indexed}/{files_scanned} files")
        print(f"✅ {len(self.index['keywords'])} keywords indexed")
        print(f"✅ Emotional salience scoring enabled")
        print(f"✅ Index saved to {INDEX_FILE}")
        
    def _calculate_salience(self, content):
        """
        Calculate salience score based on emotional keywords.
        From Axiom research: amygdala boosts memory for emotional events.
        """
        content_lower = content.lower()
        
        # Count emotional keyword matches
        matches = 0
        matched_keywords = []
        
        for keyword in EMOTIONAL_KEYWORDS:
            if keyword in content_lower:
                matches += 1
                matched_keywords.append(keyword)
        
        # Score: 0-10 scale based on density
        # More emotional keywords = higher salience
        if matches == 0:
            salience = 0
        elif matches <= 2:
            salience = 2
        elif matches <= 5:
            salience = 5
        elif matches <= 10:
            salience = 7
        else:
            salience = 10
            
        return salience
        
    def search(self, query, limit=5):
        """Search memory index for relevant files"""
        if not INDEX_FILE.exists():
            print("❌ No index found. Run: python3 memory_index.py --build")
            return []
            
        self._load_index()
        
        query_lower = query.lower()
        query_words = set(re.findall(r'\b\w+\b', query_lower))
        
        scores = defaultdict(float)
        
        # Score files based on keyword matches
        for word in query_words:
            if word in self.index["keywords"]:
                for filepath in self.index["keywords"][word]:
                    # NEW: Add salience boost to scoring
                    salience = self.index["files"].get(filepath, {}).get("salience", 0)
                    scores[filepath] += 1.0 + (salience * 0.2)  # Salience adds 0-2 points
                    
        # Boost scores for title matches
        for filepath, info in self.index["files"].items():
            title_lower = info.get("title", "").lower()
            if any(word in title_lower for word in query_words):
                scores[filepath] += 2.0
                
        # Sort by score
        results = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:limit]
        
        return results
        
    def get_salient_memories(self, min_salience=5):
        """Get memories with high emotional salience (from Axiom research)"""
        if not INDEX_FILE.exists():
            print("❌ No index found. Run: python3 memory_index.py --build")
            return []
            
        self._load_index()
        
        # Find files with high salience
        salient = []
        for filepath, info in self.index["files"].items():
            salience = info.get("salience", 0)
            if salience >= min_salience:
                salient.append((filepath, salience, info.get("title", "Untitled")))
        
        # Sort by salience
        return sorted(salient, key=lambda x: x[1], reverse=True)
        
    def smart_query(self, query):
        """Smart query with context understanding"""
        query_lower = query.lower()
        
        # Handle special queries
        if "yesterday" in query_lower:
            yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
            yesterday_file = f"memory/daily/{yesterday}.md"
            if (WORKSPACE / yesterday_file).exists():
                return [(yesterday_file, 10.0)]
        
        if "today" in query_lower:
            today = datetime.now().strftime("%Y-%m-%d")
            today_file = f"memory/daily/{today}.md"
            if (WORKSPACE / today_file).exists():
                return [(today_file, 10.0)]
                
        if "project" in query_lower or "working on" in query_lower:
            results = self.search(query, limit=10)
            project_results = [(p, s) for p, s in results if "project" in p or "PROJECT" in p]
            return project_results[:5] if project_results else results[:5]
            
        # Default search
        return self.search(query, limit=5)
        
    def _extract_title(self, content):
        """Extract title from markdown (first # heading)"""
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        return match.group(1).strip() if match else "Untitled"
        
    def _extract_keywords(self, content):
        """Extract important keywords from content"""
        text = content.lower()
        text = re.sub(r'[#*_`\[\]\(\)|]', ' ', text)
        words = re.findall(r'\b[a-z]{3,}\b', text)
        
        stopwords = {'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'its', 'may', 'new', 'now', 'old', 'see', 'two', 'who', 'boy', 'did', 'she', 'use', 'her', 'way', 'many', 'oil', 'sit', 'set', 'run', 'eat', 'far', 'sea', 'eye', 'ago', 'off', 'too', 'any', 'say', 'man', 'try', 'ask', 'end', 'why', 'let', 'put', 'say', 'she', 'try', 'way', 'own', 'say', 'too', 'old'}
        
        word_freq = defaultdict(int)
        for word in words:
            if word not in stopwords and len(word) > 3:
                word_freq[word] += 1
                
        return [word for word, freq in word_freq.items() if freq >= 2][:50]
        
    def _extract_dates(self, content):
        """Extract dates mentioned in content"""
        dates = []
        dates.extend(re.findall(r'\d{4}-\d{2}-\d{2}', content))
        return dates
        
    def _save_index(self):
        """Save index to disk"""
        INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(INDEX_FILE, 'w') as f:
            json.dump(self.index, f, indent=2, default=str)
            
    def _load_index(self):
        """Load index from disk"""
        with open(INDEX_FILE, 'r') as f:
            self.index = json.load(f)

def main():
    parser = argparse.ArgumentParser(description='Memory Indexer - Local search that works')
    parser.add_argument('--build', action='store_true', help='Build the memory index')
    parser.add_argument('--search', type=str, help='Search for a query')
    parser.add_argument('--query', type=str, help='Smart query with context')
    parser.add_argument('--stats', action='store_true', help='Show index statistics')
    parser.add_argument('--salient', action='store_true', help='Show high-salience memories')
    parser.add_argument('--salience-min', type=int, default=5, help='Minimum salience filter')
    
    args = parser.parse_args()
    
    indexer = MemoryIndexer()
    
    if args.build:
        indexer.build_index()
        
    elif args.salient:
        results = indexer.get_salient_memories(min_salience=args.salience_min)
        print(f"\n🎯 High-Salience Memories (score >= {args.salience_min})")
        print("=" * 50)
        if results:
            for filepath, salience, title in results:
                print(f"  📌 [{salience}/10] {title}")
                print(f"     {filepath}")
                print()
        else:
            print("  No high-salience memories found")
            
    elif args.search:
        results = indexer.search(args.search)
        print(f"\n🔍 Search: '{args.search}'")
        print("=" * 50)
        if results:
            for filepath, score in results:
                info = indexer.index["files"].get(filepath, {})
                title = info.get("title", "Untitled")
                salience = info.get("salience", 0)
                print(f"  📄 {title[:50]}")
                print(f"     Path: {filepath}")
                print(f"     Score: {score:.1f} | Salience: {salience}/10")
                print()
        else:
            print("  No results found")
            
    elif args.query:
        results = indexer.smart_query(args.query)
        print(f"\n🧠 Query: '{args.query}'")
        print("=" * 50)
        if results:
            for filepath, score in results:
                info = indexer.index["files"].get(filepath, {})
                title = info.get("title", "Untitled")
                print(f"  📄 {title[:50]}")
                print(f"     Path: {filepath}")
                print()
        else:
            print("  No results found")
            
    elif args.stats:
        if INDEX_FILE.exists():
            indexer._load_index()
            stats = indexer.index.get("stats", {})
            print("📊 Memory Index Statistics")
            print("=" * 30)
            print(f"Files indexed: {stats.get('files_indexed', 0)}")
            print(f"Keywords: {stats.get('keywords_indexed', 0)}")
            print(f"Last build: {indexer.index.get('last_build', 'Unknown')}")
            
            # Show salience distribution
            salience_scores = [f.get("salience", 0) for f in indexer.index["files"].values()]
            if salience_scores:
                high_sal = sum(1 for s in salience_scores if s >= 5)
                print(f"High-salience memories: {high_sal}")
        else:
            print("❌ No index found. Run with --build first")
            
    else:
        parser.print_help()
        print("\n💡 Examples:")
        print("  python3 memory_index.py --build")
        print("  python3 memory_index.py --search 'domain flipping'")
        print("  python3 memory_index.py --salient          # Show important memories")
        print("  python3 memory_index.py --query 'What did we discuss yesterday?'")

if __name__ == "__main__":
    main()