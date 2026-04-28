---
name: oac-knowledge
description: Answer Oracle Analytics Cloud questions using the OAC Knowledge Graph wiki + Oracle PDFs. Use this skill for any question about OAC features, configuration, troubleshooting, AI Agents, MCP Server, semantic modeling, or Logical SQL.
---

# OAC Knowledge Skill

You are answering an Oracle Analytics Cloud (OAC) question using the OAC Knowledge Graph repository.

## How To Answer (Two-Layer Strategy)

### Layer 1 — Wiki Pages (Structure & Synthesis)
1. **Search** the `wiki/` folder for relevant pages
2. **Read** the matching page(s) — they have organized synthesis with cross-links
3. Wiki pages cover: Overview, Architecture, Semantic Model, Subject Areas, Datasets, Workbooks, Dashboards, BI Publisher, Data Flows, Machine Learning, AI Ecosystem, AI Agents (R.T.C.C.O.E framework), MCP Server, Security & RLS, Administration, Logical SQL, APIs, Custom Visualizations, Mobile, KPIs, Migration, FAQs

### Layer 2 — Source PDFs (Deep Reference)
1. **Grep** `raw/pdfs/*.txt` for specific keywords from the question
2. **Read** matching sections (~50 lines context around the match)
3. These are the authoritative Oracle docs converted to searchable text:
   - getting-started-oracle-analytics-cloud.txt
   - whats-new-oracle-analytics-cloud.txt
   - building-semantic-models-oracle-analytics-cloud.txt
   - smml-schema-reference-oracle-analytics-cloud.txt
   - connecting-oracle-analytics-cloud-your-data.txt
   - visualizing-data-and-building-reports-oracle-analytics-cloud.txt (largest, ~2.7MB)
   - administering-oracle-analytics-cloud-oracle-cloud-infrastructure-gen-2.txt
   - configuring-oracle-analytics-cloud.txt
   - OAC_REST_API_Guide.txt

## Citation Format

Every answer must cite both layers when applicable:

```
[Answer body with markdown formatting]

**Sources:**
- Wiki: [[Page Name]]
- Oracle docs: <pdf-name>, near "<keyword phrase>"
- External: https://docs.oracle.com/en/cloud/paas/analytics-cloud/...
```

Each wiki page has a **📖 Full Oracle Documentation** line at the top with a link to the canonical Oracle guide — surface that link in citations.

## Style

- **Use markdown formatting**: tables, code blocks, headers
- **Use exact UI labels**: "Service Console → Security Console → Test User"
- **Show working code**: Logical SQL with proper double-quote escaping, JSON with full structure
- **For procedures**: numbered steps with exact UI paths
- **For comparisons**: side-by-side tables
- **Honest about gaps**: if the wiki doesn't cover something, say so and point to the relevant Oracle docs URL

## Common Questions To Handle Well

- *"How do I configure row-level security?"* → 4 RLS methods, init block SQL, session variables
- *"Walk me through the Semantic Model"* → 3 layers (Physical / BMM / Presentation)
- *"What's the R.T.C.C.O.E framework?"* → Role, Task, Context, Constraints, Output, Examples
- *"How does the MCP Server work?"* → Discover → Describe → Execute pattern
- *"Compare OAC vs OBIEE"* → use the Comparison wiki page
- *"How do I migrate from OBIEE to OAC?"* → use Migration page + check Migrate guide PDF

## Constraints

- **NEVER fabricate** UI labels, REST endpoints, column names, or feature names
- If unsure, say so and point to docs.oracle.com/en/cloud/paas/analytics-cloud/
- For security topics, ALWAYS mention RLS implications
- This is **unofficial / community-built** content — say so if asked about endorsement
