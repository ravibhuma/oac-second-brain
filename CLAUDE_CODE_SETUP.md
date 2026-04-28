# Claude Code Setup — Ask AI Questions About OAC

> Set up Claude Code in 10 minutes. Then ask any OAC question and get cited answers from this knowledge base.

---

## What You'll Get

After setup, you can ask in your terminal:
```
> How do I configure row-level security in OAC?
> What's the R.T.C.C.O.E framework for AI Agents?
> Walk me through the three-layer Semantic Model
> Compare OAC vs OBIEE migration paths
```

Claude reads the entire knowledge base (30+ wiki pages + 9 Oracle PDFs) and answers with citations. **Free tier available.**

---

## Prerequisites

| Requirement | Check |
|---|---|
| **OS** | Windows 10+, macOS, or Linux |
| **Node.js** | v18 or higher — [Download here](https://nodejs.org/) (LTS) |
| **Git** | [Download here](https://git-scm.com/downloads) (Windows users: includes Git Bash) |
| **Anthropic account** | Free signup at [claude.ai](https://claude.ai) |

**Verify Node.js + Git:** open a terminal and run:
```bash
node --version    # should show v18.x.x or higher
git --version     # should show 2.x.x
```

---

## Step 1 — Install Claude Code

### Windows / macOS / Linux (One Command)

Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux):

```bash
npm install -g @anthropic-ai/claude-code
```

Verify:
```bash
claude --version
```

> 💡 If you get a permission error on macOS/Linux, prefix with `sudo`. On Windows, run the terminal as administrator.

---

## Step 2 — Clone The Repo

Pick a folder where you want to keep the knowledge base:

```bash
cd C:\Users\YourName\Documents          # Windows
# or
cd ~/Documents                          # Mac/Linux

git clone https://github.com/ravibhuma/oac-knowledge-graph.git
cd oac-knowledge-graph
```

You should now be inside the `oac-knowledge-graph` folder, which contains `wiki/`, `raw/`, etc.

---

## Step 3 — Start Claude Code

From inside the `oac-knowledge-graph` folder:

```bash
claude
```

**First-time authentication:**
1. Claude Code will print a URL or open your browser
2. Sign in with your Anthropic account (or sign up free)
3. Authorize Claude Code
4. Return to your terminal — you'll see a chat prompt

You should now see something like:
```
Welcome to Claude Code!
cwd: /path/to/oac-knowledge-graph
>
```

---

## Step 4 — Ask Your First Question

Just type and press Enter:

```
How do I configure row-level security in OAC?
```

Claude will:
1. **Search the wiki** for relevant pages (semantic search)
2. **Grep the PDFs** for specific keywords
3. **Read** the matching sections
4. **Answer with citations** — points to wiki pages and PDF sources

Try follow-ups in the same conversation:
```
> Show me the SQL for the initialization block
> What if I'm using ADW as the data source?
> Compare this to OBIEE's approach
```

---

## Step 5 — Useful Claude Code Commands

While in the `claude` session, try these:

| Command | What it does |
|---|---|
| `/help` | List all built-in commands |
| `/clear` | Start a fresh conversation |
| `/exit` | Quit Claude Code |
| `Ctrl+C` | Stop a long-running answer |

---

## Example Q&A Session

```
> What's the R.T.C.C.O.E framework?

The R.T.C.C.O.E framework is a structured approach for writing
Supplemental Instructions when building OAC AI Agents...

[Detailed answer with sections for each letter]

Source: wiki/OAC AI Agents.md
Source: raw/articles/medium-building-effective-oac-ai-agents.md

> Give me an example for a Sales Operations Agent

Here's a complete R.T.C.C.O.E spec for a Sales Operations Agent...

[Worked example]
```

---

## Tips For Best Results

### Be specific
❌ *"Tell me about security"*
✅ *"How do I set up data filters in a Subject Area for region-based RLS?"*

### Ask follow-ups
✅ *"Now show me the init block SQL"*
✅ *"What if we're on Autonomous Database?"*

### Reference specific topics
✅ *"Use the Semantic Model wiki page to explain LTS fragmentation"*

### Ask for formats
✅ *"Give me a comparison table"*
✅ *"Show me the SQL with comments"*
✅ *"List the steps numbered"*

### Combine sources
✅ *"Cross-reference the AI Agents wiki with the Oracle blog post on AI Ecosystem"*

---

## Cost & Usage Limits

Claude Code uses your Anthropic account. As of 2026:

| Tier | Cost | Best For |
|---|---|---|
| **Free** | $0 | Light use — a few questions per day |
| **Pro** | $20/month | Heavy use — unlimited within fair-use |
| **Pay-as-you-go (API)** | ~$0.003-0.015/query | Unpredictable / heavy use |

Check current pricing: https://www.anthropic.com/pricing

> 💡 The free tier handles most casual exploration of this knowledge base.

---

## Troubleshooting

### `claude: command not found`
Node.js install didn't add npm globals to PATH. Fix:
- Close and reopen your terminal
- On Windows: log out and back in
- Or reinstall Node.js with the LTS installer (uncheck and recheck "Add to PATH")

### `EACCES: permission denied`
On Mac/Linux:
```bash
sudo npm install -g @anthropic-ai/claude-code
```

### Authentication browser doesn't open
Manually copy the URL Claude prints and paste it into your browser.

### Claude says "I don't have access to those files"
You're probably running `claude` from the wrong folder. Make sure you `cd` into `oac-knowledge-graph` first:
```bash
cd path/to/oac-knowledge-graph
claude
```

### Claude isn't citing sources
Add to your question: *"Cite the specific wiki page or PDF you used."*

### Want to reset everything?
```bash
claude --logout
# Then run claude again to re-authenticate
```

---

## Updating The Knowledge Base

When the maintainer pushes new content:

```bash
cd oac-knowledge-graph
git pull
```

Your next `claude` session will have the latest content automatically.

---

## What Makes This Better Than ChatGPT/Gemini Alone?

| | ChatGPT/Gemini (Generic) | Claude Code + This Repo |
|---|---|---|
| **Knowledge** | General training data | Curated OAC knowledge + Oracle PDFs |
| **Up-to-date** | Cutoff date (varies) | Updated when repo updates |
| **Citations** | Sometimes hallucinated | Real wiki/PDF references |
| **OAC-specific** | Generic | Built for OAC by an OAC expert |
| **Free tier** | ✅ | ✅ |

---

## Next Steps

✅ **You're set up.** Ask anything OAC-related.

If you find gaps or errors, [open a GitHub issue](https://github.com/ravibhuma/oac-knowledge-graph/issues) or submit a PR.

If you build something cool with this knowledge base, share it — tag [@ravibhuma](https://github.com/ravibhuma) on GitHub or [Ravi Bhuma](https://medium.com/@ravishankerb) on Medium.

---

## Companion Resources

- [📖 Browse the Wiki online](https://ravibhuma.github.io/oac-knowledge-graph/)
- [📂 GitHub Repo](https://github.com/ravibhuma/oac-knowledge-graph)
- [🤖 OAC Prompt Studio](https://ravi-bhuma.github.io/oac-prompt-studio/) — for building OAC AI Agents
- [✍️ Building Effective OAC AI Agents](https://medium.com/@ravishankerb/building-effective-oac-ai-agents-the-framework-the-techniques-and-the-resource-hub-to-get-you-eba3797ca991) — Medium article on the R.T.C.C.O.E framework
