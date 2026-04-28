# OAC Knowledge Graph — Operating Rules

## Purpose
This is a living, AI-maintained knowledge base for Oracle Analytics Cloud (OAC).
It covers features, architecture, administration, development, and best practices end-to-end.

## Folder Layout
```
raw/articles/   ← source articles/web clips (markdown, untouched)
raw/pdfs/       ← Oracle documentation PDFs
raw/notes/      ← freeform notes from the user
wiki/           ← synthesized, cross-linked wiki pages (agent-maintained)
index.md        ← content map of all wiki pages
log.md          ← ingestion and update history
```

## Agent Rules

### Ingest
When new content is added to `raw/`:
1. Read the source material fully.
2. Identify which existing wiki pages it affects — update them.
3. Create new wiki pages if a topic is not yet covered.
4. Update `index.md` if new pages were created.
5. Append an entry to `log.md`.

### Query
**Two-layer answer strategy:**
1. **Start with wiki pages** for structure and overview (`wiki/`)
2. **Deep-dive via Grep on raw text** when more detail is needed:
   ```
   raw/pdfs/*.txt — searchable full text of all official Oracle Analytics Cloud guides
   ```
3. **Cite both layers** in answers: `[[wiki page]]` + `(Source: <pdf-name>, page X)`

**Source PDFs available in raw/pdfs/ (and their .txt versions):**
- getting-started — orientation, editions, service mgmt
- whats-new — release notes, monthly updates
- building-semantic-models — Semantic Modeler full guide
- smml-schema-reference — SMML JSON schema reference
- connecting — data sources and connections
- visualizing-data-and-building-reports — workbooks, dashboards, BI Publisher (largest)
- administering — service admin, snapshots, security
- configuring — system configuration
- OAC_REST_API_Guide — REST API OpenAPI spec

**For any question, the canonical pattern:**
```
1. Grep raw/pdfs/*.txt with relevant keywords
2. Read matching sections (~50-100 lines context)
3. Read related wiki page for structure
4. Synthesize answer with both sources cited
```

### Lint
Periodically check for:
- Broken `[[wiki links]]`
- Contradictions between pages
- Orphan pages (not linked from anywhere)
- Stale content (flag with `> ⚠️ Review needed`)

## Wiki Page Format
Every page must have:
```markdown
# Page Title

> **Last updated:** YYYY-MM-DD
> **Tags:** tag1, tag2

## Summary
One paragraph overview.

## Body
...sections...

## Related
- [[Page Name]]
- [[Page Name]]
```

## Conventions
- Use `[[Page Name]]` for internal wiki links (Obsidian-style)
- Use `> 💡 Tip:` for best practices
- Use `> ⚠️ Warning:` for gotchas and common mistakes
- Code blocks use appropriate language tags: `sql`, `json`, `bash`, `xml`
- OAC-specific terms are always capitalized: Subject Area, Data Flow, Workbook, etc.
