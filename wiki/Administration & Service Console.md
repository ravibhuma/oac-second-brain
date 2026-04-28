# Administration & Service Console

> **Last updated:** 2026-04-27
> **Tags:** administration, service console, snapshots, scaling, caching, performance, diagnostics, usage tracking


📖 **Full Oracle Documentation**: [Administering OAC](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acoag/) · [Configuring OAC](https://docs.oracle.com/en/cloud/paas/analytics-cloud/aciag/)

## Summary
OAC administration is performed through the **Service Console** (OCI console → Analytics Cloud → your instance) and the **OAC Administration** page (within the OAC UI). Admins manage backups/snapshots, scaling, system configuration, caching, diagnostics, and user management.

---

## Accessing the Admin Areas

### OCI Console (Provisioning & Infrastructure)
`OCI Console` → `Analytics & AI` → `Analytics Cloud` → select your instance
- Scale OCPUs up/down
- Start/stop the service
- Create/restore snapshots
- Private Access Channel management
- Manage IDCS/IAM integration

### OAC Administration Page (In-App)
`OAC Home` → **Navigator (hamburger)** → **Console** (or **Administration**)
- System configuration
- Semantic model management
- Usage tracking
- Cache management
- Manage connections
- Security settings
- Mail server setup

---

## Snapshots (Backup & Restore)

Snapshots capture the complete OAC state: catalog, data models, connections, system settings.

### Creating a Snapshot
**OCI Console** → **Analytics Cloud** → instance → **Snapshots** → **Create Snapshot**:
- Snapshot includes: full catalog, RPD/Semantic Model, connections, BI Publisher catalog
- Does **not** include: data in datasets (must be re-loaded), user passwords

### Restoring a Snapshot
- Restore to the same instance (overwrite)
- Restore to a new instance (migration)

> ⚠️ Warning: Restoring a snapshot overwrites all existing content. Always take a new snapshot before restoring.

### Scheduled Snapshots
Oracle does NOT automatically schedule snapshots. Best practice:
- Create a weekly snapshot via OCI Console or API
- Store externally (download to Object Storage) for DR

---

## Scaling

### Vertical Scaling (OCPUs)
OAC is licensed and sized by OCPUs:
- Scale up: increase OCPUs for better query performance / more concurrent users
- Scale down: reduce costs during off-peak

**Steps**: OCI Console → Analytics Cloud → instance → **Scale**
- Choose new OCPU count
- Takes ~5-10 minutes; service briefly restarts

### Auto-Scaling (Not Native)
OAC does not auto-scale. Manual scaling or scripted scaling via OCI APIs:
```bash
# OCI CLI example
oci analytics analytics-instance scale \
  --analytics-instance-id <ocid> \
  --capacity-type OLPU_COUNT \
  --capacity-value 4
```

---

## Caching

### BI Server Cache (Query Cache)
Caches Logical SQL query results:
- **Enabled by default**
- Cache entries keyed by exact Logical SQL + parameters
- TTL configurable per Subject Area or globally
- **Seed cache**: pre-populate after data refresh

**Configuration**: Administration → Cache Management
- Enable/disable cache globally
- Set maximum cache entries (default 1000)
- Set maximum row count per entry

**Purge Cache**:
- Purge all: Administration → Cache Management → Purge All
- Purge specific Subject Area: selective purge
- Event-based purge: trigger via ODBC/API after ETL completes

### Dataset Cache
Datasets loaded into OAC in-memory engine:
- Set dataset refresh schedule or manual refresh
- Administration → Dataset Cache → view cached datasets

---

## System Configuration

### General Settings
- Default home page
- Session timeout
- Max rows returned per query (default 65,000 for analysis)
- Performance settings

### Map Settings
- Configure map background layers (Oracle Maps Cloud, custom tile servers)
- Load custom GeoJSON map layers

### Mail Server
Configure SMTP for:
- Agent deliveries (scheduled reports/alerts)
- BI Publisher report distribution
- KPI alert notifications

Administration → Manage Email → provide SMTP host, port, TLS settings, sender address

---

## Usage Tracking

Records every query executed against OAC Subject Areas.

### Enable Usage Tracking
Administration → Usage Tracking:
1. Enable Usage Tracking
2. Specify target connection (Oracle DB recommended)
3. Specify schema / table prefix
4. OAC creates `S_NQ_ACCT` table for query logs, `S_NQ_DB_ACCT` for physical queries

### Usage Tracking Tables
| Table | Contents |
|---|---|
| `S_NQ_ACCT` | One row per Logical query: user, subject area, time, rows, duration |
| `S_NQ_DB_ACCT` | One row per Physical query generated |
| `S_NQ_SUMMARY` | Aggregated summary |

> 💡 Tip: Build an OAC Subject Area on top of the usage tracking tables to analyze performance, popular reports, and slow queries.

---

## Diagnostics & Logs

### Log Files (Service Console → Diagnostics)
| Log | Contents |
|---|---|
| `nqquery.log` | BI Server query log (Logical and Physical SQL) |
| `nqserver.log` | BI Server startup, errors, warnings |
| `obips_diagnostic.log` | Presentation Services errors |
| `xmlp_server.log` | BI Publisher log |

### Enable Query Logging per User
For debugging a specific user's queries:
1. Administration → Manage Sessions → select user → set Log Level (1-5)
2. Level 1: basic query info; Level 5: full query trace

### Performance Analyzer (Workbooks)
Enable via browser URL parameter: `?enablePerformanceDashboard=true`
Shows render time, query time, and data fetch time per visualization.

---

## Managing the Semantic Model

### Upload RPD (Classic)
Service Console → Semantic Model → Upload:
- Upload `.rpd` file
- Set RPD password
- Activate (takes 1-2 minutes)

### Download RPD
Service Console → Semantic Model → Download

### Semantic Modeler (Browser)
Access via OAC Home → Navigate → Semantic Model

---

## User & Session Management

### View Active Sessions
Administration → Manage Sessions:
- See all active user sessions
- Kill a session
- See what query a user is running

### Impersonate User
Administration → Security → Test User:
- Log in as another user to test their security context

---

## Related
- [OAC Overview & Architecture](OAC%20Overview%20%26%20Architecture.md){ .wikilink }
- [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }
- [Semantic Model](Semantic%20Model.md){ .wikilink }
- [Data Sources & Connections](Data%20Sources%20%26%20Connections.md){ .wikilink }
- [Migration, Snapshots & Lifecycle](Migration%2C%20Snapshots%20%26%20Lifecycle.md){ .wikilink }
- [OCI REST APIs & CLI for OAC](OCI%20REST%20APIs%20%26%20CLI%20for%20OAC.md){ .wikilink }
- [Custom Visualizations & Plug-ins](Custom%20Visualizations%20%26%20Plug-ins.md){ .wikilink }
- [OAC AI Agents](OAC%20AI%20Agents.md){ .wikilink }
- [OAC MCP Server](OAC%20MCP%20Server.md){ .wikilink }
