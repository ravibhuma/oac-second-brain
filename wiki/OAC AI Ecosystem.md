# OAC AI Ecosystem

> **Last updated:** 2026-04-27
> **Tags:** AI ecosystem, AI Assistant, AI Agents, MCP Server, generative AI, OCI Generative AI, conversational analytics, augmented analytics


📖 **Full Oracle Documentation**: [Oracle Analytics Blog — AI Ecosystem](https://blogs.oracle.com/analytics/the-oracle-analytics-cloud-ai-ecosystem-shaping-the-future-of-enterprise-analytics) · [Visualizing Data — AI Assistant](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/)

## Summary
OAC's AI ecosystem is a layered stack: **augmented analytics** built into the product (Explain, Auto Insights, NLQ), **generative AI** via OCI Generative AI integration (AI Assistant in homepage, workbook, mobile), **AI Agents** for domain-specialized conversational experiences, and the **MCP Server** for external AI client integration. Together they shift OAC from a "platform you navigate" to "analytics you talk to."

> Source: Oracle Analytics Blog, *The Oracle Analytics Cloud AI Ecosystem* + product documentation

---

## The Stack — Five Layers of AI in OAC

```
┌─────────────────────────────────────────────────┐
│  LAYER 5: External AI Integration               │
│  → MCP Server: Claude / Cline / Copilot / n8n   │
├─────────────────────────────────────────────────┤
│  LAYER 4: AI Agents (Domain Specialists)        │
│  → Bound to dataset + RAG knowledge docs + SI   │
├─────────────────────────────────────────────────┤
│  LAYER 3: AI Assistant (Generative)             │
│  → Homepage / Workbook / Mobile conversational  │
├─────────────────────────────────────────────────┤
│  LAYER 2: NLQ + Augmented Analytics             │
│  → Ask, Explain, Auto Insights                  │
├─────────────────────────────────────────────────┤
│  LAYER 1: Built-in ML & OCI AI Services         │
│  → OML, Vision, Language, Forecasting           │
└─────────────────────────────────────────────────┘
```

---

## Layer 1: Built-in ML & OCI AI Services

The foundation — predictive and descriptive analytics.

### Oracle Machine Learning (OML)
- Train models in Data Flows
- Regression, classification, clustering
- Score data with `Apply Model` step

### OCI AI Services Integration
| Service | Capability |
|---|---|
| OCI AI Vision | Image classification, object detection |
| OCI AI Language | Sentiment, entities, key phrases |
| OCI AI Forecasting | Time-series prediction |
| OCI AI Document Understanding | OCR, table extraction |
| OCI Anomaly Detection | Multivariate outlier detection |

See [Machine Learning & AI Features](Machine%20Learning%20%26%20AI%20Features.md){ .wikilink }.

---

## Layer 2: NLQ + Augmented Analytics

Quick-win AI features built into Workbooks.

### Ask (Natural Language Query)
Type a question in the Workbook → get a visualization.
> *"Top 10 products by revenue last quarter"*

### Explain
Right-click a measure → Explain.

- Basic facts, key drivers, segments, anomalies
- One-click adoption of insights into canvas

### Auto Insights
Proactive insights surfaced when you open a Workbook:

- Significant changes
- Correlations
- Outliers

See [Workbooks & Visualizations](Workbooks%20%26%20Visualizations.md){ .wikilink } and [Machine Learning & AI Features](Machine%20Learning%20%26%20AI%20Features.md){ .wikilink }.

---

## Layer 3: AI Assistant (Three Modes)

Conversational AI built into OAC's UI, powered by **OCI Generative AI**.

### Homepage AI Assistant
- Start your day with a question, not a dashboard
- *"Build me an executive profitability dashboard"* → generates a workbook
- Search catalog + answer with public/internal knowledge

### Workbook AI Assistant
- In-canvas conversational partner
- Iteratively refine visualizations
- *"Add a trend line"* / *"Compare to last year"* / *"Filter to enterprise customers"*
- Smart follow-up question handling

### Mobile AI Assistant
- Voice input on phone/tablet
- Podcast-style audio narration of insights
- Hands-free analytics for executives

### Capabilities Across Modes
- Context-aware dialogue (remembers previous turns)
- Smart semantic search (catalog + public knowledge)
- Role-based access enforcement
- User feedback loop for continuous improvement

---

## Layer 4: AI Agents (Domain Specialists)

A step beyond assistants — dataset-specific, RAG-enabled, domain-tuned.

**Difference from AI Assistant**:
- Bound to one dataset (governed scope)
- Customized with **Supplemental Instructions** (R.T.C.C.O.E framework)
- Enriched with **Knowledge Documents** (PDFs/TXT) via RAG
- Acts as a domain expert (not a generalist)

**Use cases**:
- Sales Operations Analyst Agent
- HR Compensation Analyst Agent
- Finance FP&A Agent
- Marketing Performance Agent

See [OAC AI Agents](OAC%20AI%20Agents.md){ .wikilink } for full framework.

---

## Layer 5: External AI via MCP Server

Open standard integration for any MCP-compliant AI client.

**Three operations**: Discover → Describe → Execute

**Clients**: Claude Desktop, Claude Code, Cline, GitHub Copilot, n8n, LangChain, plus any MCP-compliant client.

**Use cases**:
- Slack bot answering "What's our quarterly bookings?"
- Custom app with LangChain RAG over OAC data
- IDE coding assistants aware of your real schema
- n8n automation with OAC as a knowledge source

See [OAC MCP Server](OAC%20MCP%20Server.md){ .wikilink }.

---

## Architectural Principle: One Brain, Many Surfaces

All five layers share the same governed foundation:

- The **Semantic Model** (RPD) provides metric consistency
- **Row-level security** applies across all interfaces
- **Roles** control what each user/agent can see
- The **catalog** is the single source of truth

```
                  ┌─ Homepage AI Assistant
                  ├─ Workbook AI Assistant
   GOVERNED       ├─ Mobile AI Assistant
   FOUNDATION ────┼─ Domain AI Agents
                  ├─ MCP Server (external)
                  └─ Built-in NLQ / Explain / Auto Insights
```

This means: a metric defined once in the Semantic Model → consistent answers across every AI interface.

---

## Choosing the Right AI Surface

| User Need | Recommended Surface |
|---|---|
| Casual Q&A while in OAC | AI Assistant (Workbook) |
| Build a new dashboard from scratch | AI Assistant (Homepage) |
| Mobile / voice / on-the-go | AI Assistant (Mobile) |
| Domain expert experience for a specific team | AI Agent |
| Bring OAC data into a custom app or workflow | MCP Server |
| Quick insight on a metric | Explain (right-click) |
| Open Workbook insights | Auto Insights |
| Predict future values | OML / OCI AI Forecasting |
| Apply a trained model to new data | Data Flow Apply Model |

---

## Strategic Direction (Per Oracle's Roadmap)

The ecosystem is moving from **"navigate to insight"** → **"talk to your data"**:

> *"Analytics is no longer something users navigate. It's something they talk to."*

Key trends:

- AI Assistant becoming the default entry point
- Domain Agents proliferating (each business area has its own)
- MCP Server enabling embedded analytics in any app
- Voice-first mobile experiences
- Generative AI reducing time from question to insight

---

## Adoption Roadmap (Recommended)

For organizations adopting OAC's AI capabilities:

**Phase 1 — Foundation (Month 1-2)**
- Solidify Semantic Model (consistent metrics)
- Index key datasets for AI Assistant
- Train users on Explain and Ask

**Phase 2 — AI Assistant (Month 2-3)**
- Roll out AI Assistant to power users
- Collect feedback on common queries
- Refine Subject Area metadata for AI

**Phase 3 — Domain Agents (Month 3-6)**
- Identify 3-5 high-value domains (Sales, Finance, HR)
- Build agents using R.T.C.C.O.E framework
- Iterate Supplemental Instructions weekly based on user feedback

**Phase 4 — MCP & Integration (Month 6+)**
- Set up MCP Server
- Pilot with one external use case (Slack bot, custom app)
- Expand to additional automations

---

## Governance Across the Ecosystem

A governance checklist that applies to ALL AI surfaces:

- [ ] Semantic Model defines KPIs consistently
- [ ] RLS rules cover all sensitive data
- [ ] AI Assistant indexed datasets reviewed for sensitive columns
- [ ] AI Agent SI includes "do not fabricate" constraint
- [ ] MCP Server users use enterprise LLMs (zero retention)
- [ ] Audit logs reviewed for unusual queries
- [ ] User feedback loop active for AI improvements

---

## Related
- [OAC AI Agents](OAC%20AI%20Agents.md){ .wikilink }
- [OAC MCP Server](OAC%20MCP%20Server.md){ .wikilink }
- [Machine Learning & AI Features](Machine%20Learning%20%26%20AI%20Features.md){ .wikilink }
- [Workbooks & Visualizations](Workbooks%20%26%20Visualizations.md){ .wikilink }
- [Mobile (Oracle Analytics App)](Mobile%20%28Oracle%20Analytics%20App%29.md){ .wikilink }
- [Semantic Model](Semantic%20Model.md){ .wikilink }
- [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }
