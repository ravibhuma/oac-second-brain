# OAC Knowledge Graph — Ingestion Log

## 2026-04-27 — Initial Build
- Created folder structure: `raw/`, `wiki/`, `index.md`, `log.md`, `CLAUDE.md`
- Built 16 foundational wiki pages from Claude knowledge:
  - OAC Overview & Architecture
  - Data Sources & Connections
  - Semantic Model
  - Subject Areas & Datasets
  - Workbooks & Visualizations
  - Classic Dashboards & Analyses
  - BI Publisher
  - Data Flows & Data Preparation
  - Machine Learning & AI Features
  - Security & Row-Level Security
  - Administration & Service Console
  - Logical SQL Reference
  - APIs, Embedding & Integration
  - KPIs, Alerts & Notifications
  - Migration, Snapshots & Lifecycle
  - OAC vs OBIEE vs OAS Comparison

## 2026-04-27 — Coverage Expansion (Round 2)
Added 8 wiki pages to align with full Oracle docs structure:
- Whats New & Release Updates
- FAQs & Troubleshooting
- Consumer Guide (Explore)
- Subscribe & Provisioning
- OCI REST APIs & CLI for OAC
- Maps & Geospatial Analytics
- Custom Visualizations & Plug-ins
- Mobile (Oracle Analytics App)

## 2026-04-27 — AI Ecosystem Coverage (Round 3)
Ingested 3 source articles:
- `raw/articles/medium-building-effective-oac-ai-agents.md` (Ravi Bhuma — Medium)
- `raw/articles/oracle-blog-mcp-server.md` (Oracle Analytics Blog)
- `raw/articles/oracle-blog-ai-ecosystem.md` (Oracle Analytics Blog)

Added 4 wiki pages:
- OAC AI Agents (R.T.C.C.O.E framework, SI engineering)
- OAC MCP Server (Discover/Describe/Execute, Claude integration)
- OAC AI Ecosystem (master 5-layer overview)
- Tutorials, Solutions & Learning Resources

## 2026-04-27 — Reference Layer
- Created Docs Coverage Matrix mapping every Oracle docs guide → wiki page with status
- Updated index.md with full topic taxonomy
- Added source references for blog and YouTube channel

## 2026-04-27 — PDF Ingestion (Round 4)
User dropped 9 official Oracle Analytics Cloud PDFs into `raw/pdfs/`:
- getting-started-oracle-analytics-cloud.pdf (864KB)
- whats-new-oracle-analytics-cloud.pdf (324KB)
- building-semantic-models-oracle-analytics-cloud.pdf (3.1MB)
- smml-schema-reference-oracle-analytics-cloud.pdf (252KB)
- connecting-oracle-analytics-cloud-your-data.pdf (5.1MB)
- visualizing-data-and-building-reports-oracle-analytics-cloud.pdf (32MB)
- administering-oracle-analytics-cloud-oracle-cloud-infrastructure-gen-2.pdf (8.5MB)
- configuring-oracle-analytics-cloud.pdf (8.3MB)
- OAC_REST_API_Guide.pdf (192KB)

**Conversion**: All 9 PDFs converted to searchable `.txt` files using `pdftotext -layout`.
**Total deep reference text**: ~6.8 MB (~1.5M tokens).

**Strategy decision**: Rather than copy PDF content into wiki pages (token-expensive,
lossy summarization), adopted **grep-at-query-time** pattern:
- Wiki pages = navigation + structure (29 pages)
- Raw .txt files = full deep reference, grep at query time
- CLAUDE.md updated with the two-layer query pattern
- New wiki page: [[Source PDFs Index]] documents this pattern

This aligns with Karpathy's LLM Wiki insight: synthesis happens in the wiki for structure,
sources stay raw and citable for fidelity.

## Verified Working
- Sample grep: "row level security|VPD" → 57 hits across 4 PDFs (50 in Semantic Models guide)
- Sample grep: "event polling" → matches in smml-schema-reference
- The system can now answer any deep OAC question by:
  1. Grepping raw/pdfs/*.txt for keywords
  2. Reading matching sections
  3. Synthesizing with wiki context
  4. Citing both sources
