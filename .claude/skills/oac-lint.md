---
name: oac-lint
description: Health-check the OAC Knowledge Graph wiki. Find broken links, contradictions, orphaned pages, stale claims, and gaps. Use periodically (monthly) or after major content changes.
---

# OAC Lint Skill

Periodic health check on the OAC Knowledge Graph wiki. Run this monthly or after major Oracle releases.

## Checks To Run

### 1. Broken Internal Links
Run the audit script and check for orphans:
```bash
python scripts/audit_links.py
```

Look for:
- Pages with TOTAL connections ≤ 4 (under-connected)
- Pages with 0 IN connections (orphaned destinations)
- Wiki links pointing to non-existent pages

For each broken link, suggest a fix:
- Update the link target if the page was renamed
- Remove the link if the target was intentionally deleted
- Create the missing page if it should exist

### 2. Broken External Links
Sample-check Oracle docs URLs (the **📖 Full Oracle Documentation:** lines at the top of each wiki page):
```bash
grep "https://docs.oracle.com" wiki/*.md
```

Note any 404s and update to current URLs.

### 3. Contradictions Across Pages
Look for places where two pages disagree on a fact. Common patterns:
- Different OAC URL formats in different pages
- Different OCPU sizing recommendations
- Different REST API endpoints / version numbers
- Different feature availability claims (Enterprise vs Professional)

If found, reconcile by checking the source PDF and updating the wrong page.

### 4. Stale Content
Check the "Last updated" dates and content freshness:
- AI Ecosystem pages — Oracle ships new features monthly; check Whats New
- BI Publisher — verify any version-specific claims still hold
- AI Agents — verify the 6000 char SI limit, 10 PDF / 5MB knowledge document limits
- REST API endpoints — verify versioning still says 20210901 or has bumped

For stale items, update OR add a `> ⚠️ Review needed` callout.

### 5. Source PDF Coverage
Run:
```bash
grep -l "Source:.*\.txt" wiki/*.md | wc -l
```

If many wiki pages don't cite source PDFs, that's a sign the wiki has drifted from its sources. Suggest re-ingesting key Oracle PDFs.

### 6. Orphan Source PDFs
Check if any PDFs in `raw/pdfs/` aren't referenced from `wiki/Source PDFs Index.md`. Add them.

### 7. Categorization Coverage
Verify every wiki page is assigned to a category in `scripts/build_graph.py` `CATEGORIES` dict. New pages added without categorization end up as "Other" gray nodes — uncategorized and visually disconnected.

```python
# scripts/build_graph.py — CATEGORIES dict
CATEGORIES = {
    "Architecture": [...],
    "Data Layer": [...],
    # ... etc
}
```

For new wiki pages, add them to the appropriate category.

### 8. Doc Reference Coverage
Verify every wiki page has the **📖 Full Oracle Documentation:** line at the top. Run:
```bash
grep -L "📖 \*\*Full Oracle Documentation\*\*" wiki/*.md
```

Any page that doesn't show — add doc reference using `scripts/add_doc_references.py` mapping.

## Output

Produce a report:

```markdown
# Lint Report — YYYY-MM-DD

## Issues Found
1. [HIGH] Broken link in <page>: [target] does not exist
2. [MED] Contradiction: <page-A> says X, <page-B> says Y
3. [LOW] Stale: <page> hasn't been updated since N months ago

## Recommendations
- [ ] Fix N broken links
- [ ] Reconcile N contradictions
- [ ] Update N stale pages
- [ ] Categorize N orphan pages

## Healthy Stats
- Total pages: N
- Total cross-references: N
- Average connections per page: N.N
- Pages with doc references: N/N
```

After fixing issues, suggest:
```bash
python scripts/audit_links.py     # verify connectivity improved
python scripts/build_graph.py     # regenerate graph
git add . && git commit -m "Lint: fixed N issues" && git push
```
