# OAC MCP Server

> **Last updated:** 2026-04-27
> **Tags:** MCP, Model Context Protocol, Claude, Cline, GitHub Copilot, n8n, LangChain, external AI, LSQL

## Summary
The Oracle Analytics Cloud MCP Server implements the open **Model Context Protocol** standard, enabling external AI clients (Claude Desktop, Claude Code, Cline, GitHub Copilot, n8n, LangChain) to query OAC data through governed conversational interfaces. It bridges enterprise analytics with the broader AI ecosystem while maintaining row-level security, role-based access, and semantic model governance.

> Source: Oracle Analytics Blog, *OAC MCP Server: Bridging Enterprise Analytics and AI*

---

## What MCP Solves

**Inside OAC** — the AI Assistant gives conversational analytics in OAC's UI.
**Outside OAC** — the MCP Server lets *external* AI agents query OAC data from anywhere.

```
External AI Client (Claude / Cline / Copilot / n8n / LangChain)
                    ↓
         MCP Server (OAC-hosted)
                    ↓
            ┌──────────────┐
            │  OAC Engine  │ ← governance, RLS, semantic model
            └──────────────┘
                    ↓
         Subject Areas / Datasets
```

---

## The Three Core Tools

The MCP Server exposes exactly three governed operations:

| Tool | Function | Purpose |
|---|---|---|
| `oracle_analytics-discoverData` | List datasets and Subject Areas | Find what data exists |
| `oracle_analytics-describeData` | Get column-level metadata for a Subject Area or dataset | Understand structure |
| `oracle_analytics-executeLogicalSQL` | Run a Logical SQL query | Get answers |

Plus a **Logical SQL Grammar Reference** resource that helps the AI client construct valid queries.

---

## The Discover → Describe → Execute Workflow

The standard interaction pattern:

```
1. DISCOVER
   AI: "What datasets are available?"
   → Server returns subject areas + datasets list

2. DESCRIBE
   AI: "Tell me about Sales Overview"
   → Server returns columns, types, measures, hierarchies

3. EXECUTE
   AI: "Show total revenue by region for 2024"
   → AI generates Logical SQL
   → Server validates + executes
   → Returns rows (governed by RLS, roles)
```

This three-step flow ensures the AI has correct schema knowledge before generating queries — drastically reducing hallucinated columns or invalid joins.

---

## Supported AI Clients

| Client | Type |
|---|---|
| **Claude Desktop** | Anthropic's desktop app |
| **Claude Code** | Anthropic's CLI / IDE agent |
| **Cline** | VS Code extension |
| **GitHub Copilot** | Microsoft's coding assistant |
| **n8n** | Automation platform |
| **LangChain** | Python AI framework |
| Any MCP-compliant client | Open protocol |

---

## Authentication Methods

### Method 1: Browser-Based (Recommended)
- First-time use: a browser window opens
- Sign in with OCI / IDCS credentials
- Tokens are cached locally
- Auto-refresh on expiration

### Method 2: Token-Based (For Automation)
- Pre-configured OAuth tokens stored in `tokens.json`
- Best for scheduled/headless workflows
- Auto-refresh of access tokens
- Refresh token must be valid

---

## Installation (15-20 Minutes)

### Prerequisites
- An Oracle Analytics Cloud instance with permissions
- **Node.js v18 or higher**
- Windows, macOS, or Linux

### Step 1: Generate Access Tokens
1. Sign in to OAC
2. Click your **Profile** (top-right)
3. **Access Tokens** section
4. Generate token → download `tokens.json`

### Step 2: Download MCP Connect Package
1. OAC Profile → **MCP Connect** section
2. Download the ZIP
3. Extract — contains:
   - `oac-mcp-connect.js` — Node.js MCP server implementation
   - Configuration template
   - README
   - Dependency libraries

### Step 3: Install Node.js
- Download from [nodejs.org](https://nodejs.org) (LTS recommended)
- Verify:
  ```bash
  node -v  # should be ≥ v18
  npm -v
  ```

### Step 4: Configure Your AI Client

#### For Claude Desktop

Edit the config file:
- **Windows**: `C:\Users\<username>\AppData\Roaming\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "oac": {
      "command": "node",
      "args": [
        "C:\\path\\to\\oac-mcp-connect.js"
      ],
      "env": {
        "OAC_INSTANCE_URL": "https://<instance>.analytics.ocp.oraclecloud.com",
        "TOKENS_PATH": "C:\\path\\to\\tokens.json"
      }
    }
  }
}
```

#### For Claude Code

Edit `~/.claude.json` or per-project settings:
```json
{
  "mcpServers": {
    "oac": {
      "command": "node",
      "args": ["/path/to/oac-mcp-connect.js"],
      "env": {
        "OAC_INSTANCE_URL": "https://<instance>...",
        "TOKENS_PATH": "/path/to/tokens.json"
      }
    }
  }
}
```

### Step 5: Restart and Verify
1. Quit Claude Desktop / Claude Code completely
2. Reopen
3. Verify all three tools appear:
   - `oracle_analytics-discoverData` ✓ Connected
   - `oracle_analytics-describeData` ✓ Connected
   - `oracle_analytics-executeLogicalSQL` ✓ Connected

---

## Example Conversations

### "What datasets are available in my OAC environment?"
→ Triggers **Discover** → returns:
```
Subject Areas: Sales Overview, HR Analytics, Finance
Datasets: Marketing Campaign Data (XSA), Customer Survey Q1
```

### "Describe the Sales Overview dataset"
→ Triggers **Describe** → returns:
```
Subject Area: Sales Overview
Tables:
  - Time: Year, Quarter, Month, Date
  - Product: Category, Subcategory, Product Name
  - Customer: Region, Country, Segment
  - Facts: Revenue (SUM), Units (SUM), Cost (SUM)
Hierarchies: Time (Year > Quarter > Month), Product (Category > Subcategory > Product)
```

### "Show total revenue by region for 2024"
→ Triggers **Execute** with generated LSQL:
```sql
SELECT 
  "Sales Overview"."Customer"."Region",
  "Sales Overview"."Facts"."Revenue"
FROM "Sales Overview"
WHERE "Sales Overview"."Time"."Year" = 2024
ORDER BY "Sales Overview"."Facts"."Revenue" DESC
FETCH FIRST 100 ROWS ONLY
```
→ Returns rows respecting the user's RLS

---

## Why MCP Beats Generic LLM + Database Connection

| Without MCP (LLM + DB direct) | With OAC MCP Server |
|---|---|
| LLM writes raw SQL — error-prone | LLM writes Logical SQL on Subject Areas — robust |
| Joins must be specified manually | BI Server resolves joins automatically |
| No RLS / governance | Full RLS + role-based security enforced |
| LLM might hallucinate columns | Schema retrieved via `describeData` first |
| Complex multi-source federation | Subject Area pre-federates |
| Aggregation logic exposed to LLM | BI Server handles measure aggregation |

---

## Security Considerations

> ⚠️ **Critical:** Once data leaves OAC and reaches the external AI client, OAC governance no longer applies. The data becomes subject to the *client's* data handling.

### Best Practices for Sensitive Data
- Use **enterprise LLMs with zero-retention policies** (Anthropic Enterprise, Azure OpenAI Enterprise)
- Deploy **local or OCI-hosted LLMs** (no third-party data egress)
- Work with **aggregated/masked datasets** for AI consumption
- Apply **column-level security** at the Subject Area level
- Align with organizational **compliance standards** (HIPAA, GDPR, SOC2)

### What OAC Still Enforces
- Authentication (only authenticated users can connect)
- Row-level security (filter rows the user shouldn't see)
- Object-level permissions (Subject Area access)
- Query logging (every LSQL execution is logged)

---

## With vs Without Semantic Model

| With Semantic Model (RPD) | Without (XSA datasets only) |
|---|---|
| Trusted business abstraction | Direct dataset access |
| Consistent metric definitions | Per-dataset measures |
| Pre-defined joins | User must understand structure |
| Standardized hierarchies | Ad-hoc structures |
| **Recommended for governed AI** | OK for self-service |

---

## Use Cases

### Conversational BI in Slack/Teams
- LangChain agent hooked to OAC MCP Server
- Slack bot answers "What's our pipeline coverage this quarter?" with a chart

### Automated Insights Generation
- n8n workflow runs daily
- Queries OAC for KPI changes
- Sends summary to email/Slack

### Embedded AI in Custom App
- Custom app uses LangChain + OAC MCP
- Users ask questions in app context
- Real-time governed answers

### Code Generation Aware of Your Data
- GitHub Copilot uses MCP to know your real schema
- Generates correct SQL in Python/Java code
- No more hallucinated column names

---

## Troubleshooting

| Issue | Fix |
|---|---|
| Tools show "Disconnected" | Restart Claude/client; verify Node.js installed; check tokens.json path |
| "Authentication failed" | Tokens expired — regenerate from OAC profile |
| "No datasets returned" | User has no permissions; check OAC role assignments |
| LSQL syntax errors | Use `describeData` first; reference Logical SQL Grammar resource |
| Slow queries | Same DB tuning rules apply — check physical SQL in nqquery.log |

---

## Related
- [OAC AI Agents](OAC%20AI%20Agents.md){ .wikilink }
- [OAC AI Ecosystem](OAC%20AI%20Ecosystem.md){ .wikilink }
- [APIs, Embedding & Integration](APIs%2C%20Embedding%20%26%20Integration.md){ .wikilink }
- [Logical SQL Reference](Logical%20SQL%20Reference.md){ .wikilink }
- [Subject Areas & Datasets](Subject%20Areas%20%26%20Datasets.md){ .wikilink }
- [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }
