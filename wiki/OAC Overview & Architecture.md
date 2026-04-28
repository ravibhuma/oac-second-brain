# OAC Overview & Architecture

> **Last updated:** 2026-04-27
> **Tags:** architecture, overview, platform, editions, components

## Summary
Oracle Analytics Cloud (OAC) is Oracle's cloud-native business intelligence and analytics platform. It delivers self-service data visualization, enterprise reporting, augmented analytics (AI/ML), and semantic modeling in a fully managed SaaS/PaaS service on Oracle Cloud Infrastructure (OCI).

---

## Editions

| Edition | Target | Key Capabilities |
|---|---|---|
| **Enterprise** | Large organizations | Full semantic model, Classic Dashboards, BI Publisher, ML, 4 OCPUs+ |
| **Professional** | Departmental / SMB | Self-service only, Workbooks & Datasets, no RPD modeling, no Publisher |
| **OAC Free** (OAF) | Learning / Dev | Limited OCPUs, full Enterprise features, not for production |

> 💡 **Tip:** Enterprise edition is required if you need Classic Dashboards, BI Publisher reports, or the full Semantic Model (RPD).

---

## Core Components

```
┌─────────────────────────────────────────────────────────┐
│                  OAC Service (OCI)                       │
│                                                          │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────┐  │
│  │  Presentation│  │  BI Server   │  │ BI Publisher   │  │
│  │  Services   │  │ (Query Eng.) │  │ (Reports)      │  │
│  └──────┬──────┘  └──────┬───────┘  └───────┬────────┘  │
│         │                │                   │           │
│  ┌──────▼──────────────────────────────────────────┐    │
│  │              Semantic Model (RPD)                │    │
│  │   Physical Layer → Business Model → Presentation│    │
│  └──────────────────────────┬───────────────────────┘    │
│                             │                            │
│  ┌──────────────────────────▼───────────────────────┐    │
│  │        Data Sources (DB, Files, Cloud, XSA)      │    │
│  └──────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

### Presentation Services
- Web-based UI (browser)
- Hosts Workbooks (self-service), Classic Dashboards, Analyses
- Manages catalog (folders, permissions, favorites)
- Handles user sessions, authentication, and page rendering

### BI Server (Query Engine)
- Core analytical engine
- Translates Logical SQL → physical SQL for any data source
- Manages the Semantic Model (RPD)
- Cache manager, usage tracking, aggregate navigation
- Federated queries across multiple data sources

### BI Publisher (Reporting Engine)
- Pixel-perfect report generation
- Template-based: RTF, XPT, Excel, PDF templates
- Bursting: split reports and deliver by recipient
- Scheduler: time-based and event-based delivery

### Oracle Analytics Data Server
- Columnar in-memory engine
- Accelerates dataset queries (Workbook-style)
- Backs Extended Subject Areas (XSA)

---

## Deployment Architecture

### Fully Managed (Default)
OAC runs entirely on OCI. Oracle manages:
- Patching, upgrades, backups
- High availability and disaster recovery
- Scaling (vertical: OCPU scaling)

### Private Access Channel (PAC)
Connects OAC to private/on-premise data sources without exposing them to the internet.
- Reverse proxy inside customer VCN
- Supports DB, REST, JDBC connections
- See [Data Sources & Connections](Data%20Sources%20%26%20Connections.md){ .wikilink }

### Remote Data Gateway (RDG)
Agent installed on-premise to relay data queries:
- Supports relational databases, files
- Used when PAC is not sufficient or for legacy connectivity

---

## User Roles & Access Layers

| Layer | Who | Tool |
|---|---|---|
| Self-Service Analytics | Business Users | Workbooks, Datasets |
| Enterprise Reporting | Power Users / Analysts | Classic Dashboards, Analyses, Publisher |
| Data Modeling | Data Engineers / Admins | Semantic Model (RPD via Model Administration Tool) |
| Administration | Admins | Service Console, Security Console |

---

## OAC URL Structure

```
https://<instance-name>-<tenant>.analytics.ocp.oraclecloud.com/ui/
```

Key paths:
- `/ui/` — Main analytics UI
- `/analytics/` — Alternate path (same destination)
- `/xmlpserver/` — BI Publisher direct access
- `/bi/` — Classic catalog and Answers

---

## Versioning & Updates
- OAC follows a monthly release cadence
- Updates are applied by Oracle; customers can defer one release cycle
- Release notes published at docs.oracle.com/en/cloud/paas/analytics-cloud/

---

## Related
- [OAC vs OBIEE vs OAS Comparison](OAC%20vs%20OBIEE%20vs%20OAS%20Comparison.md){ .wikilink }
- [Semantic Model](Semantic%20Model.md){ .wikilink }
- [Data Sources & Connections](Data%20Sources%20%26%20Connections.md){ .wikilink }
- [Administration & Service Console](Administration%20%26%20Service%20Console.md){ .wikilink }
- [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }
