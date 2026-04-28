# OpenAI Codex Setup — Ask AI Questions About OAC

> Set up OpenAI Codex in 10 minutes. Then ask any OAC question and get cited answers from this knowledge base.

OpenAI Codex is OpenAI's open-source coding agent — equivalent to Claude Code. It can run locally (CLI) or in the cloud (ChatGPT Codex).

**Two ways to use it with this repo:**
1. **Codex CLI** (local, recommended) — runs in your terminal
2. **ChatGPT Codex** (cloud) — connects to your GitHub repo, runs in browser

---

## Option 1 — Codex CLI (Local, Recommended)

### What You'll Get

After setup, ask in your terminal:
```
> How do I configure row-level security in OAC?
> What's the R.T.C.C.O.E framework for AI Agents?
> Walk me through the three-layer Semantic Model
```

Codex reads the entire knowledge base (30+ wiki pages + 9 Oracle PDFs) and answers with citations.

---

### Prerequisites

| Requirement | Check |
|---|---|
| **OS** | Windows 10+, macOS, or Linux |
| **Node.js** | v18 or higher — [Download here](https://nodejs.org/) (LTS) |
| **Git** | [Download here](https://git-scm.com/downloads) |
| **OpenAI account** | [Sign up](https://platform.openai.com/signup) |

Verify Node.js + Git:
```bash
node --version    # v18.x.x or higher
git --version     # 2.x.x
```

---

### Step 1 — Install Codex CLI

```bash
npm install -g @openai/codex
```

Or on macOS via Homebrew:
```bash
brew install codex
```

Verify:
```bash
codex --version
```

> 💡 If you get a permission error on Mac/Linux, prefix with `sudo`. On Windows, run terminal as administrator.

---

### Step 2 — Authenticate

Codex supports two auth methods. Pick one.

#### Method A: Sign In With ChatGPT (Easiest)

If you have **ChatGPT Plus, Pro, or Team** ($20+/mo):

```bash
codex
```

On first run it opens a browser → sign in to ChatGPT → authorize Codex CLI. Done. Codex usage is included in your ChatGPT subscription.

#### Method B: API Key (Pay-as-you-go)

If you prefer pay-per-use without ChatGPT subscription:

1. Get a key at https://platform.openai.com/api-keys
2. Set the env var:

**Windows (CMD):**
```cmd
setx OPENAI_API_KEY "sk-...your-key..."
```

**Mac/Linux:**
```bash
echo 'export OPENAI_API_KEY="sk-...your-key..."' >> ~/.zshrc
source ~/.zshrc
```

Restart your terminal. Codex will use the API key automatically.

---

### Step 3 — Clone The Repo

```bash
cd C:\Users\YourName\Documents          # Windows
# or
cd ~/Documents                          # Mac/Linux

git clone https://github.com/ravibhuma/oac-second-brain.git
cd oac-second-brain
```

---

### Step 4 — Start Codex

From inside the `oac-second-brain` folder:

```bash
codex
```

You'll see a prompt. Type your question:

```
> How do I configure row-level security in OAC?
```

Codex will:
1. **Read the directory structure** to understand what's there
2. **Search wiki/ + raw/** for relevant content
3. **Open matching files**
4. **Answer with citations**

---

### Step 5 — Useful Codex Commands

| Command | What it does |
|---|---|
| `/help` | List all built-in commands |
| `/clear` | Reset conversation |
| `/exit` or `Ctrl+C` twice | Quit |
| `/model gpt-5-codex` | Switch model (default is good) |

---

### Quick One-Off Questions (No Interactive Mode)

You can also ask without entering interactive mode:

```bash
codex "How do I set up row-level security in OAC?"
```

Codex answers and exits.

---

## Option 2 — ChatGPT Codex (Cloud, In Browser)

If you don't want to install anything locally, you can use **ChatGPT Codex** — a cloud agent inside ChatGPT that connects directly to your GitHub repo.

### Prerequisites
- **ChatGPT Plus, Pro, or Team** subscription
- GitHub account

### Setup Steps

1. Sign in to https://chatgpt.com
2. Click **Codex** in the left sidebar
3. **Connect GitHub** → authorize the OpenAI Codex GitHub App
4. Select the repo: `ravibhuma/oac-second-brain` (or fork it first to your account)
5. Codex creates a sandboxed environment with the repo
6. Ask questions in the chat:
   ```
   How do I configure row-level security in OAC?
   ```

### Pros / Cons vs CLI

| Aspect | Codex CLI (local) | ChatGPT Codex (cloud) |
|---|---|---|
| Install | Required | None |
| Cost | API or ChatGPT plan | ChatGPT Plus+ required |
| Speed | Fast (local) | Slightly slower (cloud) |
| Privacy | Files stay local | Files in OpenAI sandbox |
| Best for | Power users, frequent use | Casual exploration, no install |

---

## Tips For Best Results

### Be specific
❌ *"Tell me about security"*
✅ *"How do I set up data filters in a Subject Area for region-based RLS?"*

### Reference paths to focus the answer
✅ *"Read wiki/Semantic Model.md and explain LTS fragmentation"*

### Ask follow-ups
```
> Now show me the init block SQL
> What if I'm using Autonomous Database?
> Compare this to OBIEE 11g
```

### Ask for specific formats
✅ *"Give me a comparison table"*
✅ *"Show me the SQL with comments explaining each line"*
✅ *"List the steps numbered with exact UI labels"*

---

## Troubleshooting

### `codex: command not found`
Node.js install didn't add npm globals to PATH. Fix:
- Close and reopen terminal
- On Windows: log out and back in
- Or reinstall Node.js with LTS installer

### `EACCES: permission denied` on Mac/Linux
```bash
sudo npm install -g @openai/codex
```

### `OPENAI_API_KEY not set`
Either:
- Sign in with ChatGPT account: just run `codex` → browser auth
- Or set the API key as shown in Step 2 Method B

### Codex says "I can't access those files"
You're running Codex from the wrong directory. Make sure you're inside the repo:
```bash
cd path/to/oac-second-brain
codex
```

### Want to switch from API to ChatGPT auth (or vice versa)?
```bash
codex logout
codex login          # interactive prompt for ChatGPT or API key
```

---

## Cost Comparison

| Auth Method | Cost | Best For |
|---|---|---|
| ChatGPT Plus | $20/mo | Heavy use, also covers ChatGPT |
| ChatGPT Pro | $200/mo | Power users, GPT-5 Pro access |
| API Key (pay-as-you-go) | ~$0.01-0.10/query | Light/predictable use |

Light exploration of this knowledge base typically costs **<$1/month** on API key auth.

Current pricing: https://openai.com/pricing

---

## Updating The Knowledge Base

When the maintainer pushes new content:

```bash
cd oac-second-brain
git pull
```

For ChatGPT Codex (cloud), it auto-syncs with the connected repo.

---

## Codex vs Claude Code — Which Should You Use?

Both work great with this repo. Pick based on preference:

| | Codex (OpenAI) | Claude Code (Anthropic) |
|---|---|---|
| Install | `npm install -g @openai/codex` | `npm install -g @anthropic-ai/claude-code` |
| Free tier | API has free credits | Limited free tier |
| Subscription | ChatGPT Plus $20 | Claude Pro $20 |
| Cloud version | ChatGPT Codex (in chatgpt.com) | claude.ai web app |
| Strengths | Coding + execution | Long-context reasoning, citations |

**You can install both** and try the same question in each — see which gives you better answers for OAC.

---

## Companion Resources

- [📖 Browse the Wiki online](https://ravibhuma.github.io/oac-second-brain/)
- [📂 GitHub Repo](https://github.com/ravibhuma/oac-second-brain)
- [📘 Claude Code Setup](CLAUDE_CODE_SETUP.md) — alternative AI tool
- [🤖 OAC Prompt Studio](https://ravi-bhuma.github.io/oac-prompt-studio/) — for building OAC AI Agents

---

## Next Steps

✅ **You're set up.** Ask anything OAC-related.

If you find gaps or errors, [open a GitHub issue](https://github.com/ravibhuma/oac-second-brain/issues) or submit a PR.
