# AI Skills & Integrations

> **Pre-configured agent skills and instructions** that make the OAC Knowledge Graph instantly usable with every major AI assistant. Clone the repo, point your tool at the folder, and start asking OAC questions with no manual prompt engineering.

This repo ships with **pre-built skills/instructions** for every major AI tool. You don't have to configure prompts manually — just point your AI tool at the cloned folder.

---

## What Ships In This Repo

| File / Folder | Used By | Purpose |
|---|---|---|
| `.claude/skills/oac-knowledge.md` | **Claude Code** | Q&A skill — answers OAC questions with citations |
| `.claude/skills/oac-ingest.md` | **Claude Code** | Add new sources to the wiki |
| `.claude/skills/oac-lint.md` | **Claude Code** | Periodic health check |
| `CLAUDE.md` | **Claude Code, Claude Desktop** | Project-level operating rules |
| `AGENTS.md` | **OpenAI Codex, Cline, agent IDEs** | Project-level agent instructions |
| `.cursorrules` | **Cursor** | Cursor-specific conventions |
| `PROJECT_INSTRUCTIONS.md` | **Claude Project, Custom GPT, Gemini Gem** | Custom instructions to paste into web AI projects |

When you clone this repo, **all of these activate automatically** for the AI tool you use. No manual setup required beyond installing the tool itself.

---

## Tool-By-Tool Setup

### 🥇 Claude Code (Recommended)

```bash
# Install
npm install -g @anthropic-ai/claude-code

# Use
git clone https://github.com/ravibhuma/oac-knowledge-graph.git
cd oac-knowledge-graph
claude

# Inside Claude Code:
> /skill oac-knowledge "How do I configure row-level security?"
> /skill oac-ingest "Update the wiki from the new file in raw/articles/"
> /skill oac-lint "Health check the wiki"
```

The skills in `.claude/skills/` activate automatically — Claude knows how to query, ingest, and lint without you explaining the structure.

📘 Full guide: [CLAUDE_CODE_SETUP.md](CLAUDE_CODE_SETUP.md)

---

### 🥈 OpenAI Codex

```bash
# Install
npm install -g @openai/codex

# Use
git clone https://github.com/ravibhuma/oac-knowledge-graph.git
cd oac-knowledge-graph
codex

# Codex automatically reads AGENTS.md from the project root
> How do I configure row-level security in OAC?
```

The `AGENTS.md` file at the project root tells Codex how to use the wiki + PDFs + cite sources. No manual prompt needed.

📘 Full guide: [CODEX_SETUP.md](CODEX_SETUP.md)

---

### 🥉 Cursor

```bash
# Open Cursor
# File → Open Folder → select cloned oac-knowledge-graph
# Cursor auto-detects .cursorrules
# Press Ctrl+L (or Cmd+L on Mac) to open chat
```

Reference paths in your prompt:
```
@wiki Explain row-level security
@raw/pdfs/building-semantic-models-oracle-analytics-cloud.txt How do hierarchies work?
@workspace Compare OAC AI Agents to MCP Server
```

The `.cursorrules` file in this repo configures Cursor to use the two-layer query strategy automatically.

---

### Cline (VS Code Extension)

```bash
# 1. Install VS Code
# 2. Install Cline extension from VS Code Marketplace
# 3. Configure Cline with your Anthropic / OpenAI / Gemini API key
# 4. Open the cloned folder in VS Code
# 5. Cline auto-reads AGENTS.md
# 6. Open Cline panel → ask:
> How do I configure row-level security in OAC?
```

Cline uses the `AGENTS.md` for project context and reads files automatically with citations.

---

### GitHub Copilot Chat

```bash
# 1. Sign in to GitHub Copilot ($10/mo)
# 2. Install GitHub Copilot Chat extension in VS Code
# 3. Open the cloned folder
# 4. Open Chat with Ctrl+Shift+I
# 5. Use @workspace for repo-scoped questions:
@workspace How does OAC's Semantic Model work?
@workspace Show me Logical SQL syntax for time-series functions
```

Copilot doesn't directly use AGENTS.md but `@workspace` reads from your open files including the wiki.

---

### Claude Project (claude.ai)

For non-technical users who want a shareable URL with knowledge baked in:

```
1. Sign in at https://claude.ai (Pro tier $20/mo recommended for sharing)
2. Click Projects → Create Project
3. Name: "OAC Knowledge Graph"
4. Set custom instructions: paste contents of PROJECT_INSTRUCTIONS.md
5. Add Content → upload all 30 wiki/*.md files + index.md + CLAUDE.md
6. Optionally upload selected PDFs from raw/pdfs/
7. Share → copy link → share with team or public
```

End users with Claude Plus accounts get free access via your link.

---

### ChatGPT (Custom GPT)

```
1. Sign in to https://chatgpt.com (Plus $20/mo required to create Custom GPTs)
2. Go to https://chatgpt.com/gpts/editor
3. Create a Custom GPT named "OAC Knowledge Assistant"
4. Instructions: paste contents of PROJECT_INSTRUCTIONS.md
5. Knowledge: upload wiki/*.md + selected PDFs (max 20 files)
6. Save → publish → share the public link
```

Free ChatGPT users can use your shared GPT.

---

### Google Gemini (Gem)

```
1. Sign in to https://gemini.google.com (Gemini Advanced for sharing)
2. Click Gems in sidebar → New Gem
3. Name: "OAC Knowledge Graph"
4. Instructions: paste contents of PROJECT_INSTRUCTIONS.md
5. Upload knowledge files (Gemini accepts up to ~100MB — ALL 9 PDFs fit!)
6. Save → Test → Share
```

Gemini's huge file limits make it the **best free option** for full repo + PDFs.

---

### Cline / Continue / Other VS Code Extensions

Most AI coding extensions read `AGENTS.md` from project root by convention. Just open the cloned folder.

---

### Ollama (Local, Offline, Private)

For sensitive data or air-gapped environments:

```bash
# 1. Install Ollama
# Download from https://ollama.ai

# 2. Pull a model (qwen2.5:14b or llama3.1 work well)
ollama pull qwen2.5:14b

# 3. Install AnythingLLM
# Download from https://anythingllm.com

# 4. In AnythingLLM:
#    - Create new workspace: "OAC Knowledge Graph"
#    - Set LLM provider: Ollama
#    - Upload all files from cloned folder
#    - Start chatting offline
```

Trade-offs: slower than cloud LLMs, smaller context window, less polished — but **completely free, private, and offline**.

---

### OAC AI Agent (Inside OAC)

The on-brand path if you have an OAC instance — apply the [R.T.C.C.O.E framework](wiki/OAC%20AI%20Agents.md):

```
1. Bundle wiki/*.md into 8 grouped PDFs (Oracle's 10-file × 5-MB limit)
2. OAC → Create → AI Agent
3. Dataset: pick or create any indexed dataset (placeholder OK)
4. Supplemental Instructions: paste R.T.C.C.O.E spec
5. Knowledge Documents: upload up to 10 PDFs (≤ 5 MB each)
6. Welcome Message: include sample questions
7. Save → test → iterate SI weekly
```

📘 Full framework: [wiki/OAC AI Agents.md](wiki/OAC%20AI%20Agents.md)

---

## What Each Skill Does

### `oac-knowledge` (Claude Code)
Answers OAC questions using the two-layer strategy:
1. Search wiki/ for organized synthesis
2. Grep raw/pdfs/*.txt for specific keywords
3. Cite both wiki page + source PDF

### `oac-ingest` (Claude Code)
Adds new sources to the wiki:
1. Reads file from raw/articles/, raw/pdfs/, or raw/notes/
2. Identifies affected wiki pages
3. Updates those pages with new facts
4. Adds cross-links
5. Appends to log.md
6. Runs audit script

### `oac-lint` (Claude Code)
Periodic wiki health check:
1. Finds broken links, contradictions, orphans
2. Checks PDF coverage and citations
3. Reports stale content
4. Suggests fixes

---

## How To Test Your Setup

After installing your chosen AI tool and pointing it at the cloned folder, run this verification question:

```
"How do I configure row-level security in OAC? Cite sources."
```

A correctly configured AI should:
1. Reference `wiki/Security & Row-Level Security.md`
2. Mention the 4 RLS methods (Subject Area Data Filters, VPD, Connection Pool, BMM Layer Filters)
3. Cite `building-semantic-models-oracle-analytics-cloud.txt` from raw/pdfs/
4. Link to the corresponding Oracle docs URL

If it does all four, your setup works.

---

## Recommended Stack For Different Users

| User type | Recommended setup |
|---|---|
| **OAC Architect** (daily reference) | Clone repo + Claude Code locally + Obsidian for visual browsing |
| **OAC Developer** | Clone repo + Codex CLI or Cursor for in-IDE queries |
| **Business User** | Use the public site OR Claude Project link |
| **Manager / Casual Browser** | Just bookmark the [browsable site](https://ravibhuma.github.io/oac-knowledge-graph/) |
| **Privacy-Sensitive Org** | Clone repo + Ollama + AnythingLLM (everything local) |
| **Existing OAC Customer** | Build OAC AI Agent inside your OAC instance using these wiki PDFs as Knowledge Documents |
| **Team Lead** | Fork the repo for your org + add internal patterns + host privately |

---

## Companion Resources

- 📘 [CLAUDE_CODE_SETUP.md](CLAUDE_CODE_SETUP.md) — Detailed Claude Code setup
- 📘 [CODEX_SETUP.md](CODEX_SETUP.md) — Detailed Codex setup
- 📘 [AI_ASSISTANTS.md](AI_ASSISTANTS.md) — All 12 AI tools setup walkthrough
- 📘 [PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md) — Custom instructions for Claude Project / Custom GPT / Gemini Gem
- 📘 [SETUP.md](SETUP.md) — Repo setup if forking for your domain

---

## Author

Built by **[Ravi Bhuma](https://github.com/ravibhuma)** ([Medium](https://medium.com/@ravishankerb)).

If you build a Knowledge Graph for *your* domain using these skills, tag me — I'd love to see it. ⭐ [Star the repo](https://github.com/ravibhuma/oac-knowledge-graph) if useful.
