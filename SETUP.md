# Setup Guide — Build & Share Your OAC Knowledge Graph

Step-by-step instructions to publish this knowledge base in three places:

1. **GitHub repo** (source code, anyone can clone)
2. **GitHub Pages** (browsable website with search)
3. **Claude Project** (shared AI Q&A)

Total time: ~2 hours. Total cost: $0.

---

## PART 1 — GitHub Repo (30 min)

### 1.1 Create GitHub Account (skip if you have one)
- Go to https://github.com/signup
- Create account with username — this becomes part of your URLs
- Recommended: use the same `RaviBhuma` brand or a related one

### 1.2 Create the Repository on GitHub
1. Sign in to GitHub
2. Click **+** (top right) → **New repository**
3. Fill in:
   - **Repository name**: `oac-second-brain`
   - **Description**: `Comprehensive AI-maintained knowledge base for Oracle Analytics Cloud — 29 wiki pages + searchable Oracle PDFs`
   - **Visibility**: ✅ **Public**
   - ❌ Do NOT initialize with README/license/.gitignore (we already have them)
4. Click **Create repository**
5. GitHub shows a setup page — **leave that tab open**, you'll need the URL

### 1.3 Push Your Local Folder to GitHub

Open **Git Bash** (or terminal) and run these commands one at a time:

```bash
# Navigate to the folder
cd "/c/Users/RaviBhuma/Downloads/OAC-SecondBrain"

# Initialize git
git init -b main

# Configure git identity (first time only)
git config user.name "Ravi Bhuma"
git config user.email "ravi.bhuma@gmail.com"

# Stage all files
git add .

# First commit
git commit -m "Initial commit: OAC Knowledge Graph — 29 wiki pages + 9 Oracle PDFs"

# Connect to your new GitHub repo (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/oac-second-brain.git

# Push
git push -u origin main
```

**Authentication**: GitHub will prompt for credentials.
- Username: your GitHub username
- Password: a **Personal Access Token** (not your account password)
  - Create at: https://github.com/settings/tokens → Generate new token (classic) → check `repo` scope
  - Copy and paste it as the password

### 1.4 Verify on GitHub
- Refresh your repo page on github.com
- You should see all files: `wiki/`, `raw/`, `README.md`, etc.
- The README displays automatically as the homepage

### 1.5 Add Topics for Discoverability
On your repo page:
1. Click the **gear icon** next to "About" (right sidebar)
2. Add topics: `oracle-analytics-cloud`, `oac`, `obiee`, `claude`, `llm-wiki`, `knowledge-base`, `obsidian`, `business-intelligence`, `ai-agents`
3. Save

---

## PART 2 — GitHub Pages (45 min)

GitHub Pages will host a beautiful searchable website built automatically from your wiki using **MkDocs Material**.

### 2.1 Enable GitHub Pages

1. On your repo page, click **Settings** tab
2. In left sidebar: **Pages**
3. Under **Build and deployment**:
   - **Source**: select **GitHub Actions**
4. Save

### 2.2 Update mkdocs.yml With Your Username

The `mkdocs.yml` file currently has placeholder URLs. Edit it:

```bash
# In your local folder
# Open mkdocs.yml and replace 'ravi-bhuma' with your actual GitHub username
# Lines to update:
#   site_url: https://YOUR-USERNAME.github.io/oac-second-brain/
#   repo_url: https://github.com/YOUR-USERNAME/oac-second-brain
#   repo_name: YOUR-USERNAME/oac-second-brain
#   social link: https://github.com/YOUR-USERNAME
```

Or just ask Claude Code: *"Update mkdocs.yml with my GitHub username `<your-username>`"*

### 2.3 Push the Updated Config

```bash
git add mkdocs.yml
git commit -m "Update mkdocs.yml with GitHub username"
git push
```

### 2.4 Watch the Build
1. Go to your repo on GitHub
2. Click the **Actions** tab
3. You'll see a workflow running called **Deploy MkDocs site to Pages**
4. Wait ~2-3 minutes for it to complete (green checkmark)

### 2.5 Visit Your Site
Once the workflow completes:
- URL: `https://YOUR-USERNAME.github.io/oac-second-brain/`
- Browse with sidebar nav, search any topic, dark mode toggle

### 2.6 Common Issues
- **404 on first visit**: Wait another 2-3 minutes; first deploy can be slow
- **Workflow fails on `[[wiki links]]`**: The `roamlinks` plugin handles them; if it fails, edit and remove from `mkdocs.yml` plugins list
- **Pages settings show "Source: Branch"**: Change to "GitHub Actions" as in 2.1

---

## PART 3 — Claude Project (30 min)

This makes the brain **AI-queryable for anyone with a Claude.ai account**.

### 3.1 Sign Up / Sign In to Claude.ai
- Go to https://claude.ai
- Free tier works for testing; **Pro tier** ($20/month) recommended for shareable Projects with full features

### 3.2 Create a New Project

1. Sign in to claude.ai
2. Click **Projects** in the left sidebar
3. Click **Create Project**
4. Name it: **OAC Knowledge Graph**
5. Description: `AI-powered Q&A for Oracle Analytics Cloud — 29 wiki pages + Oracle PDFs as knowledge base`

### 3.3 Add Custom Instructions

1. In your new Project, click **Set custom instructions** (or the ⚙️ icon)
2. Open the file `PROJECT_INSTRUCTIONS.md` from this repo
3. **Copy the entire contents** (the section starting with "You are the OAC Knowledge Graph...")
4. **Paste** into the Custom Instructions field
5. Save

### 3.4 Upload Knowledge Files

> **Note on Knowledge Limits**:
> - Free tier: limited project knowledge size
> - Pro tier: 200K tokens of project knowledge
> - All 29 wiki pages = ~150-200K tokens (fits Pro tier)
> - The 6.8MB of PDF text exceeds the limit — start with wiki only

**Step 1: Add the wiki**
- In Project → **Add Content** → **Upload from computer**
- Navigate to: `C:\Users\RaviBhuma\Downloads\OAC-SecondBrain\wiki\`
- Select **all 29 .md files** (Ctrl+A in the file picker)
- Upload

**Step 2: Add the index files**
- Upload: `index.md`, `CLAUDE.md`, `README.md`

**Step 3: (Optional) Add specific PDFs**
- If room remains in your project knowledge budget, add the most-asked-about PDFs:
  - `getting-started-oracle-analytics-cloud.pdf` (small)
  - `building-semantic-models-oracle-analytics-cloud.pdf` (most-asked topic)
  - `OAC_REST_API_Guide.pdf` (developer reference)
- For the rest of the PDFs, users can attach them per-conversation if needed

### 3.5 Test the Project

In a new conversation within the Project, ask:
- *"What's the R.T.C.C.O.E framework for building OAC AI Agents?"*
- *"How do I configure row-level security in OAC?"*
- *"Walk me through the three layers of the Semantic Model"*

Verify Claude is citing your wiki pages in answers.

### 3.6 Share the Project

1. In your Project, click the **Share** button (top right)
2. Choose share mode:
   - **Anyone with the link can use** (recommended for community)
   - **Only specific people** (for team)
3. Copy the share link
4. Update your README.md with the link:
   ```markdown
   ### 💬 2. Ask Questions (Claude Project)
   > **`https://claude.ai/project/<your-actual-link>`**
   ```
5. Commit and push:
   ```bash
   git add README.md
   git commit -m "Add Claude Project share link"
   git push
   ```

> **Note**: Sharing a Claude Project with knowledge files requires **Pro or Team tier**. On the free tier, you can use the project yourself but not share publicly.

---

## PART 4 — Tell the World

Now that everything's live, promote it:

### 4.1 Update Your GitHub Profile
- Pin the repo on your profile so visitors see it first
- Add it to your bio links

### 4.2 Share on Social
**Twitter/X**:
> 🧠 Just open-sourced an OAC Knowledge Graph — comprehensive AI-maintained knowledge base for Oracle Analytics Cloud.
>
> ✅ 29 cross-linked wiki pages
> ✅ 9 Oracle PDFs as deep reference
> ✅ AI Q&A via Claude Project
> ✅ Browsable docs site
>
> Built on @karpathy's LLM Wiki pattern.
>
> 🔗 [your-github-pages-url]

**LinkedIn**: similar with longer-form context about the Karpathy pattern and OAC.

**Medium**: write a follow-up to your AI Agents article showing how this brain extends the framework to all of OAC.

### 4.3 Submit to Communities
- **Oracle Analytics Community** forum: post in resources/tools section
- **r/OracleBI** subreddit
- **Awesome lists**: submit to relevant awesome-* repos on GitHub
- **Hacker News**: Show HN post

### 4.4 Continuously Improve
- Tag the first release: `git tag v1.0.0 && git push --tags`
- Watch GitHub Issues for community feedback
- Add new sources monthly (Oracle ships features monthly)
- Re-ingest after each Oracle docs update

---

## Maintenance Workflow

### When Oracle releases new features (monthly)
1. Download updated PDFs to `raw/pdfs/`
2. Re-run pdftotext: `cd raw/pdfs && for f in *.pdf; do pdftotext -layout "$f" "${f%.pdf}.txt"; done`
3. Open Claude Code: *"Lint the wiki against the new PDFs"*
4. Claude updates wiki pages
5. Commit + push: GitHub Actions auto-rebuilds the Pages site
6. Re-upload modified wiki files to Claude Project

### When users open issues / PRs
- Each issue is a signal of a coverage gap
- Fix → commit → auto-deploys

---

## Troubleshooting

### Git asks for credentials repeatedly
Set up credential caching:
```bash
git config --global credential.helper manager-core
```

### Push fails with "non-fast-forward"
Pull first:
```bash
git pull --rebase origin main
git push
```

### GitHub Pages workflow fails
- Check **Actions** tab → click the failed run → read the logs
- Most common: `mkdocs.yml` has a typo, or a wiki file path doesn't match `nav:` exactly
- Test locally first:
  ```bash
  pip install mkdocs-material mkdocs-awesome-pages-plugin mkdocs-roamlinks-plugin
  mkdocs serve
  ```

### Claude Project rejects upload (file too large)
- Project knowledge has size limits
- Start with the wiki .md files (small, structured)
- Add PDFs selectively
- For full PDF Q&A, users on the free path can use Claude Code locally

---

## Done!

You now have:
- ✅ A public GitHub repo
- ✅ A beautiful searchable website
- ✅ A shareable AI Q&A project

Anyone in the world can now learn OAC by browsing your site or asking your Claude Project. 🎉
