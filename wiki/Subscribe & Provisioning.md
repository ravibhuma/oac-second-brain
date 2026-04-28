# Subscribe & Provisioning

> **Last updated:** 2026-04-27
> **Tags:** provisioning, subscription, OCPU, sizing, region, IDCS, OCI IAM, setup


📖 **Full Oracle Documentation**: [Administering OAC (Gen 2)](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acoag/) · [Subscribe and Set Up](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acoag/manage-services.html)

## Summary
Provisioning OAC means creating an Analytics Cloud instance in Oracle Cloud Infrastructure. This involves choosing a region, sizing OCPUs, configuring identity (IDCS or OCI IAM with Identity Domains), and (optionally) configuring Private Access Channel for private network connectivity.

---

## Prerequisites

Before provisioning OAC:

| Requirement | Notes |
|---|---|
| OCI tenancy | Active Oracle Cloud account |
| OCPU quota | Verify in OCI → Limits, Quotas — request increase if needed |
| IAM identity setup | IDCS (legacy) or OCI IAM Identity Domains |
| Region selected | Choose closest to users / data sources |
| Compartment | Logical container for the OAC instance |
| (Optional) VCN | If using Private Access Channel for on-prem data |

---

## Provisioning Steps (OCI Console)

### Step 1: Navigate
**OCI Console** → **Analytics & AI** → **Analytics Cloud**

### Step 2: Create Instance
Click **Create Instance**:

- **Name**: e.g., `oac-prod`
- **Compartment**: choose compartment
- **Region**: confirm region
- **Edition**: Enterprise / Professional
- **Capacity Type**: OCPU count or "License Included"
- **OCPU Count**: 1, 2, 4, 8, 12, 16, 24, 36, 52
- **License Type**: Bring Your Own License (BYOL) or License Included

### Step 3: Authentication
Choose identity provider:

- **OCI IAM with Identity Domains** (recommended for new instances)
- **IDCS** (legacy, for existing tenancies)

Select an Identity Domain → assign administrators.

### Step 4: Network (Optional)
- **Public access** (default): instance accessible via internet
- **Private Access Channel**: configure VCN/subnet for private connectivity

### Step 5: Tagging (Optional)
- Free-form tags or defined tags for cost tracking

### Step 6: Create
Click **Create**. Provisioning takes 15-30 minutes.

---

## OCPU Sizing Guidance

OCPU = the unit of compute that determines:

- Memory (typically 16-30 GB per OCPU)
- Concurrent user capacity
- Query parallelism

| Use Case | Recommended OCPUs |
|---|---|
| Development / small team (≤10 users) | 1-2 |
| Small department (≤50 users, light usage) | 2-4 |
| Mid-size deployment (50-200 users) | 4-8 |
| Large deployment (200-500 users) | 8-16 |
| Enterprise (500+ users, heavy usage) | 16-52 |

> 💡 **Tip:** Start small. OCPU count can be scaled up/down anytime in 5-10 minutes via OCI Console.

### Sizing Considerations
- **Concurrent users**: each user consumes memory for sessions
- **Data volume**: larger Subject Areas / Datasets need more memory
- **Query complexity**: BI Server uses CPU for joins, aggregations
- **Data Flow load**: Data Flows are CPU-intensive
- **ML training**: model training in Data Flows uses significant compute

---

## Edition Selection

| Edition | When to Choose |
|---|---|
| **Enterprise** | Need Classic Dashboards, BI Publisher, Semantic Model, ML, full features |
| **Professional** | Self-service only — Workbooks, Datasets, no RPD modeling |

> ⚠️ **Warning:** You cannot upgrade Professional → Enterprise without re-provisioning. Choose carefully.

---

## License Models

### License Included
- Pay Oracle as part of the OCPU rate
- All features included
- Simplest to start

### Bring Your Own License (BYOL)
- Use existing OBIEE/OAC perpetual licenses
- Lower OCPU rate
- Requires valid Oracle license entitlement

---

## Post-Provisioning Setup

### 1. Verify Instance
**OCI Console** → instance → **Status**: Active

### 2. Access OAC
Click the OAC URL: `https://<instance>-<tenant>.analytics.ocp.oraclecloud.com/ui/`

### 3. Add Users to Roles
Navigate to **Console** → **Users and Roles**:

- Assign **BI Service Administrator** to admins
- Assign **DV Author** or **BI Author** to content creators
- Assign **DV Consumer** or **BI Consumer** to end users

### 4. Configure Mail Server
**Console** → **Mail Settings**:
- SMTP host, port, credentials
- Sender address
- Test email

### 5. Configure Map Service (Optional)
**Console** → **Map Settings**:
- Default: Oracle Maps Cloud Service
- Custom: register Esri or other tile services
- Upload custom GeoJSON layers

### 6. Configure Safe Domains (For Embedding)
**Console** → **Safe Domains**:
- Add domains where OAC content will be embedded
- Required before any embedded use

### 7. Set Up Connections
Console → **Connections** → create connections to data sources:

- Oracle Autonomous Database
- On-premise databases (via PAC)
- Cloud applications (Fusion, Salesforce, etc.)

See [Data Sources & Connections](Data%20Sources%20%26%20Connections.md){ .wikilink }.

### 8. Take Initial Snapshot
**OCI Console** → **Snapshots** → **Create**:
- Baseline snapshot before any work begins
- Restore point if needed

---

## Multi-Environment Setup

For DEV/TEST/PROD:

```
PROD instance — full OCPU, restricted access
TEST instance — half OCPU, business stakeholder access
DEV instance — minimum OCPU, developer access
```

Use snapshots to clone PROD → TEST or DEV for testing.

---

## Cost Optimization

### Pause / Resume
OAC can be **paused** when not in use:

- **OCI Console** → instance → **Stop**
- Stops billing for OCPU compute
- Storage continues to bill (small)
- **Start** to resume — typically 5-10 minutes

> 💡 **Tip:** Stop DEV/TEST instances overnight and weekends to cut costs ~70%.

### Scaling Down for Off-Peak
Schedule OCI CLI / Functions to scale OCPUs down at night:
```bash
oci analytics analytics-instance scale \
  --analytics-instance-id <ocid> \
  --capacity-type OLPU_COUNT \
  --capacity-value 2
```

---

## Region Selection

Choose region based on:

- **User location** (latency)
- **Data source location** (avoid cross-region data transfer fees)
- **Compliance** (data sovereignty)
- **Service availability** (some regions don't have all OCI services)

OAC is available in 30+ OCI regions globally.

---

## Identity Domain Considerations

### IDCS (Legacy)
- Original OCI identity service
- Still supported
- Tenancies created before ~2021 likely use this

### OCI IAM with Identity Domains
- Modern unified identity
- Recommended for new tenancies
- Better security features (advanced MFA, adaptive auth)

> ⚠️ **Warning:** Migrating from IDCS to OCI IAM Domains is a multi-step process. Start with the right choice.

---

## Decommissioning

To delete an OAC instance:

1. Take final snapshot (optional, for archive)
2. Download snapshot to OCI Object Storage
3. **OCI Console** → instance → **Delete**
4. Confirm — instance is permanently deleted

---

## Related
- [OAC Overview & Architecture](OAC%20Overview%20%26%20Architecture.md){ .wikilink }
- [Administration & Service Console](Administration%20%26%20Service%20Console.md){ .wikilink }
- [OCI REST APIs & CLI for OAC](OCI%20REST%20APIs%20%26%20CLI%20for%20OAC.md){ .wikilink }
- [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }
- [Migration, Snapshots & Lifecycle](Migration%2C%20Snapshots%20%26%20Lifecycle.md){ .wikilink }
