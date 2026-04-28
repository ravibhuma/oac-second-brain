#!/usr/bin/env python3
"""
Preprocess [[wiki links]] in markdown files into proper relative links.

[[Page Name]]            -> [Page Name](Page%20Name.md)
[[Page Name|Display]]    -> [Display](Page%20Name.md)

Run before mkdocs build. Operates on docs/ folder created by the workflow.
"""
import os
import re
import sys
import urllib.parse
from pathlib import Path

WIKILINK_RE = re.compile(r'\[\[([^\]|]+?)(?:\|([^\]]+?))?\]\]')

def find_target(target_name: str, docs_root: Path) -> str | None:
    """Find the actual file path for a wiki link target."""
    # Try wiki/ first, then root
    candidates = [
        docs_root / "wiki" / f"{target_name}.md",
        docs_root / f"{target_name}.md",
    ]
    for c in candidates:
        if c.exists():
            return c.relative_to(docs_root).as_posix()
    return None

def replace_in_file(md_file: Path, docs_root: Path) -> int:
    """Replace [[wiki links]] in one file. Returns number of replacements."""
    text = md_file.read_text(encoding="utf-8")
    file_dir = md_file.parent

    def replace(match):
        target = match.group(1).strip()
        display = match.group(2).strip() if match.group(2) else target
        target_path = find_target(target, docs_root)
        if not target_path:
            # Unresolved — leave as plain text
            return display
        # Compute relative path from current file
        target_abs = (docs_root / target_path).resolve()
        rel = os.path.relpath(target_abs, file_dir.resolve()).replace("\\", "/")
        # URL-encode spaces
        rel_encoded = urllib.parse.quote(rel, safe="/.#")
        return f'[{display}]({rel_encoded}){{ .wikilink }}'

    new_text, n = WIKILINK_RE.subn(replace, text)
    if n:
        md_file.write_text(new_text, encoding="utf-8")
    return n

def main():
    if len(sys.argv) < 2:
        print("Usage: preprocess_wikilinks.py <docs_dir>", file=sys.stderr)
        sys.exit(1)

    docs_root = Path(sys.argv[1]).resolve()
    if not docs_root.is_dir():
        print(f"Not a directory: {docs_root}", file=sys.stderr)
        sys.exit(1)

    total = 0
    files = 0
    for md_file in docs_root.rglob("*.md"):
        n = replace_in_file(md_file, docs_root)
        if n:
            files += 1
            total += n
            print(f"  {md_file.relative_to(docs_root)}: {n} link(s)")

    print(f"\n✓ Replaced {total} wiki links across {files} files")

if __name__ == "__main__":
    main()
