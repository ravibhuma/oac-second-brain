# OAC Knowledge Graph

> **An open-source community knowledge base for Oracle Analytics Cloud — built without RAG, vector databases, or embeddings. Just markdown, grep, and the LLM you already use.**

[![License: MIT](https://img.shields.io/badge/License-MIT-2D7D55.svg)](https://opensource.org/licenses/MIT)
[![Site Status](https://img.shields.io/badge/docs-live-00A36C)](https://ravibhuma.github.io/oac-knowledge-graph/)
[![Topic: Oracle Analytics Cloud](https://img.shields.io/badge/topic-Oracle%20Analytics%20Cloud-C74634)](https://www.oracle.com/business-analytics/analytics-cloud/)
[![No Vector DB](https://img.shields.io/badge/no-vector%20database-2D7D55)](#-why-no-rag-or-vector-db)
[![Pattern: LLM Wiki by A. Karpathy](https://img.shields.io/badge/pattern-LLM%20Wiki%20by%20A.%20Karpathy-1F5A3D)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

> ⚠️ **Unofficial / Community-Built.** Not affiliated with, sponsored by, or endorsed by Oracle Corporation. "Oracle", "Oracle Analytics Cloud", and related marks are trademarks of Oracle and/or its affiliates. This project is an independent community resource that synthesizes publicly available Oracle documentation, blogs, and tutorials for educational use.

---

## 🌟 What This Is

A **comprehensive, AI-queryable knowledge base** for Oracle Analytics Cloud. The same content serves three different audiences from one source-of-truth:

| Audience | What They Get |
|---|---|
| 🌐 **Browsers** | A clean, searchable docs site at [ravibhuma.github.io/oac-knowledge-graph](https://ravibhuma.github.io/oac-knowledge-graph/) |
| 🕸️ **Visual learners** | An [interactive force-directed graph](https://ravibhuma.github.io/oac-knowledge-graph/graph/) of how 30 OAC topics connect |
| 🤖 **Power users** | Clone the repo, ask any AI tool (Claude, ChatGPT, Gemini, Codex, ...) — get answers with cited sources |

**By the numbers:**
- **30** cross-linked wiki pages
- **158** logical cross-references between topics
- **9** official Oracle PDFs (~6.8 MB searchable text) as deep reference
- **80+** OAC data source types documented
- **12** AI tool integration guides (Claude Code, Codex, ChatGPT, Gemini, Cursor, Cline, Ollama, OAC AI Agent, ...)
- Every wiki page **hyperlinks to the canonical Oracle documentation** for citation
- **0** vector databases. **0** embedding pipelines.

---

## ⚡ Try It In 60 Seconds

### Option A — Browse Online (No Install)

Visit **[https://ravibhuma.github.io/oac-knowledge-graph/](https://ravibhuma.github.io/oac-knowledge-graph/)** — works on any device.

### Option B — Open The Knowledge Graph

**[https://ravibhuma.github.io/oac-knowledge-graph/graph/](https://ravibhuma.github.io/oac-knowledge-graph/graph/)** — see all 30 topics as a network. Hover, click, search.

### Option C — Clone + Ask Any AI

```bash
git clone https://github.com/ravibhuma/oac-knowledge-graph.git
cd oac-knowledge-graph

# Install Claude Code (or use Codex, ChatGPT, Gemini, etc.)
npm install -g @anthropic-ai/claude-code

# Ask anything
claude
> How do I configure row-level security in OAC?
> Walk me through the three-layer Semantic Model architecture
> What's the R.T.C.C.O.E framework for AI Agents?
```

That's it. **No vector database. No chunking pipeline. No embedding model. Just markdown + an LLM.**

---

## 🕸️ See The Knowledge As A Graph

**[👉 Open the Interactive Knowledge Graph](https://ravibhuma.github.io/oac-knowledge-graph/graph/)**

What you'll see:
- **30 colored nodes** — one per wiki page
- **158 lines** — cross-references between topics
- **Color-coded by category** — Architecture (dark green), AI Ecosystem (Oracle red), Security (slate), etc.
- **Hover** any node → connections light up, others fade
- **Click** → info panel with category, connection count, and clickable list of related pages
- **Double-click** → opens the actual wiki page
- **Search** → highlights and zooms to matching topics

The category coloring shows the **mental model** of OAC at a glance:
| Color | Category | Pages |
|---|---|---|
| 🟢 Dark green | Architecture | OAC Overview, OAC vs OBIEE, Subscribe & Provisioning, What's New |
| 🟢 Mid green | Data Layer | Data Sources & Connections, Semantic Model, Subject Areas & Datasets |
| 🟢 Bright green | Analytics | Workbooks, Maps, Classic Dashboards, BI Publisher |
| 🟢 Light green | Data Engineering | Data Flows, Machine Learning |
| 🔴 **Oracle red** | **AI Ecosystem** | AI Ecosystem, AI Agents, MCP Server *(intentional pop)* |
| ⚪ Slate | Security & Admin | Security & RLS, Administration |
| 🟢 Forest green | Developer | Logical SQL, APIs, OCI APIs/CLI, Custom Visualizations |
| 🟢 Mint | End User | Consumer Guide, Mobile |
| 🟢 Sage | Operations | KPIs, Migration, FAQs |
| ⚪ Gray | Reference | Coverage Matrix, Tutorials, Source PDFs |

---

## 🧠 How The Nodes Are Related

Connections aren't random. Each line in the graph is an actual `[wiki link](OtherPage.md)` in the markdown source — written deliberately to express a real conceptual relationship.

**Functional dependencies** — *"X uses Y"*
- AI Agents → Subject Areas & Datasets *(an Agent is bound to a dataset)*
- AI Agents → Security & RLS *(agent filters use session variables)*
- BI Publisher → Logical SQL *(Publisher data models query Subject Areas via LSQL)*

**Comparison / alternative** — *"X vs Y"*
- Subject Areas ↔ Datasets *(governed vs self-service)*
- Workbooks ↔ Classic Dashboards *(modern vs legacy)*

**Architectural composition** — *"X contains Y"*
- Semantic Model → Physical / BMM / Presentation layers
- AI Ecosystem → AI Assistant + AI Agents + MCP Server (5 layers)

**Cross-cutting concerns** — *"Y applies to X"*
- Security & RLS connects to half the wiki *(governance touches everything)*
- Administration → Snapshots, Migration, Mail Server, Connections
- Mobile → Workbooks, Dashboards, KPIs *(mobile is a different surface for same content)*

The most-connected hub topics:
1. **Docs Coverage Matrix** (28 connections — catalogs everything)
2. **Administration & Service Console** (18 — touches all operations)
3. **Source PDFs Index** (15 — every page traces back)
4. **Security & RLS** (15 — cross-cutting governance)
5. **Workbooks & Visualizations** (14 — primary user surface)

---

## 🤖 Use With Any AI Tool

The cloned repo works with **every major AI assistant**:

| Tool | Quick Setup | Cost |
|---|---|---|
| **[Claude Code](CLAUDE_CODE_SETUP.md)** | `npm install -g @anthropic-ai/claude-code` → `claude` | Free tier |
| **[OpenAI Codex](CODEX_SETUP.md)** | `npm install -g @openai/codex` → `codex` | Free tier / $20 |
| **[Google Gemini](https://gemini.google.com)** | Upload all 9 PDFs (accepts up to 100MB) | **Free** |
| **[ChatGPT](https://chatgpt.com)** | Upload PDFs or build a Custom GPT | Free / $20 |
| **[Cursor](https://cursor.com)** / **[Cline](https://github.com/cline/cline)** | Open repo as workspace, ask `@workspace ...` | Free / $20 |
| **[Ollama](https://ollama.ai)** + AnythingLLM | Local, private, offline | Free |
| **OAC AI Agent** | Bundle wiki into PDFs, build inside OAC | Already in OAC |

**👉 Full guide for all 12 tools: [AI_ASSISTANTS.md](AI_ASSISTANTS.md)**

---

## 📓 Browse In Obsidian (Best Local Experience)

Install **[Obsidian](https://obsidian.md)** (free) for the most polished local browsing experience:

```
1. git clone https://github.com/ravibhuma/oac-knowledge-graph.git
2. Open Obsidian → "Open folder as vault" → select the cloned folder
3. Press Ctrl+G → see the same knowledge graph natively in Obsidian
```

You get:
- **Sidebar** — file tree of all 30 pages
- **Live preview** — markdown renders beautifully
- **Backlinks panel** — see what links to each page
- **Tag search** — filter by tag (RLS, AI, Semantic Model, etc.)
- **Native graph view** (Ctrl+G) — Obsidian's signature force-directed graph
- **Offline access** — works without internet

This is the recommended workflow for daily reference — clone, open in Obsidian, search, click, navigate connections.

---

## 🔧 How It's Built

```
oac-knowledge-graph/
├── wiki/                          ← 30 cross-linked .md pages (the brain)
│   ├── OAC Overview & Architecture.md
│   ├── Semantic Model.md
│   ├── Logical SQL Reference.md
│   ├── OAC AI Agents.md          ← R.T.C.C.O.E framework
│   ├── OAC MCP Server.md
│   ├── Security & Row-Level Security.md
│   ├── Data Sources & Connections.md   ← 80+ data source types
│   └── … (23 more)
├── raw/
│   ├── pdfs/                      ← 9 official Oracle PDFs + searchable .txt
│   ├── articles/                  ← Curated blog posts, Medium articles
│   └── notes/                     ← Source references
├── scripts/
│   ├── build_graph.py             ← generates interactive vis.js graph
│   ├── preprocess_wikilinks.py    ← converts [[wiki links]] for site
│   ├── audit_links.py             ← finds under-connected pages
│   └── add_doc_references.py      ← Oracle docs hyperlinks per page
├── stylesheets/extra.css          ← OAC green theme (light + dark mode)
├── assets/
│   ├── favicon.svg                ← OAC green graph icon
│   └── vendor/vis-network.min.js  ← bundled locally (no CDN dependency)
├── .github/workflows/
│   └── deploy-pages.yml           ← auto-build on every push
├── CLAUDE.md                      ← Operating rules for the AI maintainer
└── README.md                      ← This file
```

**Build pipeline (runs on every git push):**
1. **Preprocessor** converts `[[wiki links]]` to standard markdown
2. **Graph builder** scans wiki/, generates `docs/graph/index.html` with vis.js
3. **MkDocs Material** builds the docs site with OAC green theme
4. **GitHub Pages** deploys at https://ravibhuma.github.io/oac-knowledge-graph/

Whenever you `git push`:
- Wiki page edits → site rebuilds in ~3 minutes
- New wiki pages → graph regenerates with new nodes
- New `[wiki link](X.md)` references → new edges in the graph
- Auto-sync, zero manual steps

---

## 📚 Adding Your Own Documentation

Karpathy's pattern shines beyond just Q&A — the wiki **compounds** as you add sources:

```
You drop a new source             →   raw/articles/new-blog.md
        ↓ ask Claude to "ingest"
LLM updates affected wiki pages   →   wiki/relevant-page.md
        ↓ git push
Site rebuilds, graph regenerates  →   docs site + interactive graph
        ↓ next user benefits
Knowledge compounds
```

Three operations:

### Operation 1 — Ingest (Add New Source)
```bash
# Drop new content
cp my-oac-notes.md raw/notes/
# Or for PDFs:
cp new-oracle-guide.pdf raw/pdfs/
cd raw/pdfs && pdftotext -layout new-oracle-guide.pdf new-oracle-guide.txt

# Open Claude Code in the repo
claude
> Ingest the new file in raw/notes/. Update affected wiki pages.
```

### Operation 2 — Query (Ask Anything)
```bash
claude
> What's the right RLS approach when the data source is Snowflake?
```

### Operation 3 — Lint (Health Check)
```bash
claude
> Lint the wiki. Find broken links, contradictions, orphan pages, stale claims.
```

---

## 🚀 Apply To YOUR Domain

The OAC Knowledge Graph is a **template**. Fork it, swap the content, and you have an instant knowledge base for any domain.

```bash
# 1. Fork the repo on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/oac-knowledge-graph.git
cd oac-knowledge-graph

# 3. Empty the content folders
rm wiki/*.md raw/articles/*.md raw/pdfs/*.pdf raw/pdfs/*.txt

# 4. Drop in your sources
cp /path/to/your-docs/*.pdf raw/pdfs/
cd raw/pdfs && for f in *.pdf; do pdftotext -layout "$f" "${f%.pdf}.txt"; done

# 5. Update CLAUDE.md with YOUR domain context

# 6. Build wiki pages from sources
claude
> Read all files in raw/. Create wiki pages organized by topic.
> Each page: summary, sections, related links, doc references.

# 7. Customize the brand color in stylesheets/extra.css

# 8. Push to your repo and enable GitHub Pages → GitHub Actions
git add . && git commit -m "Initial knowledge base" && git push
```

The interactive graph regenerates automatically from your wiki content. Done.

---

## 🎯 Why No RAG Or Vector DB?

Most "AI Q&A over docs" projects in 2025 use **RAG** (Retrieval-Augmented Generation):
- Chunk documents into 500-token pieces
- Compute vector embeddings
- Store in a vector database
- At query time: vectorize the question, retrieve nearest chunks, send to LLM

For focused-domain knowledge bases under ~10MB, **this is overkill**.

```
                  ┌──────────────────────────────────┐
                  │  Modern LLM (200K-2M context)     │
                  └─────────────▲────────────────────┘
                                │
                    Whole files + grep results
                                │
   ┌────────────────────────────┴─────────────────────────────┐
   │                                                            │
   │     wiki/ (cross-linked .md)        raw/pdfs/*.txt          │
   │     - Karpathy-style synthesis      - Authoritative source │
   │     - Manual semantic cross-refs    - Grep at query time   │
   │     - Folder = semantic grouping    - Cite exact lines     │
   │                                                            │
   └────────────────────────────────────────────────────────────┘
```

**No vectors. No embedding model. No vector DB. No re-ranker.**

### RAG vs LLM Wiki — Side By Side

| Aspect | Traditional RAG | LLM Wiki Pattern |
|---|---|---|
| **Storage** | Vector database | Plain markdown in Git |
| **Indexing pipeline** | Chunk → embed → upsert | None — `git pull` |
| **Retrieval** | Cosine similarity | `grep` + folder + wiki links |
| **Chunking** | Required, lossy | None |
| **Citation precision** | Chunk-level (fuzzy) | File + line (exact) |
| **Cost (running)** | DB + embedding + LLM | LLM only |
| **Setup time** | Hours-days | Minutes |
| **Update latency** | Re-embed pipeline | Immediate |
| **Best for** | Millions of documents | Focused domain |

**LLM Wiki wins when** the knowledge fits in ~5-10MB and you have a modern LLM (Claude, GPT-4, Gemini all qualify).

For Oracle Analytics Cloud (~7MB of canonical docs), **LLM Wiki wins on every dimension**.

---

## 💡 Sample Questions To Try

```
"How do I configure row-level security in OAC?"
"Walk me through the three-layer Semantic Model"
"What's the R.T.C.C.O.E framework for AI Agents?"
"Compare OAC vs OBIEE migration paths"
"Show me Logical SQL syntax for time-series functions"
"What's the difference between Subject Areas and Datasets?"
"How does the OAC MCP Server work with Claude Desktop?"
"Walk me through provisioning an OAC instance on OCI"
"Explain BI Publisher bursting with a sales use case"
"List every option for connecting to private/on-prem databases"
```

---

## 📚 Topics Covered

**Platform & Architecture** · OAC Overview · OAC vs OBIEE vs OAS · Subscribe & Provisioning · What's New
**Data Layer** · Data Sources & Connections (80+ types) · Semantic Model · Subject Areas & Datasets
**Analytics & Reporting** · Workbooks & Visualizations · Maps & Geospatial · Classic Dashboards · BI Publisher
**Data Engineering** · Data Flows & Preparation · Machine Learning & AI Features
**AI Ecosystem** · OAC AI Ecosystem · OAC AI Agents (R.T.C.C.O.E) · OAC MCP Server
**Governance & Security** · Security & RLS · Administration & Service Console
**Developer Reference** · Logical SQL · APIs & Embedding · OCI REST APIs & CLI · Custom Visualizations
**End User** · Consumer Guide · Mobile App
**Operations** · KPIs & Alerts · Migration & Lifecycle · FAQs & Troubleshooting

📋 [Full topic index](topics.md) · 📊 [Coverage matrix vs Oracle docs](wiki/Docs%20Coverage%20Matrix.md) · 📖 [Source PDFs Index](wiki/Source%20PDFs%20Index.md)

Every page links to the corresponding **canonical Oracle documentation** at the top — proper citation chain for every claim.

---

## 🤝 Contributing

Found a gap, error, or want to add a source? Welcome.

1. Fork the repo
2. Drop new article/PDF into `raw/articles/` or `raw/pdfs/`
3. Open Claude Code: *"Ingest the new source"*
4. Claude updates wiki pages + index + log
5. Submit a PR

Or just [open an issue](https://github.com/ravibhuma/oac-knowledge-graph/issues) describing what's missing.

---

## 🙏 Acknowledgments

### The LLM Wiki Pattern — Andrej Karpathy
This project is a direct application of **Andrej Karpathy's LLM Wiki pattern**, originally published as a public gist:

📘 **Original gist**: [karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

Karpathy's core insight — *"the wiki is a persistent, compounding artifact; the cross-references are already there"* — guides every architectural decision in this repo:

- **`raw/`** = curated immutable sources
- **`wiki/`** = LLM-maintained synthesis layer
- **`CLAUDE.md`** = operating rules for the agent
- **Three operations: Ingest, Query, Lint**
- **Human curates, LLM does everything else**

This repo demonstrates the pattern applied to enterprise documentation. **All credit for the pattern itself goes to Andrej Karpathy.** He is not affiliated with this project.

### Source Materials
Knowledge content synthesized from publicly available materials:
- [Oracle Analytics Cloud Documentation](https://docs.oracle.com/en/cloud/paas/analytics-cloud/) © Oracle Corporation
- [Oracle Analytics Blog](https://blogs.oracle.com/analytics/) © Oracle Corporation
- [Oracle Analytics YouTube](https://www.youtube.com/c/OracleAnalytics) © Oracle Corporation

Oracle documentation is included as searchable PDFs for **fair-use review and educational reference**. All Oracle copyrights, trademarks, and brand assets remain property of Oracle Corporation.

---

## 📜 License & Trademark Notices

**Code & synthesized wiki content**: MIT License — see [LICENSE](LICENSE).

**Oracle documentation in `raw/pdfs/`**: © Oracle Corporation. Used for fair-use review/educational purposes.

**Trademarks**:
- "Oracle", "Oracle Analytics Cloud", "OBIEE", "OAS", and related product names are trademarks of Oracle Corporation
- "Claude" and "Claude Code" are trademarks of Anthropic
- "ChatGPT" and "OpenAI" are trademarks of OpenAI
- "Gemini" is a trademark of Google LLC
- "Obsidian" is a trademark of Dynalist, Inc.
- All other trademarks are property of their respective owners

This project is **not affiliated with, sponsored by, or endorsed by Oracle, Anthropic, OpenAI, Google, or any other entity** mentioned. It is an independent community resource.

---

## 👤 Author

Maintained by **[@ravibhuma](https://github.com/ravibhuma)** ([Medium](https://medium.com/@ravishankerb)).

Companion projects:
- [OAC Prompt Studio](https://ravi-bhuma.github.io/oac-prompt-studio/) — Open-source learning platform for OAC AI Agents (R.T.C.C.O.E framework)
- [Building Effective OAC AI Agents](https://medium.com/@ravishankerb/building-effective-oac-ai-agents-the-framework-the-techniques-and-the-resource-hub-to-get-you-eba3797ca991) — Medium article

⭐ **[Star this repo](https://github.com/ravibhuma/oac-knowledge-graph)** — it helps others discover the LLM Wiki pattern by Andrej Karpathy.
