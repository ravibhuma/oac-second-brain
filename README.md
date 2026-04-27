# OAC Second Brain

> A comprehensive, AI-maintained knowledge base for **Oracle Analytics Cloud (OAC)** — covering every feature, component, and topic end-to-end.

Built on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): synthesize knowledge once, compound forever.

---

## What's Inside

- **29 cross-linked wiki pages** covering every Oracle Analytics Cloud topic
- **9 official Oracle PDF guides** (~6.8 MB searchable text) as deep reference
- **Source articles** from Oracle blogs, Medium, and YouTube
- **Coverage matrix** mapping every Oracle docs guide to wiki pages

### Topics Covered
Platform & Architecture · Data Sources & Connections · Semantic Model · Subject Areas & Datasets · Workbooks & Visualizations · Maps & Geospatial · Classic Dashboards & Analyses · BI Publisher · Data Flows · Machine Learning & AI · OAC AI Agents (R.T.C.C.O.E framework) · OAC MCP Server · OAC AI Ecosystem · Security & RLS · Administration · Logical SQL · APIs & Embedding · OCI REST APIs & CLI · Custom Visualizations · KPIs & Alerts · Mobile App · Migration & Lifecycle · Subscribe & Provisioning · Tutorials & Resources · OAC vs OBIEE vs OAS · FAQs & Troubleshooting

---

## How To Use This

There are **three ways**, pick whichever suits you:

### 🌐 1. Browse Online (No Install)
Visit the **GitHub Pages site** → full search, sidebar nav, dark mode:
> **`https://ravibhuma.github.io/oac-second-brain/`**

### 💬 2. Ask Questions (Claude Project)
Visit the **shared Claude Project** → ask any OAC question, get answers grounded in this knowledge base:
> **`https://claude.ai/project/<shared-link>`**

### 🔧 3. Run Locally (For Power Users)
Clone the repo and use with [Obsidian](https://obsidian.md) (browse) and [Claude Code](https://claude.com/claude-code) (Q&A):

```bash
git clone https://github.com/ravibhuma/oac-second-brain.git
cd oac-second-brain
# Open the folder in Obsidian as a vault
# OR run: claude  (in this folder, with Claude Code installed)
```

Ask anything:
> *"How do I set up row-level security?"*
> *"Walk me through creating a Semantic Model from scratch"*
> *"What's the R.T.C.C.O.E framework for AI Agents?"*

---

## Folder Structure

```
oac-second-brain/
├── wiki/                  ← 29 cross-linked markdown pages (the brain)
├── raw/
│   ├── pdfs/              ← 9 official Oracle PDFs + searchable .txt
│   ├── articles/          ← Curated source articles
│   └── notes/             ← Source references
├── index.md               ← Map of all wiki pages
├── log.md                 ← Ingestion history
├── CLAUDE.md              ← Operating rules for the AI maintainer
└── README.md              ← This file
```

---

## How It Works (The Karpathy Pattern)

```
┌─────────────────────────────────────────────────────┐
│  SOURCES (you curate)        →   raw/               │
│  Oracle docs PDFs, blogs, articles, notes           │
└─────────────────────────────────────────────────────┘
                       ↓ ingest
┌─────────────────────────────────────────────────────┐
│  WIKI (LLM maintains)        →   wiki/              │
│  Cross-linked pages, compounds over time            │
└─────────────────────────────────────────────────────┘
                       ↓ query
┌─────────────────────────────────────────────────────┐
│  ANSWERS                                             │
│  Claude grep raw + read wiki → cite both            │
└─────────────────────────────────────────────────────┘
```

**Three operations**:
- **Ingest** — Add new sources, LLM updates wiki pages
- **Query** — Ask questions, LLM answers from wiki + raw
- **Lint** — LLM checks for broken links, contradictions, stale claims

---

## Contributing

Add a source → ingest → enrich the wiki:

1. Drop a new article/PDF into `raw/articles/` or `raw/pdfs/`
2. Open Claude Code in the repo folder
3. Run: *"Ingest the new source in raw/"*
4. Claude updates the wiki + `index.md` + `log.md`
5. Commit and push the changes

PRs welcome for: missing topics, error corrections, additional source material.

---

## Sources

- [Oracle Analytics Cloud Documentation](https://docs.oracle.com/en/cloud/paas/analytics-cloud/) — 25+ official guides
- [Oracle Analytics Blog](https://blogs.oracle.com/analytics/) — Product updates
- [Oracle Analytics YouTube](https://www.youtube.com/c/OracleAnalytics) — Video tutorials
- [OAC Prompt Studio (Ravi Bhuma)](https://ravi-bhuma.github.io/oac-prompt-studio/) — AI Agents framework

---

## License

MIT License — see [LICENSE](LICENSE).

The Oracle documentation referenced is © Oracle Corporation. This knowledge base is an independent, community-maintained synthesis under fair-use review/commentary principles.

---

## Author

Maintained by [@RaviBhuma](https://github.com/ravibhuma).
Inspired by [Andrej Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

⭐ **Star this repo** if you find it useful — it helps others discover it.
