#!/usr/bin/env python3
"""
Fix common markdown rendering issues:
  1. Lists/tables that need a blank line before them
  2. Code fences that need blank lines before/after

Run on a single file: python scripts/fix_markdown_lists.py path/to/file.md
Run on all wiki: python scripts/fix_markdown_lists.py --wiki
"""
import re
import sys
from pathlib import Path

def needs_blank_before(prev: str, curr: str) -> bool:
    """Return True if curr line starts a list/table that needs a blank line before it."""
    if not prev.strip():
        return False  # already blank
    p = prev.lstrip()
    c = curr.lstrip()
    # If prev is itself a list item or table or header or quote, no break needed
    if p.startswith(("-", "*", "+", "|", "#", ">", "```")) or re.match(r"^\d+\.", p):
        return False
    # If curr is a bullet, ordered list, or table row → needs blank
    if c.startswith(("- ", "* ", "+ ", "| ")) or re.match(r"^\d+\. ", c):
        return True
    return False

def fix_file(path: Path) -> int:
    """Insert blank lines where needed. Return number of fixes."""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    out = []
    fixes = 0
    for i, line in enumerate(lines):
        prev = lines[i - 1] if i > 0 else ""
        if needs_blank_before(prev, line):
            out.append("")
            fixes += 1
        out.append(line)
    if fixes:
        path.write_text("\n".join(out), encoding="utf-8")
    return fixes

def main():
    if len(sys.argv) < 2:
        print("Usage: fix_markdown_lists.py <file.md> | --wiki | --all")
        sys.exit(1)

    arg = sys.argv[1]
    if arg == "--wiki":
        files = list(Path("wiki").glob("*.md"))
    elif arg == "--all":
        files = list(Path("wiki").glob("*.md")) + [
            Path(f) for f in [
                "README.md", "AI_ASSISTANTS.md", "AI_SKILLS.md",
                "CLAUDE_CODE_SETUP.md", "CODEX_SETUP.md", "SETUP.md",
                "PROJECT_INSTRUCTIONS.md", "AGENTS.md", "AUTHORS.md",
                "index.md", "log.md"
            ] if Path(f).exists()
        ]
    else:
        files = [Path(arg)]

    total = 0
    for f in files:
        if not f.exists():
            print(f"Skip (not found): {f}")
            continue
        n = fix_file(f)
        if n:
            print(f"  [fixed {n}] {f}")
            total += n
        else:
            print(f"  [clean] {f}")

    print(f"\nTotal fixes: {total} across {len(files)} files")

if __name__ == "__main__":
    main()
