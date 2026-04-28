# Agent Instructions — OAC Knowledge Graph

> This file is read by **OpenAI Codex CLI** (`AGENTS.md`), **Cursor**, **Cline**, and other agentic IDE/CLI tools that look for project-level agent instructions.

## What This Repo Is

This is the **OAC Knowledge Graph** — an open-source knowledge base for Oracle Analytics Cloud (OAC), built using Andrej Karpathy's LLM Wiki pattern.

- **30 cross-linked wiki pages** in `wiki/` covering every OAC topic
- **9 official Oracle PDFs** in `raw/pdfs/` (with `.txt` versions for grep)
- **Curated source articles** in `raw/articles/` and `raw/notes/`
- Every wiki page has a **📖 Full Oracle Documentation** link at the top citing the canonical Oracle source

⚠️ **Unofficial / community-built.** Not affiliated with Oracle Corporation. Created by [Ravi Bhuma](https://github.com/ravibhuma).

## How To Answer OAC Questions

When the user asks any question about Oracle Analytics Cloud, follow this two-layer strategy:

### Layer 1 — Wiki Pages (Structure & Synthesis)
1. Check `wiki/` for relevant pages first
2. Read matching pages — they contain organized synthesis with cross-links
3. Topics covered: Architecture, Editions, Provisioning, Connections, Semantic Model, Subject Areas, Datasets, Workbooks, Maps, Dashboards, BI Publisher, Data Flows, Machine Learning, AI Ecosystem, AI Agents (R.T.C.C.O.E framework), MCP Server, Security & RLS, Administration, Logical SQL, APIs, OCI APIs/CLI, Custom Visualizations, Mobile, KPIs, Migration, FAQs, OAC vs OBIEE/OAS

### Layer 2 — Source PDFs (Deep Reference)
1. `grep` `raw/pdfs/*.txt` for specific keywords from the question
2. Read matching sections (~50 lines context)
3. PDF text files available:
   - `getting-started-oracle-analytics-cloud.txt`
   - `whats-new-oracle-analytics-cloud.txt`
   - `building-semantic-models-oracle-analytics-cloud.txt`
   - `smml-schema-reference-oracle-analytics-cloud.txt`
   - `connecting-oracle-analytics-cloud-your-data.txt`
   - `visualizing-data-and-building-reports-oracle-analytics-cloud.txt` (largest)
   - `administering-oracle-analytics-cloud-oracle-cloud-infrastructure-gen-2.txt`
   - `configuring-oracle-analytics-cloud.txt`
   - `OAC_REST_API_Guide.txt`

### Citation Format
Every answer must cite both layers when applicable:

```
[Answer body with markdown formatting]

**Sources:**
- Wiki: wiki/<Page Name>.md
- Oracle docs: <pdf-filename>, near "<keyword phrase>"
- External: https://docs.oracle.com/en/cloud/paas/analytics-cloud/<book>/
```

## How To Add New Content (Ingest Operation)

When the user drops a new file into `raw/` and asks to "ingest" it:

1. Read the new source fully
2. Identify which `wiki/` pages it affects
3. Update those pages with the new facts
4. Add cross-links between pages where the source reveals connections
5. If the source introduces a new topic, create `wiki/<New Topic>.md`
6. Append to `log.md` with date and summary
7. Run `python scripts/audit_links.py` to verify connectivity
8. Suggest commit + push

## Style Guide

- **Use markdown formatting** — tables, code blocks, headers
- **Use exact UI labels** — "Service Console → Security Console → Test User"
- **Show working code** — Logical SQL with proper double-quote escaping
- **For procedures** — numbered steps with exact UI paths
- **For comparisons** — side-by-side tables
- **Cite sources** — point to wiki pages AND source PDFs
- **Honest about gaps** — if the wiki doesn't cover something, say so

## Constraints

- **NEVER fabricate** UI labels, REST endpoints, column names, or feature names
- For security topics, ALWAYS mention RLS implications
- Maintain the **unofficial / community-built** disclaimer when describing the project
- Respect Oracle's trademarks — don't claim affiliation or endorsement

## Build & Validate

After making changes:

```bash
# Validate wiki link health
python scripts/audit_links.py

# Regenerate the interactive graph (preview only — workflow does this on push)
python scripts/build_graph.py docs-test
rm -rf docs-test

# Commit + push (CI rebuilds the GitHub Pages site)
git add . && git commit -m "Description" && git push
```

## Companion Resources

- **R.T.C.C.O.E framework** for OAC AI Agents: `wiki/OAC AI Agents.md` and https://medium.com/@ravishankerb/building-effective-oac-ai-agents...
- **OAC Prompt Studio**: https://ravi-bhuma.github.io/oac-prompt-studio/
- **Karpathy's LLM Wiki gist**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## When You Don't Know

If a question is outside this knowledge base:

- Say so explicitly
- Point to the relevant Oracle docs URL: `https://docs.oracle.com/en/cloud/paas/analytics-cloud/`
- Suggest searching: Oracle Analytics Blog, YouTube, Community forums
