# Use This Knowledge Base With Any AI Assistant

> Pick your preferred AI tool below. All work with this repo. Times shown are first-time setup.

| AI Assistant | Setup Time | Cost | Type |
|---|---|---|---|
| [Claude Code](#1-claude-code-cli) | 10 min | Free tier / $20 Pro | CLI agent |
| [OpenAI Codex](#2-openai-codex) | 10 min | Free tier / $20 Plus | CLI + cloud |
| [Claude Desktop](#3-claude-desktop) | 5 min | Free tier | Web/desktop |
| [ChatGPT](#4-chatgpt) | 5 min | Free / $20 Plus | Web |
| [Google Gemini](#5-google-gemini) | 5 min | **Free** | Web |
| [Microsoft Copilot](#6-microsoft-copilot) | 5 min | Free / $20 Pro | Web |
| [Perplexity](#7-perplexity) | 5 min | Free / $20 Pro | Web |
| [Cursor](#8-cursor) | 10 min | Free / $20 Pro | IDE |
| [Cline (VS Code)](#9-cline-vs-code-extension) | 5 min | Bring your API key | IDE extension |
| [GitHub Copilot Chat](#10-github-copilot-chat) | 5 min | $10/mo | IDE extension |
| [Ollama (Local)](#11-ollama-local-offline) | 30 min | **Free, offline** | Local LLM |
| [OAC AI Agent](#12-oac-ai-agent-inside-oac) | 1 hour | Already in OAC | Inside OAC |

---

## Prerequisites For All Tools

```bash
# Clone the repo first (one-time)
git clone https://github.com/ravibhuma/oac-knowledge-graph.git
cd oac-knowledge-graph
```

---

## 1. Claude Code (CLI)

**Best for**: power users, free tier covers casual use, deep agentic work

```bash
npm install -g @anthropic-ai/claude-code
cd oac-knowledge-graph
claude
> How do I configure row-level security in OAC?
```

📘 **Full guide**: [CLAUDE_CODE_SETUP.md](CLAUDE_CODE_SETUP.md)

---

## 2. OpenAI Codex

**Best for**: ChatGPT subscribers, cloud agent option

```bash
npm install -g @openai/codex
cd oac-knowledge-graph
codex
> How do I configure row-level security in OAC?
```

Or use **ChatGPT Codex** in your browser at chatgpt.com → Codex → connect this GitHub repo.

📘 **Full guide**: [CODEX_SETUP.md](CODEX_SETUP.md)

---

## 3. Claude Desktop

**Best for**: visual interface, no terminal, Claude.ai users

1. Sign up free at https://claude.ai
2. Download **Claude Desktop** (Windows/Mac)
3. Open a new chat → click the **paperclip icon**
4. Drag in:
   - The entire `wiki/` folder (30 .md files)
   - Selected PDFs from `raw/pdfs/` (each chat ~5MB total)
5. Ask: *"Using these files, how do I configure RLS in OAC?"*

> 💡 For larger context, use **Claude Project** — upload all files once, ask anytime.

---

## 4. ChatGPT

**Best for**: most users already have an account

1. Sign in at https://chatgpt.com
2. Click the **paperclip icon** in the chat input
3. Upload PDFs from `raw/pdfs/` (free tier supports up to 5 files / chat)
4. Ask: *"Using these PDFs, explain the Semantic Model architecture"*

**For persistent knowledge** ($20 Plus required):
1. Go to https://chatgpt.com/gpts/editor
2. Create a Custom GPT named **OAC Knowledge Graph Assistant**
3. Upload PDFs as Knowledge files
4. Paste contents of `PROJECT_INSTRUCTIONS.md` as the GPT Instructions
5. Save → share the public link

---

## 5. Google Gemini

**Best for**: free, handles the largest files

1. Go to https://gemini.google.com
2. Sign in with Google account
3. Click the **paperclip / "+" icon**
4. Upload **all 9 PDFs** from `raw/pdfs/` (Gemini supports up to ~100MB per chat)
5. Ask: *"Using these Oracle Analytics docs, how do I migrate from OBIEE to OAC?"*

**For a custom assistant** (Gemini Advanced):
1. Click **Gems** in sidebar → **New Gem**
2. Name: `OAC Knowledge Graph`
3. Paste contents of `PROJECT_INSTRUCTIONS.md` as instructions
4. Upload knowledge files
5. Save and use

---

## 6. Microsoft Copilot

**Best for**: enterprise users with Microsoft 365

1. Go to https://copilot.microsoft.com
2. Sign in with Microsoft account
3. Click the **paperclip icon**
4. Upload PDFs from `raw/pdfs/` (free supports a few; Copilot Pro for more)
5. Ask: *"Explain OAC's row-level security based on these docs"*

**With Copilot Pro / Microsoft 365 Copilot**: also works in Word, Excel, Teams chat with file attachments.

---

## 7. Perplexity

**Best for**: research-style answers with web + your docs combined

1. Go to https://perplexity.ai
2. Sign in
3. Click **+** → **Upload File**
4. Drop PDFs from `raw/pdfs/`
5. Ask: *"How does OAC compare to OBIEE for migration?"*

Perplexity will combine your uploaded docs with current web sources.

---

## 8. Cursor

**Best for**: developers who already use VS Code-like IDEs

1. Download Cursor from https://cursor.com
2. Open the cloned `oac-knowledge-graph` folder
3. Press **Ctrl+L** (or Cmd+L on Mac) to open chat
4. Reference the docs:
   ```
   @wiki Explain row-level security
   @raw/pdfs/building-semantic-models-oracle-analytics-cloud.txt How do hierarchies work?
   ```

Cursor reads the entire workspace and answers with file citations.

---

## 9. Cline (VS Code Extension)

**Best for**: VS Code users, bring your own API key

1. Install [VS Code](https://code.visualstudio.com)
2. Install the **Cline** extension from VS Code marketplace
3. Configure with your Anthropic / OpenAI / Gemini API key
4. Open the `oac-knowledge-graph` folder in VS Code
5. Open Cline panel → ask:
   ```
   How do I configure row-level security in OAC?
   ```

Cline reads files automatically and cites sources.

---

## 10. GitHub Copilot Chat

**Best for**: GitHub users with Copilot subscription

1. Sign in to GitHub Copilot ($10/mo)
2. In VS Code: install **GitHub Copilot Chat** extension
3. Open the `oac-knowledge-graph` folder
4. Open chat with **Ctrl+Shift+I** (Cmd+Shift+I on Mac)
5. Use **@workspace** to scope to the repo:
   ```
   @workspace How does OAC's Semantic Model work?
   ```

---

## 11. Ollama (Local, Offline)

**Best for**: privacy-sensitive users, offline use, free

```bash
# 1. Install Ollama
# Download from https://ollama.ai

# 2. Pull a model
ollama pull llama3.1
# Or for better quality:
ollama pull qwen2.5:14b

# 3. Install AnythingLLM (provides UI + RAG)
# Download from https://anythingllm.com

# 4. In AnythingLLM:
#    - Create new workspace: "OAC Knowledge Graph"
#    - Set LLM provider: Ollama
#    - Upload all files from oac-knowledge-graph folder
#    - Start chatting
```

Trade-offs: slower than cloud LLMs, smaller context window, less polished — but **completely free, private, and offline**.

---

## 12. OAC AI Agent (Inside OAC)

**Best for**: production OAC users who want this knowledge available natively in the OAC UI

This is the **on-brand path** if you have an OAC instance:

### Quick Steps

1. **Bundle wiki + selected sources into 8 grouped PDFs** (each ≤ 5 MB; use Pandoc or any md-to-pdf tool)
2. **OAC** → **Create** → **AI Agent**
3. **Dataset**: pick or create any indexed dataset (placeholder OK)
4. **Supplemental Instructions**: paste R.T.C.C.O.E spec (template in `wiki/OAC AI Agents.md`)
5. **Knowledge Documents**: upload up to 10 PDFs (≤ 5 MB each)
6. **Welcome Message**: include sample questions
7. **Save** → test → iterate SI weekly

📘 **Full framework**: [wiki/OAC AI Agents.md](wiki/OAC%20AI%20Agents.md)

---

## Which Tool Should You Pick?

```
Casual exploration, no install        →   Gemini (free, easy)
You're already using ChatGPT          →   ChatGPT Plus + Custom GPT
You're a developer                    →   Claude Code or Codex CLI
You want the fastest, deepest         →   Claude Code with Pro
You need privacy / offline            →   Ollama + AnythingLLM
You're already in OAC                 →   OAC AI Agent
You want shareable public link        →   Custom GPT or Claude Project
You use VS Code                       →   Cline or Copilot Chat
```

---

## Power User Tip — Use Two Tools

Different LLMs answer the same question differently. Try the same query in:
- **Claude Code** (cited, structured)
- **Codex CLI** (concise, code-focused)
- **Gemini** (broad, free)

Compare answers. The combination beats any single tool.

---

## Sample Questions To Try (In Any Tool)

```
"How do I configure row-level security in OAC?"
"Walk me through the three-layer Semantic Model architecture"
"What's the R.T.C.C.O.E framework for AI Agents?"
"Compare OAC vs OBIEE migration paths"
"Show me the Logical SQL syntax for time-series functions"
"What's the difference between Subject Areas and Datasets?"
"How does the OAC MCP Server work with external AI clients?"
"Walk me through provisioning an OAC instance on OCI"
"Explain BI Publisher bursting with a sales use case"
"List every option for connecting to private/on-prem databases"
```

---

## Updating The Knowledge Base

```bash
cd oac-knowledge-graph
git pull
```

Re-upload to your AI tool if needed (Gemini, ChatGPT, Custom GPT). Codex/Claude Code/Cursor auto-detect the new files.

---

## Companion Resources

- [📖 Browse the Wiki online](https://ravibhuma.github.io/oac-knowledge-graph/)
- [📂 GitHub Repo](https://github.com/ravibhuma/oac-knowledge-graph)
- [🤖 OAC Prompt Studio](https://ravi-bhuma.github.io/oac-prompt-studio/) — for building OAC AI Agents
- [✍️ Building Effective OAC AI Agents](https://medium.com/@ravishankerb/building-effective-oac-ai-agents-the-framework-the-techniques-and-the-resource-hub-to-get-you-eba3797ca991) — Medium article

---

## Issues / Feedback

[Open a GitHub issue](https://github.com/ravibhuma/oac-knowledge-graph/issues) — let us know which AI tool worked best, gaps in the knowledge base, or new sources to add.
