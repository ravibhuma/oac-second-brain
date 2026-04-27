# OAC AI Agents

> **Last updated:** 2026-04-27
> **Tags:** AI agents, conversational analytics, RAG, supplemental instructions, RTCCOE, knowledge documents, prompt engineering

## Summary
OAC AI Agents are domain-specialized conversational interfaces that turn datasets and business knowledge into a "data analyst that talks." Unlike the generic AI Assistant, an Agent is bound to a specific dataset, encoded with custom business rules (Supplemental Instructions), enriched with knowledge documents (RAG), and tuned for a specific business function. The quality gap between a frustrating agent and an expert one comes down to **Supplemental Instructions engineering**.

> Source: Ravi Bhuma, *Building Effective OAC AI Agents* (Medium, 2024-2025) — see `raw/articles/`

---

## What Is an OAC AI Agent?

A conversational AI bound to a dataset, configured to act as a domain expert (Sales analyst, Finance analyst, HR analyst, etc.). Users ask questions in natural language, and the agent generates governed visualizations and insights.

```
User Question (NL)
   ↓
Agent
   ├── Dataset (indexed for AI Assistant)
   ├── Supplemental Instructions (≤ 6000 chars)
   ├── Knowledge Documents (≤ 10 files, 5MB each)
   └── Welcome Message
   ↓
Visualization + Narrative Answer
```

---

## The Four Components

### 1. Dataset (One per Agent)
- Foundation of the agent's data
- Must be **indexed for AI Assistant**:
  - Right-click dataset → **Inspect** → **Search** → **"Index for Assistants"**
- Apply **Agent Filters** to restrict columns/rows for governed access

### 2. Supplemental Instructions (SI)
- Up to **6,000 characters**
- Encodes business logic, terminology, KPI formulas, fiscal calendars, defaults
- THE single biggest quality lever (per Ravi Bhuma's article)

### 3. Knowledge Documents
- Up to **10 files**, **5 MB each**
- PDF or TXT
- RAG-processed for semantic search at query time
- Use for: policies, glossaries, methodology docs, business context

### 4. Welcome Message
- First-impression text shown when user opens the agent
- Include sample questions to set expectations

---

## The R.T.C.C.O.E Framework (Structuring Supplemental Instructions)

This six-section framework maximizes the 6,000-character SI limit with high signal density.

### **R — Role**
Define the agent's persona and domain expertise.
```
You are a Senior Sales Operations Analyst with 15 years of experience in B2B SaaS.
Your expertise: pipeline analysis, forecast accuracy, territory performance, churn risk.
You communicate concisely with executives and dive deep when asked.
```

### **T — Task**
Outline core analytical workflows and responsibilities.
```
Your primary tasks:
1. Answer questions about pipeline, bookings, ARR, and churn
2. Compare performance across regions, segments, and time periods
3. Surface anomalies and recommend follow-up analysis
4. Generate executive-ready visualizations
```

### **C — Context**
Encode business rules, fiscal calendars, KPI formulas, hierarchies.
```
Business Definitions:
- ARR = Annual Recurring Revenue (Sum of contract value / contract length in years × 12)
- ATV = Average Transaction Value = SUM(Revenue) / SUM(Transactions)
- Pipeline coverage = Open Pipeline / (Quota - Closed Won)

Fiscal Calendar:
- Fiscal year starts February 1
- "Current quarter" = quarter that contains today's date in fiscal calendar
- "Last year" = same fiscal period one year prior

Hierarchies:
- Region → Sub-region → Country → State
- Segment: Enterprise > Mid-Market > SMB
```

### **C — Constraints**
Hard rules; what the agent must NOT do.
```
Constraints:
- NEVER fabricate data — if a column is missing, say so
- ALWAYS apply the "Active = Y" filter unless user explicitly asks for inactive
- DEFAULT metric for "performance" = Bookings unless context implies otherwise
- DO NOT show data older than 5 years (older than 2021)
- For PII: never show individual employee names; aggregate to team level
```

### **O — Output**
Specify visualization preferences and response formats.
```
Output Preferences:
- For trends: line chart with 13-month rolling window
- For comparisons: bar chart with target line overlay
- For top-N: horizontal bar chart, max 10 items
- For drill-downs: pivot table with subtotals
- For text answers: 3 sentences max, then visualization
- Include a 1-sentence "What this means" summary after every visualization
```

### **E — Examples**
2-3 few-shot query → response pairs. **The single biggest quality improvement.**
```
Example 1:
User: "How is EMEA doing?"
Agent: Generates a bar chart of EMEA bookings by country, last 4 quarters,
       with quota line. Sentence summary: "EMEA at 87% of YTD quota,
       Germany leading at 112%."

Example 2:
User: "Why did churn go up?"
Agent: Generates churn rate line chart for last 12 months. Decomposes by
       customer segment. Surfaces top 3 churned accounts.

Example 3:
User: "Show me pipeline."
Agent: Defaults to: Pipeline by Stage (funnel chart), filtered to current
       fiscal quarter close date, US region (most common scope).
```

---

## Custom KPI Implementation

Without explicit formulas, agents make assumptions. Always define metrics:

```
KPI Formulas (encode in Context section):
- ATV = SUM(Revenue) / SUM(Transactions)
- Win Rate = COUNT(Closed Won) / COUNT(Closed Opportunities)
- Avg Deal Size = SUM(ACV) / COUNT(Closed Won Deals)
- Pipeline Coverage = SUM(Open Pipeline Amount) / (Quarterly Quota - Closed Won)
```

---

## Geographic / Distance Logic

Teach the agent to interpret coordinates:
```
Geography:
- Latitude/Longitude columns: "store_lat", "store_lon"
- For "stores within X miles of [city]": use Haversine formula
- For "nearby" (no distance specified): default to 25 miles
- Always show as a map visualization for spatial queries
```

---

## Agent Filters (Governed Access)

Apply mandatory filters at the agent level:
- Restrict columns visible to the agent
- Apply WHERE clauses always enforced
- Prevents users asking the agent for unauthorized data

**Example**: Sales Director Agent might have:
- Column subset: exclude `salary`, `bonus_pct`
- Row filter: `region = NQ_SESSION.USER_REGION`

---

## Pre-Deployment Checklist

Before releasing an agent to users:

- [ ] Primary dataset is fully indexed for AI Assistant
- [ ] Agent filters applied for governed access
- [ ] Supplemental Instructions ≤ 6,000 characters
- [ ] SI follows R.T.C.C.O.E structure
- [ ] All KPI formulas explicitly defined
- [ ] Fiscal calendar mappings encoded
- [ ] Knowledge documents reviewed for contradictions
- [ ] Default metrics, aggregations, chart types specified
- [ ] 2-3 concrete few-shot examples in SI
- [ ] Welcome message includes 3-4 sample questions
- [ ] Tested with edge cases (vague queries, ambiguous time references)

---

## Common Failure Modes (Without Good SI)

| Failure | Cause | Fix |
|---|---|---|
| Generic LLM answers | No domain context in SI | Add Role + Context |
| Wrong metric calculation | Assumed aggregation | Define KPI formulas explicitly |
| Wrong time period | Calendar misalignment | Encode fiscal calendar |
| Hallucinated data | No constraint against it | Add "NEVER fabricate" constraint |
| Wrong visualization | No output spec | Define Output preferences |
| User confusion on first use | No welcome guidance | Welcome message with samples |

---

## AI Agent vs AI Assistant vs MCP Server

| | AI Assistant | AI Agent | MCP Server |
|---|---|---|---|
| Where it lives | Inside OAC UI | Inside OAC UI | External (Claude, Cline, etc.) |
| Scope | All user data | Single dataset, domain-tuned | All datasets/SAs (governed) |
| Customization | Limited | Full SI + RAG docs | None (governed by OAC) |
| Best for | General Q&A | Domain expert experience | External AI workflows |

See [[OAC MCP Server]] and [[OAC AI Ecosystem]].

---

## Resource Hub

The author of the source article maintains an open-source learning platform:

**OAC Prompt Studio**: https://ravi-bhuma.github.io/oac-prompt-studio/
- 11 industry templates
- Interactive SI builder
- 16 SI patterns
- 40 prompt engineering techniques
- 12 hands-on exercises
- 28-question knowledge quiz
- Downloadable PDF guide

---

## Best Practices Summary

> 💡 **Tip:** Start every agent's SI with Role and Examples — the rest can be tuned later. These two alone produce 60% of the quality lift.

> 💡 **Tip:** When SI exceeds 6,000 chars, move details to Knowledge Documents. Use SI for rules, KD for reference.

> 💡 **Tip:** Iterate weekly — collect user queries, review agent responses, refine SI based on failures.

> ⚠️ **Warning:** Without explicit "do not fabricate" constraints, LLMs will invent column values when uncertain. Always include this.

> 💡 **Tip:** Test the agent with 5 different user personas (executive, analyst, novice, skeptic, edge-case asker). The novice queries reveal gaps.

---

## Related
- [[Machine Learning & AI Features]]
- [[OAC MCP Server]]
- [[OAC AI Ecosystem]]
- [[Workbooks & Visualizations]]
- [[Subject Areas & Datasets]]
