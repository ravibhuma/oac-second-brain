# OAC vs OBIEE vs OAS Comparison

> **Last updated:** 2026-04-27
> **Tags:** OBIEE, OAS, OAC, comparison, migration, differences, feature parity

## Summary
Oracle has three generations of analytics platforms: **OBIEE** (on-premise, legacy), **Oracle Analytics Server (OAS)** (on-premise, current), and **Oracle Analytics Cloud (OAC)** (cloud, current). OAC is the strategic direction. OAS is OAC's on-premise equivalent with near feature parity. OBIEE 11g is end-of-life; OBIEE 12c is in sustaining support.

---

## High-Level Comparison

| Feature | OBIEE 11g | OBIEE 12c | OAS 6.x | OAC |
|---|---|---|---|---|
| **Deployment** | On-premise | On-premise | On-premise | OCI Cloud |
| **Status** | End of Life (2024) | Sustaining Support | Active | Active / Strategic |
| **Self-Service DV** | No | Limited (VA) | Yes | Yes (Workbooks) |
| **Semantic Modeler (browser)** | No | No | No | Yes |
| **ML / AI Features** | No | No | Limited | Full (OML, Explain, AI) |
| **BI Publisher** | Yes | Yes | Yes | Yes |
| **Classic Dashboards** | Yes | Yes | Yes | Yes |
| **Natural Language Query** | No | No | Limited | Yes |
| **Data Flows** | No | No | Yes | Yes |
| **Automatic Updates** | Manual patches | Manual patches | Manual patches | Oracle-managed |
| **Scaling** | Manual hardware | Manual hardware | Manual hardware | OCPU scaling |
| **Map Backgrounds** | Oracle Maps | Oracle Maps | Oracle Maps | Oracle Maps + Esri |
| **Mobile App** | Day by Day | Day by Day | Day by Day | Oracle Analytics |

---

## Architecture Differences

### OBIEE 11g
- **Stack**: WebLogic 10.3, OPMN, BI Components
- **Admin**: Enterprise Manager, BI Admin Tool (desktop)
- **Catalog**: WebDAV-based file store
- **Security**: WLS embedded LDAP or OID
- **Deployment**: Windows or Linux server, manual installation

### OBIEE 12c
- **Stack**: WebLogic 12c, Oracle HTTP Server
- **Admin**: WebLogic Admin Console, BI Admin Tool
- **Security**: OPSS (Oracle Platform Security Services)
- **New features over 11g**: Visual Analyzer (basic DV), better mobile, refreshed UI

### Oracle Analytics Server (OAS) 6.x
- **On-premise equivalent of OAC**
- Same Workbooks / Data Flows / ML interface as OAC
- Browser-based Semantic Modeler available from OAS 7
- Requires Oracle Linux or compatible OS
- Manual installation and patching

### Oracle Analytics Cloud (OAC)
- **Fully managed PaaS on OCI**
- Same product codebase as OAS
- Oracle handles all patching, HA, backups
- Monthly feature releases
- OCPU-based scaling (no hardware management)

---

## Feature Deep Dive: What Changed in OAC vs OBIEE

### Better in OAC

| Area | OBIEE | OAC Improvement |
|---|---|---|
| Data Visualization | VA (limited) | Full Workbooks with 50+ chart types |
| Data Prep | No ETL | Data Flows with 20+ transform steps |
| ML | No | OML, AutoML, Explain, NLQ, AI Vision |
| Semantic Model | Desktop RPD tool only | Browser-based Semantic Modeler |
| Administration | FMW stack complexity | Simple Service Console |
| Deployment | Weeks | Hours |
| Maps | Basic Oracle Maps | Oracle Maps + Esri + Custom GeoJSON |
| Mobile | Day by Day (deprecated) | Oracle Analytics mobile app |
| Embedding | iFrame only | JavaScript Embedding API |

### Same in OAC (Feature Parity)
- Classic Dashboards and Analyses (Answers UI)
- BI Publisher reports (same engine)
- Logical SQL (same language)
- Semantic Model (three-layer RPD structure)
- Security model (roles, object permissions, RLS)
- Agents (alerts and scheduled delivery)
- Scorecards and KPIs

### Not Available in OAC (vs OBIEE)
| OBIEE Feature | OAC Status |
|---|---|
| Oracle BI Applications (OBIA) | Replaced by **Oracle Fusion Analytics (FAW)** |
| Direct LDAP/AD integration | Via IDCS/OCI IAM federation only |
| Custom skins/themes (CSS overrides) | Limited; different customization model |
| Complex initialization block types | Some not yet in Semantic Modeler |
| Delivers to UCM/Stellent | UCM delivery available but requires config |

---

## OAS vs OAC: Key Differences

| Aspect | OAS | OAC |
|---|---|---|
| Infrastructure | Customer-managed | Oracle-managed |
| Patching | Manual, customer responsibility | Automatic (Oracle) |
| HA/DR | Customer must configure | Built-in |
| Scaling | Add hardware | Change OCPU count |
| Cost model | License + hardware | OCPU subscription |
| Feature releases | Quarterly | Monthly |
| Internet connectivity | Not required | Required (OCI) |
| Data sovereignty | Full control | OCI region selection |

**When to choose OAS over OAC**:
- Strict data sovereignty / no cloud data requirements
- Air-gapped networks
- Existing on-premise investment to leverage

**When to choose OAC**:
- New deployments (Oracle's strategic direction)
- Rapid deployment needed
- Want managed operations (no DBA/admin overhead)
- Fusion SaaS customer (OAC integrates natively)

---

## Oracle Fusion Analytics Warehouse (FAW)

FAW is a pre-built analytics solution for Oracle Fusion Cloud (ERP, HCM, SCM, CX):
- Pre-built data pipelines: Fusion → ADW
- Pre-built semantic model (Subject Areas)
- Pre-built dashboards and KPIs for each Fusion module
- Deployed on OAC (uses OAC as the analytics front-end)

**Not the same as OAC**: FAW is a SaaS analytics product built on top of OAC + ADW.

---

## Migration Timeline / Recommendations

```
OBIEE 11g  →  Migrate to OAC ASAP (EOL since 2024)
OBIEE 12c  →  Migrate to OAC (sustaining support only)
OAS        →  Continue or migrate to OAC (functionally equivalent)
OAC        →  Strategic platform — invest here
```

---

## Related
- [OAC Overview & Architecture](OAC%20Overview%20%26%20Architecture.md){ .wikilink }
- [Migration, Snapshots & Lifecycle](Migration%2C%20Snapshots%20%26%20Lifecycle.md){ .wikilink }
- [Semantic Model](Semantic%20Model.md){ .wikilink }
- [Classic Dashboards & Analyses](Classic%20Dashboards%20%26%20Analyses.md){ .wikilink }
