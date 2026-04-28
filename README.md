# OAC Knowledge Graph

> **An open-source community knowledge base for Oracle Analytics Cloud — built without RAG, vector databases, or embeddings. Just markdown, grep, and the LLM you already use.**

[![License: MIT](https://img.shields.io/badge/License-MIT-2D7D55.svg)](https://opensource.org/licenses/MIT)
[![Site Status](https://img.shields.io/badge/docs-live-00A36C)](https://ravibhuma.github.io/oac-second-brain/)
[![Topic: Oracle Analytics Cloud](https://img.shields.io/badge/topic-Oracle%20Analytics%20Cloud-C74634)](https://www.oracle.com/business-analytics/analytics-cloud/)
[![No Vector DB](https://img.shields.io/badge/no-vector%20database-2D7D55)](#-why-this-works-without-vectorization)
[![Pattern: LLM Wiki by A. Karpathy](https://img.shields.io/badge/pattern-LLM%20Wiki%20by%20A.%20Karpathy-1F5A3D)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

> ⚠️ **Unofficial / Community-Built.** Not affiliated with, sponsored by, or endorsed by Oracle Corporation. "Oracle", "Oracle Analytics Cloud", and related marks are trademarks of Oracle and/or its affiliates. This project is an independent community resource that synthesizes publicly available Oracle documentation, blogs, and tutorials for educational use.

---

## 🕸️ See The Knowledge As A Graph

**[👉 Open the Interactive Knowledge Graph](graph/)** — explore how 30+ Oracle Analytics Cloud topics connect. Hover, search, click any node to jump to its page. Zero install.

---

## ⚡ Try It In 60 Seconds

```bash
git clone https://github.com/ravibhuma/oac-second-brain.git
cd oac-second-brain
claude    # or: codex, or upload to Gemini/ChatGPT
> How do I configure row-level security in OAC?
```

That's it. No vector database. No chunking pipeline. No embedding model. Just **markdown + an LLM**.

📖 [Browse the site](https://ravibhuma.github.io/oac-second-brain/) · 💬 [Setup any AI tool](AI_ASSISTANTS.md) · 🤖 [OAC Prompt Studio](https://ravi-bhuma.github.io/oac-prompt-studio/)

---

## 🧠 What Is This?

A **comprehensive, AI-maintained knowledge base** for Oracle Analytics Cloud — covering every feature, component, and topic end-to-end.

- **30+ cross-linked wiki pages** organized by domain
- **9 official Oracle PDFs** (~6.8 MB searchable text) as deep reference
- **Source articles** from Oracle blogs, Medium, YouTube
- **Coverage matrix** mapping every Oracle docs guide to wiki pages
- **Open source** — fork, extend, contribute

Built using [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

---

## 🎯 Why This Works Without Vectorization

Most "AI Q&A over docs" projects today use **RAG** (Retrieval-Augmented Generation):
- Chunk documents into 500-token pieces
- Compute vector embeddings
- Store in a vector database (Pinecone, Weaviate, Chroma)
- At query time: vectorize the question, retrieve nearest chunks, send to LLM

This is **complex, costly, and lossy**. And for focused-domain knowledge bases (under ~10 MB), it's overkill.

### LLM Wiki Pattern — A Simpler Approach

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
| **Storage** | Vector database (Pinecone/Weaviate/Chroma) | Plain markdown files in a Git repo |
| **Indexing pipeline** | Chunk → embed → upsert (rebuilds on update) | None — `git pull` is the update |
| **Retrieval** | Cosine similarity over vectors | `grep` + folder structure + wiki links |
| **Chunking** | Required, lossy, parameter-dependent | None — full pages stay intact |
| **Embedding model dependency** | Yes — drift on model upgrades | No — works with any LLM |
| **Citation precision** | Approximate (chunk-level) | Exact (file + line number) |
| **Context fidelity** | Chunks may miss surrounding context | Full pages preserve meaning |
| **Cost (running)** | Vector DB + embedding API + LLM | LLM only |
| **Setup time** | Hours-days | Minutes |
| **Update latency** | Re-embed pipeline | Immediate (git push) |
| **Best for** | Millions of documents | Focused domain knowledge |

### When This Pattern Works

✅ Domain knowledge fits in a single repo (typically up to 5-10 MB of text)
✅ Modern LLM with 100K+ context window (Claude, GPT-4, Gemini, all recent)
✅ Content has natural structure (folders, cross-links)
✅ Authoritative sources can be kept as raw text alongside synthesized wiki

### When You Still Need RAG

❌ Knowledge base is millions of documents (web-scale)
❌ Sub-second latency at massive concurrency required
❌ Multi-tenant, dynamic per-user knowledge

For Oracle Analytics Cloud (~7 MB of canonical docs), **LLM Wiki wins on every dimension**.

---

## 🔍 How Different Users Use This

| Persona | How they use it |
|---|---|
| **OAC Learner** | Browse the site, search keywords, follow `[[wiki links]]` to related topics |
| **OAC Developer** | Clone repo, ask Claude Code: *"Show me Logical SQL for time-series with example"* |
| **OAC Architect** | Read the [Coverage Matrix](wiki/Docs%20Coverage%20Matrix.md) to validate gap analysis |
| **AI Agent Builder** | Bundle wiki PDFs into 8 grouped files, upload to OAC AI Agent, apply [R.T.C.C.O.E framework](wiki/OAC%20AI%20Agents.md) |
| **Team Lead** | Fork the repo for your org, add internal patterns, host privately |
| **Contributor** | Drop new sources in `raw/`, run `claude ingest`, submit a PR |

---

## 🚀 Two Steps To Get Started

### Step 1 — Get The Knowledge Base

**For browsing**: [https://ravibhuma.github.io/oac-second-brain/](https://ravibhuma.github.io/oac-second-brain/) (no install)

**For AI Q&A**: clone it
```bash
git clone https://github.com/ravibhuma/oac-second-brain.git
cd oac-second-brain
```

### Step 2 — Pick Your AI Assistant

This works with **every major AI tool**. Pick one you already use:

| Tool | Quick Setup | Cost |
|---|---|---|
| **[Claude Code](CLAUDE_CODE_SETUP.md)** | `npm install -g @anthropic-ai/claude-code` → `claude` | Free tier |
| **[OpenAI Codex](CODEX_SETUP.md)** | `npm install -g @openai/codex` → `codex` | Free tier / $20 |
| **[Google Gemini](https://gemini.google.com)** | Upload all 9 PDFs in browser | **Free** |
| **[ChatGPT](https://chatgpt.com)** | Upload PDFs or build a Custom GPT | Free / $20 |
| **[Cursor](https://cursor.com)** / **[Cline](https://github.com/cline/cline)** | Open repo as workspace, ask `@workspace ...` | Free / $20 |
| **[Ollama](https://ollama.ai)** + AnythingLLM | Local, private, offline | Free |
| **OAC AI Agent** | Bundle into PDFs, build inside OAC | Already in OAC |

**👉 Full guide for all 12 tools: [AI_ASSISTANTS.md](AI_ASSISTANTS.md)**

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
```

---

## 📚 Topics Covered

**Platform & Architecture** · OAC Overview · OAC vs OBIEE vs OAS · Subscribe & Provisioning · What's New
**Data Layer** · Data Sources & Connections · Semantic Model · Subject Areas & Datasets
**Analytics & Reporting** · Workbooks & Visualizations · Maps & Geospatial · Classic Dashboards · BI Publisher
**Data Engineering** · Data Flows & Preparation · Machine Learning & AI Features
**AI Ecosystem** · OAC AI Ecosystem · OAC AI Agents · OAC MCP Server
**Governance & Security** · Security & RLS · Administration & Service Console
**Developer Reference** · Logical SQL · APIs & Embedding · OCI REST APIs & CLI · Custom Visualizations
**End User** · Consumer Guide · Mobile App
**Operations** · KPIs & Alerts · Migration & Lifecycle · FAQs & Troubleshooting

📋 [Full topic index](topics.md) · 📊 [Coverage matrix vs Oracle docs](wiki/Docs%20Coverage%20Matrix.md)

---

## 🏗️ Folder Structure

```
oac-second-brain/
├── wiki/                  ← 30 cross-linked markdown pages (the brain)
├── raw/
│   ├── pdfs/              ← 9 official Oracle PDFs + searchable .txt
│   ├── articles/          ← Curated source articles
│   └── notes/             ← Source references
├── index.md               ← Topic map
├── log.md                 ← Ingestion history
├── CLAUDE.md              ← Operating rules for AI maintainers
└── README.md              ← This page
```

---

## 🔄 The Maintenance Loop

```
SOURCES (you curate)        →   raw/         (PDFs, articles, notes)
        ↓ ingest
WIKI (LLM-maintained)       →   wiki/        (cross-linked pages)
        ↓ query
ANSWERS (with citations)         from wiki + raw
        ↓ feedback
NEW SOURCES                 →   back to raw/
```

**Three operations:**
- **Ingest** — Add sources, LLM updates wiki pages
- **Query** — Ask questions, LLM answers with citations
- **Lint** — LLM checks for broken links, contradictions, stale claims

---

## 🌟 Why This Pattern Matters Beyond OAC

This repo is also a **case study** in a broader pattern:

> **For focused domain knowledge bases (under ~10 MB), the LLM Wiki pattern beats RAG on cost, speed, accuracy, and simplicity.**

You can apply the same approach to:
- Internal company wikis
- Product documentation
- API references
- Compliance / policy docs
- Personal knowledge management
- Any domain with stable, authoritative sources

Karpathy's insight: **the wiki is a persistent, compounding artifact**. Synthesize once, query forever — without infrastructure.

---

## 🤝 Contributing

Found a gap? Want to add a source?

1. Fork the repo
2. Drop a new article/PDF into `raw/articles/` or `raw/pdfs/`
3. Open Claude Code: *"Ingest the new source"*
4. Claude updates the wiki + index + log
5. Submit a PR

Or just [open an issue](https://github.com/ravibhuma/oac-second-brain/issues) describing what's missing.

---

## 📚 Sources

- [Oracle Analytics Cloud Documentation](https://docs.oracle.com/en/cloud/paas/analytics-cloud/) — 25+ official guides
- [Oracle Analytics Blog](https://blogs.oracle.com/analytics/) — Product updates
- [Oracle Analytics YouTube](https://www.youtube.com/c/OracleAnalytics) — Video tutorials
- [OAC Prompt Studio](https://ravi-bhuma.github.io/oac-prompt-studio/) — AI Agents framework

---

## 🙏 Acknowledgments

### The LLM Wiki Pattern — Andrej Karpathy
This project is a direct application of **Andrej Karpathy's LLM Wiki pattern**, originally published as a public gist:

📘 **Original gist**: [karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

Karpathy's core insight — *"the wiki is a persistent, compounding artifact; the cross-references are already there"* — guides every architectural decision in this repo:

- **`raw/`** = curated immutable sources (his pattern)
- **`wiki/`** = LLM-maintained synthesis layer (his pattern)
- **`CLAUDE.md`** = operating rules for the agent (his pattern)
- **Three operations: Ingest, Query, Lint** (his pattern)
- **Human curates, LLM does everything else** (his philosophy)

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
- All other trademarks are property of their respective owners

This project is **not affiliated with, sponsored by, or endorsed by Oracle, Anthropic, OpenAI, Google, or any other entity** mentioned. It is an independent community resource.

---

## 👤 Author

Maintained by **[@ravibhuma](https://github.com/ravibhuma)** ([Medium](https://medium.com/@ravishankerb)).

Companion projects:
- [OAC Prompt Studio](https://ravi-bhuma.github.io/oac-prompt-studio/) — Open-source learning platform for OAC AI Agents (R.T.C.C.O.E framework)
- [Building Effective OAC AI Agents](https://medium.com/@ravishankerb/building-effective-oac-ai-agents-the-framework-the-techniques-and-the-resource-hub-to-get-you-eba3797ca991) — Medium article

⭐ **[Star this repo](https://github.com/ravibhuma/oac-second-brain)** — it helps others discover the LLM Wiki pattern by Andrej Karpathy.
