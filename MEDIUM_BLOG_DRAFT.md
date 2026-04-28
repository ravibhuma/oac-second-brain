# I Built A Production Knowledge Base Without RAG, Vector DBs, Or Embeddings — Here's How

## Apply Karpathy's LLM Wiki pattern to enterprise documentation. The OAC Second Brain case study.

---

**TL;DR**: I open-sourced a comprehensive knowledge base for Oracle Analytics Cloud — 30+ cross-linked wiki pages, 9 official Oracle PDFs, AI-queryable end-to-end. **No vector database. No embeddings. No chunking pipeline.** Just markdown, grep, Git, and the LLM you already use. It's faster to build, cheaper to run, more accurate, and easier to maintain than RAG. Here's what I learned.

🔗 **Live site**: https://ravibhuma.github.io/oac-second-brain
🔗 **Repo**: https://github.com/ravibhuma/oac-second-brain

---

## The Problem With "AI Q&A Over Docs" Today

Every team I talk to is trying to build an AI assistant for their internal documentation. The standard playbook looks like this:

1. Pick a vector database (Pinecone, Weaviate, Chroma, pgvector, ...)
2. Pick a chunking strategy (500 tokens? semantic? recursive? overlap?)
3. Pick an embedding model (OpenAI text-embedding-3? BGE? Cohere?)
4. Build a pipeline: documents → chunk → embed → upsert
5. Build a retriever: query → embed → similarity search → top-K → re-rank
6. Build a prompt: system instructions + retrieved chunks + user question
7. Wire up the LLM
8. Pay for: vector DB hosting, embedding API calls, LLM API calls

This is **RAG** — Retrieval-Augmented Generation. It's the de-facto pattern for knowledge-grounded LLM applications.

It also has **a lot of moving parts**, each with parameters that affect quality:
- Chunk size too small → loses context
- Chunk size too big → less precise retrieval
- Wrong embedding model → wrong nearest neighbors
- Re-ranker mis-tuned → hallucinated answers
- Embeddings drift on model upgrades → must re-embed everything
- Vector DB scaling costs add up

And the kicker: **citations are approximate**. The LLM gets chunks, not full pages. It can hallucinate which document it's citing. Trust gets eroded.

Then I read [Andrej Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — and realized **for many real-world knowledge bases, RAG is overkill**.

---

## The Simpler Alternative: LLM Wiki Pattern

Karpathy's insight is deceptively simple:

> *"The wiki is a persistent, compounding artifact. The cross-references are already there."*

The pattern:

```
SOURCES (curated by humans)        →   raw/         (PDFs, articles, notes)
        ↓ ingest (LLM-driven)
WIKI (maintained by the LLM)       →   wiki/        (cross-linked .md pages)
        ↓ query
ANSWERS                                 LLM reads wiki + greps raw + cites
```

**Three layers of files. That's it.**

- `raw/` is your immutable source of truth (Oracle PDFs in my case)
- `wiki/` is the synthesized, cross-linked, LLM-maintained brain
- `CLAUDE.md` (or `AGENTS.md`) tells the LLM how to behave

No vector DB. No embeddings. No chunking. No re-ranker. No pipeline.

**Why does this work?**

Because modern LLMs have **enormous context windows**:
- Claude 3.5 Sonnet: 200K tokens
- GPT-4 Turbo: 128K tokens
- Gemini 1.5 Pro: 2M tokens (!)
- Claude 3 Opus: 200K tokens

For a focused-domain knowledge base (anything under ~5-10 MB of text), **the whole thing fits in the context window**. There's no need to retrieve a few chunks — you can give the LLM everything relevant and let it reason.

And when you don't want to spend tokens on full corpus: **just grep**. `grep -r "row level security" raw/` finds exact matches in milliseconds. The LLM reads those specific sections. Citations are exact.

---

## Case Study: OAC Second Brain

I work with **Oracle Analytics Cloud** (OAC). The official documentation spans **25+ guides**, thousands of pages, plus blogs, YouTube videos, and community forums. Every OAC project starts with: *"Where do I find X?"*

I decided to test the LLM Wiki pattern by building a comprehensive OAC knowledge base.

### What I Built

```
oac-second-brain/
├── wiki/                                    ← 30 cross-linked .md pages
│   ├── OAC Overview & Architecture.md
│   ├── Semantic Model.md
│   ├── Logical SQL Reference.md
│   ├── OAC AI Agents.md
│   ├── OAC MCP Server.md
│   └── ... (25 more)
├── raw/
│   ├── pdfs/                                ← 9 Oracle docs PDFs (~6.8 MB text)
│   ├── articles/                            ← Blog posts, Medium articles
│   └── notes/                               ← Source references
├── CLAUDE.md                                ← Operating rules for the LLM
└── README.md
```

### How I Built It (In One Session)

1. **Bootstrap from training data**: Asked Claude to draft 16 wiki pages on every major OAC topic. Got a solid but shallow first draft.

2. **Curate sources**: Downloaded 9 official Oracle PDFs (Building Semantic Models, Visualizing Data, Administering OAC, etc.) into `raw/pdfs/`.

3. **Convert to searchable text**: One command:
   ```bash
   for f in *.pdf; do pdftotext -layout "$f" "${f%.pdf}.txt"; done
   ```
   Now I had ~6.8 MB of grep-able text alongside the PDFs.

4. **Update CLAUDE.md**: Added the rule "When answering, grep `raw/pdfs/*.txt` for keywords, then read matching sections, then synthesize."

5. **Test**: Asked Claude — *"How do I configure event polling tables?"* — and got a deep, cited answer pulled from the actual Oracle docs.

That's the entire build process. **No vector DB. No embedding job. No chunking parameters to tune.**

### What End Users Get

```bash
git clone https://github.com/ravibhuma/oac-second-brain.git
cd oac-second-brain
claude
> How do I configure row-level security in OAC?
```

Claude reads the wiki for structure, greps the PDFs for specifics, and answers with **exact file + line citations**. The same content can be uploaded to Gemini, ChatGPT, or any other LLM.

For browsing without AI: I publish the wiki as a [Material for MkDocs site on GitHub Pages](https://ravibhuma.github.io/oac-second-brain/) — full search, dark mode, sidebar nav.

For Obsidian users: clone the repo, open as a vault, and you get the **graph view** with all `[[wiki links]]` rendered visually.

---

## RAG vs LLM Wiki: Side-By-Side

| Aspect | Traditional RAG | LLM Wiki Pattern |
|---|---|---|
| **Storage** | Vector database (Pinecone/Weaviate/Chroma) | Plain markdown files in a Git repo |
| **Indexing pipeline** | Chunk → embed → upsert | None — `git pull` is the update |
| **Retrieval** | Cosine similarity over vectors | `grep` + folder structure + `[[wiki links]]` |
| **Chunking** | Required, lossy, parameter-dependent | None — full pages stay intact |
| **Embedding model** | Required (drifts on upgrades) | None |
| **Citation precision** | Chunk-level (approximate) | File + line (exact) |
| **Context fidelity** | Chunks may miss surrounding context | Full pages preserved |
| **Cost (running)** | Vector DB + embedding API + LLM | LLM only |
| **Setup time** | Hours-days | Minutes |
| **Update latency** | Re-embed pipeline | Immediate (`git push`) |
| **Best for** | Millions of documents | Focused domain knowledge |

---

## When LLM Wiki Wins (And When RAG Still Wins)

This is **not** "RAG is dead." It's "RAG is overkill for many cases."

### LLM Wiki Wins When:
- Knowledge base fits in ~5-10 MB of text (most enterprise documentation does)
- Modern LLM with 100K+ context window is acceptable
- Authoritative sources can be kept as raw text
- Updates happen via human curation (not real-time data ingest)
- Citation precision and trust matter

### RAG Still Wins When:
- Millions of documents (web-scale search)
- Sub-second latency at massive concurrency
- Multi-tenant per-user knowledge bases
- Real-time streaming data sources

For the **70%+ of enterprise knowledge use cases** (internal wikis, product docs, API references, compliance manuals, runbooks) — LLM Wiki is faster, cheaper, more accurate.

---

## The Maintenance Loop

This is where Karpathy's pattern shines beyond just "Q&A":

```
User asks question
       ↓
Wiki gives 80% of the answer
       ↓
Grep raw/ for the rest
       ↓
Cite both sources
       ↓
Question reveals a wiki gap
       ↓
Ingest a new source addressing the gap
       ↓
Wiki compounds — next user benefits
```

**Three operations** I run on the repo:
- `ingest`: drop a new source → "Update affected wiki pages"
- `query`: ask a question → "Answer with citations"
- `lint`: periodic health check → "Find broken links, contradictions, stale claims"

The wiki **gets better over time** as more sources are ingested. It doesn't drift like vector embeddings do on model upgrades.

---

## Connecting To OAC AI Agents (My Own Framework)

This work fits into a broader pattern I've been developing for [building effective OAC AI Agents](https://medium.com/@ravishankerb/building-effective-oac-ai-agents-the-framework-the-techniques-and-the-resource-hub-to-get-you-eba3797ca991) using the **R.T.C.C.O.E framework** (Role, Task, Context, Constraints, Output, Examples).

The OAC Second Brain provides the **knowledge documents** for OAC AI Agents:

- Bundle wiki pages into 8 grouped PDFs (Oracle's 10-file × 5-MB limit)
- Upload as Knowledge Documents in your OAC AI Agent
- Apply R.T.C.C.O.E supplemental instructions
- Now your OAC AI Agent has expert OAC knowledge

It's the same content reused across surfaces:
- **Browse**: GitHub Pages site
- **CLI Q&A**: Claude Code / Codex
- **Web Q&A**: Gemini / ChatGPT
- **In-product**: OAC AI Agent
- **External AI**: OAC MCP Server

One knowledge base, many surfaces. **The Karpathy pattern delivers this naturally** because the artifact is plain text — universally portable.

---

## Try It Yourself (In 60 Seconds)

```bash
# Install Claude Code (or use any AI tool of your choice)
npm install -g @anthropic-ai/claude-code

# Clone the knowledge base
git clone https://github.com/ravibhuma/oac-second-brain.git
cd oac-second-brain

# Start asking questions
claude
> How do I configure row-level security in OAC?
> What's the R.T.C.C.O.E framework for AI Agents?
> Compare OAC vs OBIEE migration paths
```

**It works the same with Codex, Gemini, ChatGPT, Cursor, Cline, GitHub Copilot, or local LLMs via Ollama.** No tool lock-in.

---

## Apply This Pattern To Your Domain

The OAC Second Brain is open source — fork it, replace `wiki/` and `raw/` with your domain content, and you have an instant knowledge base for:

- Your internal company wiki
- Your product documentation
- Your API reference
- Your compliance / policy docs
- Your team's runbooks
- Your personal knowledge management

Steps:
1. Fork the repo
2. Empty `wiki/` and `raw/`
3. Drop your sources into `raw/`
4. Update `CLAUDE.md` with your domain context
5. Run Claude Code: *"Build wiki pages from raw/"*
6. Push to GitHub Pages — instant docs site
7. Share the repo — anyone with any LLM can query it

---

## What Karpathy Got Right

The deep insight in Karpathy's LLM Wiki gist isn't the technical pattern — it's the **division of labor**:

> *"The human's job is to curate sources, direct the analysis, ask good questions. The LLM's job is everything else."*

In RAG systems, humans become pipeline operators (chunk size, embedding choice, re-rank tuning). In the LLM Wiki pattern, humans become **editors and curators**. The LLM does the synthesis, cross-linking, and search.

This scales better with your knowledge base than your infrastructure.

---

## Closing — The Surprising Outcome

I started this project intending to test whether the LLM Wiki pattern could work for a real, comprehensive enterprise knowledge base.

It did. But the more interesting outcome:

**I built a production-ready, AI-queryable knowledge base in a single session, with $0 of infrastructure, that's better than a $50K RAG project I'd have built six months ago.**

Modern LLMs with massive context windows have changed the calculus. For most knowledge use cases under 10 MB, **vectorization is yesterday's solution**.

Try it. Fork the [OAC Second Brain](https://github.com/ravibhuma/oac-second-brain). Apply the pattern to your own domain. See if you still need a vector database.

---

## Resources

- 🔗 **OAC Second Brain repo**: https://github.com/ravibhuma/oac-second-brain
- 🔗 **Live docs site**: https://ravibhuma.github.io/oac-second-brain
- 🔗 **Karpathy's LLM Wiki gist** (the inspiration): https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- 🔗 **OAC Prompt Studio** (companion AI Agents site): https://ravi-bhuma.github.io/oac-prompt-studio
- 🔗 **My previous article on OAC AI Agents (R.T.C.C.O.E framework)**: https://medium.com/@ravishankerb/building-effective-oac-ai-agents-the-framework-the-techniques-and-the-resource-hub-to-get-you-eba3797ca991

---

**About the author**: Ravi Bhuma is an Oracle Analytics Cloud architect, AI Agent builder, and open-source contributor. Find me on [GitHub](https://github.com/ravibhuma) and [Medium](https://medium.com/@ravishankerb).

If this resonated, ⭐ [star the repo](https://github.com/ravibhuma/oac-second-brain) — it helps others discover the LLM Wiki pattern.

---

*Tags: #AI #LLM #KnowledgeManagement #RAG #OracleAnalyticsCloud #OAC #ClaudeCode #LLMWiki #Karpathy #OpenSource*
