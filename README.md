# OAC Second Brain

> **A comprehensive, AI-maintained knowledge base for Oracle Analytics Cloud — covering every feature, component, and topic end-to-end.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Pages](https://img.shields.io/badge/docs-live-blue)](https://ravibhuma.github.io/oac-second-brain/)
[![Built with Material for MkDocs](https://img.shields.io/badge/built%20with-MkDocs%20Material-526CFE)](https://squidfunk.github.io/mkdocs-material/)

---

## 🔍 How To Use This Site

| What You Want To Do | How |
|---|---|
| **🔍 Search anything** | Click the **magnifying glass** icon at the top right — searches all 30+ pages instantly |
| **📚 Browse by topic** | Use the left sidebar — topics are grouped by area (Architecture, Data Layer, AI, etc.) |
| **🧭 See full topic map** | Visit [All Topics](topics.md) for a category overview |
| **📊 Check coverage** | [Coverage Matrix](wiki/Docs Coverage Matrix.md) maps every Oracle docs guide to wiki pages |
| **🌙 Dark mode** | Click the **sun/moon icon** at the top right |

---

## 💡 Quick Examples — What This Knowledge Base Answers

> **Architecture**
> *"What's the difference between OAC, OAS, and OBIEE?"*
> *"How do I size OCPUs for my OAC instance?"*

> **Data Modeling**
> *"Walk me through the three-layer Semantic Model architecture"*
> *"How do session variables work for row-level security?"*

> **AI & Agents**
> *"What's the R.T.C.C.O.E framework for building OAC AI Agents?"*
> *"How does the OAC MCP Server integrate with Claude Desktop?"*

> **Development**
> *"Give me the full Logical SQL function reference"*
> *"How do I embed a workbook in a custom web app?"*

Use the **search bar** to ask any of these — it'll surface the relevant pages.

---

## 🧠 What's Inside

- **30+ cross-linked wiki pages** covering every Oracle Analytics Cloud topic
- **9 official Oracle PDF guides** (~6.8 MB searchable text) as deep reference
- **Source articles** from Oracle blogs, Medium, YouTube
- **Coverage matrix** mapping every Oracle docs guide to wiki pages

### Topics Covered

**Platform & Architecture** · OAC Overview · OAC vs OBIEE vs OAS · Subscribe & Provisioning · What's New
**Data Layer** · Data Sources & Connections · Semantic Model · Subject Areas & Datasets
**Analytics & Reporting** · Workbooks & Visualizations · Maps & Geospatial · Classic Dashboards · BI Publisher
**Data Engineering** · Data Flows & Preparation · Machine Learning & AI Features
**AI Ecosystem** · OAC AI Ecosystem · OAC AI Agents · OAC MCP Server
**Governance & Security** · Security & RLS · Administration & Service Console
**Developer Reference** · Logical SQL · APIs & Embedding · OCI REST APIs & CLI · Custom Visualizations
**End User** · Consumer Guide · Mobile App
**Operations** · KPIs & Alerts · Migration & Lifecycle · FAQs & Troubleshooting

---

## 🚀 Two Steps To Get Started

### Step 1 — Download The Knowledge Base
```bash
git clone https://github.com/ravibhuma/oac-second-brain.git
cd oac-second-brain
```

Or just visit the [browsable site](https://ravibhuma.github.io/oac-second-brain/) — no install needed.

### Step 2 — Set Up Claude Code (Recommended)

**👉 Follow the complete guide: [CLAUDE_CODE_SETUP.md](CLAUDE_CODE_SETUP.md)**

Quick version:
```bash
# 1. Install Claude Code (needs Node.js 18+)
npm install -g @anthropic-ai/claude-code

# 2. From inside the cloned repo folder
claude

# 3. Sign in when prompted, then ask anything:
> How do I configure row-level security in OAC?
```

Claude reads the entire knowledge base and answers with citations. **Free tier covers most casual use.**

### Alternative AI Tools

If you prefer a different tool, all of these work — drop the wiki/ folder + selected PDFs into:

| Tool | Cost | Best For |
|---|---|---|
| **[Claude Desktop](https://claude.ai)** | Free tier | Visual UI, no terminal |
| **[ChatGPT](https://chat.openai.com)** | Free / Plus | Familiar interface |
| **[Google Gemini](https://gemini.google.com)** | **Free** (huge files) | All 9 PDFs at once |
| **[Ollama](https://ollama.ai) + AnythingLLM** | Free, offline | Private/sensitive data |
| **OAC AI Agent** | Already have OAC | Production OAC users |

### Example Questions To Try

```
"How do I configure row-level security in OAC?"
"Walk me through the three-layer Semantic Model architecture"
"What's the R.T.C.C.O.E framework for AI Agents?"
"Compare OAC vs OBIEE migration paths"
"Show me the Logical SQL syntax for time-series functions"
```

### For Browsing (No AI)

Open the cloned folder in **[Obsidian](https://obsidian.md)** as a vault to:
- See the full graph of `[[wiki links]]`
- Browse with the file tree
- Search keywords across all pages
- Read with rendered markdown, images, tables

---

## 🏗️ How It Works — The Karpathy LLM Wiki Pattern

Built on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — synthesize knowledge once, compound forever.

```
SOURCES (curated)        →   raw/         (PDFs, articles, notes)
        ↓ ingest
WIKI (LLM-maintained)    →   wiki/        (cross-linked pages)
        ↓ query
ANSWERS                       cited from wiki + raw sources
```

**Three operations:**
- **Ingest** — Add sources, LLM updates wiki pages
- **Query** — Ask questions, LLM answers with citations
- **Lint** — LLM checks for broken links, contradictions, stale claims

---

## 📂 Folder Structure

```
oac-second-brain/
├── wiki/                  ← 30 cross-linked markdown pages (the brain)
├── raw/
│   ├── pdfs/              ← 9 official Oracle PDFs + searchable .txt
│   ├── articles/          ← Curated source articles
│   └── notes/             ← Source references
├── index.md               ← Topic map (rendered as "All Topics")
├── log.md                 ← Ingestion history
├── CLAUDE.md              ← Operating rules for the AI maintainer
└── README.md              ← This page
```

---

## 🤝 Contributing

Found a gap or error? Want to add a source?

1. Fork the repo
2. Drop a new article/PDF into `raw/articles/` or `raw/pdfs/`
3. Open Claude Code: *"Ingest the new source"*
4. Claude updates the wiki + index + log
5. Commit and submit a PR

Or just [open an issue](https://github.com/ravibhuma/oac-second-brain/issues) describing what's missing.

---

## 📚 Sources

- [Oracle Analytics Cloud Documentation](https://docs.oracle.com/en/cloud/paas/analytics-cloud/) — 25+ official guides
- [Oracle Analytics Blog](https://blogs.oracle.com/analytics/) — Product updates
- [Oracle Analytics YouTube](https://www.youtube.com/c/OracleAnalytics) — Video tutorials
- [OAC Prompt Studio](https://ravi-bhuma.github.io/oac-prompt-studio/) — AI Agents framework

---

## 📜 License & Attribution

MIT License — see [LICENSE](https://github.com/ravibhuma/oac-second-brain/blob/main/LICENSE).

Oracle documentation is © Oracle Corporation, included as searchable PDFs for fair-use review and educational reference.

---

## 👤 Author

Maintained by **[@ravibhuma](https://github.com/ravibhuma)** ([Medium](https://medium.com/@ravishankerb)).
Inspired by [Andrej Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

⭐ **[Star this repo](https://github.com/ravibhuma/oac-second-brain)** if you find it useful — it helps others discover it.
