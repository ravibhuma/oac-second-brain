---
name: oac-ingest
description: Ingest a new source (PDF, blog post, article, note) into the OAC Knowledge Graph wiki. Use when the user adds a file to raw/ and wants the wiki updated. Updates affected wiki pages, refreshes index, appends to log.md.
---

# OAC Ingest Skill

The user has added a new source file to the `raw/` folder of the OAC Knowledge Graph repo. Your job: integrate that source into the wiki using Karpathy's LLM Wiki pattern.

## Steps

### 1. Identify The New Source
Check these locations for new files:
- `raw/articles/` — blog posts, Medium articles, web clips
- `raw/pdfs/` — official Oracle docs, vendor whitepapers
- `raw/notes/` — user's own notes / source references

### 2. Read The Source Fully
- For markdown/txt: read the entire file
- For PDFs: read the corresponding `.txt` (created by `pdftotext`)
- If a PDF exists without a `.txt` companion, instruct the user to run:
  ```bash
  cd raw/pdfs && pdftotext -layout <new>.pdf <new>.txt
  ```

### 3. Map To Wiki Pages
Determine which existing `wiki/*.md` pages this source relates to:

| Source topic | Wiki pages to update |
|---|---|
| Architecture / Components | OAC Overview & Architecture |
| Connections / Data Sources | Data Sources & Connections |
| Semantic Modeling | Semantic Model, Subject Areas & Datasets |
| Visualizations | Workbooks & Visualizations, Maps & Geospatial |
| Dashboards | Classic Dashboards & Analyses |
| Reports | BI Publisher |
| ETL | Data Flows & Data Preparation |
| ML / AI | Machine Learning & AI Features, OAC AI Ecosystem |
| AI Agents | OAC AI Agents |
| MCP / External AI | OAC MCP Server |
| Security / Roles / RLS | Security & Row-Level Security |
| Admin / Snapshots / Scaling | Administration & Service Console |
| Logical SQL | Logical SQL Reference |
| REST APIs / Embedding | APIs, Embedding & Integration, OCI REST APIs & CLI for OAC |
| Custom Viz / Plug-ins | Custom Visualizations & Plug-ins |
| Mobile | Mobile (Oracle Analytics App) |
| KPIs / Alerts / Agents | KPIs, Alerts & Notifications |
| Migration / OBIEE | Migration, Snapshots & Lifecycle |

### 4. Update Wiki Pages
For each affected page:
- Add new facts/details to relevant sections
- Add new H2/H3 sections if the source introduces new sub-topics
- Cite the source: "(Source: raw/articles/new-blog.md)" or similar
- Maintain the existing structure (Summary, Body, Related)
- Preserve the **📖 Full Oracle Documentation:** line at the top

### 5. Add Cross-Links
If the new content reveals connections between pages, add `[wiki link](Other%20Page.md){ .wikilink }` entries to the **Related** section of relevant pages.

### 6. Update Index If New Topic
If the source introduces a topic that doesn't fit any existing wiki page, create a new `wiki/<New Topic>.md` page following the standard template:

```markdown
# <Page Title>

> **Last updated:** YYYY-MM-DD
> **Tags:** tag1, tag2

📖 **Full Oracle Documentation**: [Link to Oracle docs]

## Summary
One paragraph overview.

## Body
...sections...

## Related
- [Other Page](Other%20Page.md){ .wikilink }
```

Then add the new page to:
- `index.md` (under appropriate category)
- `mkdocs.yml` (under nav)
- `wiki/Docs Coverage Matrix.md`

### 7. Append To log.md
Add an entry to `log.md`:
```markdown
## YYYY-MM-DD — Ingested: <source filename>
- Source: raw/articles/<file>.md
- Topic: <one-line description>
- Affected wiki pages: <list>
- New cross-links added: <count>
```

### 8. Verify
- Run `python scripts/audit_links.py` to ensure cross-link counts went up
- Suggest user does `git add . && git commit -m "Ingest: <source>" && git push`

## Constraints

- NEVER fabricate facts — only synthesize from the actual source content
- Preserve existing wiki page structure (headers, Related sections, formatting)
- Maintain the trademark/disclaimer language (this is unofficial / community-built)
- For Oracle-sourced content, cite Oracle as the © holder

## Done Output

After ingestion, summarize for the user:
- How many wiki pages updated
- How many new cross-links added
- New page created (if any)
- Commit message suggestion
