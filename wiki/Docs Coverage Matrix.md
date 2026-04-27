# Docs Coverage Matrix

> **Last updated:** 2026-04-27
> **Tags:** coverage, mapping, oracle docs, status, gaps

## Summary
Mapping of every official Oracle Analytics Cloud documentation guide → corresponding wiki page(s) → coverage status. Use this to find which wiki page covers a given Oracle doc topic, identify gaps, and prioritize deepening.

> **Authoritative source**: https://docs.oracle.com/en/cloud/paas/analytics-cloud/

---

## Coverage Status Legend

- ✅ **Covered** — wiki page maps directly, comprehensive
- 🟡 **Partial** — wiki page exists, but key sub-topics need deepening
- ❌ **Gap** — no wiki page yet
- 📚 **Reference** — covered as index/links only (e.g., Tutorials)

---

## Mapping Table

| # | Oracle Docs Guide | Wiki Page(s) | Status |
|---|---|---|---|
| 1 | What's New | [[Whats New & Release Updates]] | ✅ |
| 2 | Preview Features | [[Whats New & Release Updates]] | ✅ |
| 3 | FAQs | [[FAQs & Troubleshooting]] | ✅ |
| 4 | Troubleshoot | [[FAQs & Troubleshooting]] | ✅ |
| 5 | Explore (consumers) | [[Consumer Guide (Explore)]] | ✅ |
| 6 | Subscribe and Set Up | [[Subscribe & Provisioning]] | ✅ |
| 7 | Connect to Data | [[Data Sources & Connections]] | ✅ |
| 8 | Visualize Data | [[Workbooks & Visualizations]], [[Maps & Geospatial Analytics]] | ✅ |
| 9 | Build Reports and Dashboards | [[Classic Dashboards & Analyses]] | ✅ |
| 10 | Create Pixel-Perfect Reports | [[BI Publisher]] | 🟡 (deepen layout editor) |
| 11 | Model Data (Semantic Modeler) | [[Semantic Model]] | 🟡 (deepen multi-user dev, multilingual, OLAP) |
| 12 | Administer | [[Administration & Service Console]], [[Subscribe & Provisioning]] | ✅ |
| 13 | Develop | [[APIs, Embedding & Integration]], [[Custom Visualizations & Plug-ins]] | ✅ |
| 14 | Migrate | [[Migration, Snapshots & Lifecycle]] | ✅ |
| 15 | OAC REST APIs (application) | [[APIs, Embedding & Integration]] | 🟡 (full endpoint reference needed) |
| 16 | SOAP APIs | [[APIs, Embedding & Integration]] | 🟡 (deepen SOAP examples) |
| 17 | Publisher Web Services | [[BI Publisher]] | 🟡 |
| 18 | Publisher REST APIs | [[BI Publisher]] | 🟡 |
| 19 | OCI REST APIs (instance mgmt) | [[OCI REST APIs & CLI for OAC]] | ✅ |
| 20 | OCI CLI commands | [[OCI REST APIs & CLI for OAC]] | ✅ |
| 21 | Community | [[Tutorials, Solutions & Learning Resources]] | 📚 |
| 22 | Technical Papers | [[Tutorials, Solutions & Learning Resources]] | 📚 |
| 23 | Solutions | [[Tutorials, Solutions & Learning Resources]] | 📚 |
| 24 | Tutorials | [[Tutorials, Solutions & Learning Resources]] | 📚 |
| 25 | Videos | [[Tutorials, Solutions & Learning Resources]] | 📚 |

---

## Cross-Cutting Topics (Not Single Guides)

| Topic | Wiki Page | Status |
|---|---|---|
| Semantic Model deep concepts | [[Semantic Model]] | 🟡 (deepen with full guide PDF) |
| Logical SQL | [[Logical SQL Reference]] | ✅ |
| Subject Areas vs Datasets | [[Subject Areas & Datasets]] | ✅ |
| Data Flows / ETL | [[Data Flows & Data Preparation]] | ✅ |
| Machine Learning (OML, OCI AI) | [[Machine Learning & AI Features]] | ✅ |
| Security (RLS, IDCS, roles) | [[Security & Row-Level Security]] | ✅ |
| KPIs, Agents, Alerts | [[KPIs, Alerts & Notifications]] | ✅ |
| Maps & Geospatial | [[Maps & Geospatial Analytics]] | ✅ |
| Custom Visualizations | [[Custom Visualizations & Plug-ins]] | ✅ |
| Mobile Apps | [[Mobile (Oracle Analytics App)]] | ✅ |
| OAC vs OBIEE vs OAS | [[OAC vs OBIEE vs OAS Comparison]] | ✅ |

---

## AI Ecosystem Topics (Covered Beyond Oracle Docs)

| Topic | Wiki Page | Source |
|---|---|---|
| AI Assistant (3 modes) | [[OAC AI Ecosystem]] | Oracle blog |
| AI Agents (R.T.C.C.O.E framework) | [[OAC AI Agents]] | Ravi Bhuma Medium article |
| MCP Server (external AI) | [[OAC MCP Server]] | Oracle blog |
| Augmented Analytics (Explain, NLQ) | [[Workbooks & Visualizations]], [[Machine Learning & AI Features]] | Oracle docs |

---

## Gaps Requiring Deepening (Priority Order)

When the user provides Oracle docs PDFs (or asks me to ingest specific guides), these are the priority deepening targets:

### High Priority
1. **Semantic Modeler full guide** (acmdg book)
   - Multi-user development workflow
   - Multidimensional / OLAP sources
   - Multilingual translations
   - Static variables (vs Repository / Session)
   - Consistency check rules
   - Deployment history & rollback

2. **Visualizing Data full guide** (acubi book)
   - Every visualization type — full Grammar Panel reference
   - Every transformation step in Dataset prep
   - Storytelling / Narration deep dive
   - Home page customization
   - AI Assistant configuration details

3. **BI Publisher full guide** (acpub book)
   - Layout Editor full reference
   - eText template syntax
   - PDF form template binding
   - Bursting query patterns by use case
   - Performance tuning (large reports)

### Medium Priority
4. **Develop guide** (acdev book)
   - Full REST API endpoint catalog (every method)
   - SOAP web service operations
   - Data Action types and examples
   - Custom skin/theme development

5. **Administer guide** (acoag book)
   - Mail server full configuration
   - Cache configuration deep dive
   - Performance tuning checklists
   - Audit configuration
   - User session management

### Lower Priority
6. **Migrate guide** (acmig book)
   - OBIA-specific migration paths
   - Specific feature compatibility tables
   - Pre-flight checks

---

## How to Deepen (The Karpathy Way)

To take any 🟡 page → ✅:
1. User downloads the official PDF for that guide from `docs.oracle.com/en/cloud/paas/analytics-cloud/`
2. User saves to `raw/pdfs/<guide-name>.pdf`
3. Ask Claude: *"Ingest the new PDF in raw/pdfs/"*
4. Claude reads the PDF and significantly expands the related wiki page(s) with citations
5. Mark coverage matrix as ✅

This is the canonical Karpathy LLM Wiki workflow — sources curated by human, wiki maintained by LLM, knowledge compounds over time.

---

## Related
- [[index]]
- [[Tutorials, Solutions & Learning Resources]]
- All wiki pages
