#!/usr/bin/env python3
"""Audit wiki cross-links: count connections per page, find under-connected pages."""
import re
import sys
from pathlib import Path
from collections import defaultdict

LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+\.md)(?:#[^)]*)?\)')

def main():
    wiki_dir = Path("wiki")
    md_files = sorted(wiki_dir.glob("*.md"))
    page_names = {f.stem for f in md_files}

    # Build adjacency
    outbound = defaultdict(set)  # page -> set of pages it links to
    inbound = defaultdict(set)   # page -> set of pages linking to it

    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        source = md_file.stem
        for match in LINK_RE.finditer(text):
            target_path = match.group(2)
            target = target_path.rsplit("/", 1)[-1].replace(".md", "")
            target = target.replace("%20", " ").replace("%26", "&").replace("%2C", ",").replace("%28", "(").replace("%29", ")")
            if target in page_names and target != source:
                outbound[source].add(target)
                inbound[target].add(source)

    # Total connections per page (union of in + out)
    all_pages = sorted(page_names)
    print(f"\n{'PAGE':<55} {'OUT':>4} {'IN':>4} {'TOTAL':>6}")
    print("-" * 75)

    rows = []
    for page in all_pages:
        connections = outbound[page] | inbound[page]
        rows.append((page, len(outbound[page]), len(inbound[page]), len(connections)))

    # Sort by total ascending (least connected first)
    rows.sort(key=lambda r: r[3])

    for name, out, inn, total in rows:
        print(f"{name:<55} {out:>4} {inn:>4} {total:>6}")

    print(f"\nTotal pages: {len(all_pages)}")

if __name__ == "__main__":
    main()
