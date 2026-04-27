# Data Sources & Connections

> **Last updated:** 2026-04-27
> **Tags:** connections, data sources, PAC, remote data gateway, database, cloud

## Summary
OAC can connect to virtually any data source — cloud databases, on-premise databases, files, REST APIs, and SaaS applications. Connections are managed centrally and can be shared or private.

---

## Connection Types

### Database Connections
| Type | Protocol | Notes |
|---|---|---|
| Oracle Database (ADW, ATP, DB) | JDBC/TNS | Native, best performance |
| Oracle Autonomous Database | mTLS wallet or TLS | Recommended for cloud-native |
| MySQL | JDBC | |
| PostgreSQL | JDBC | |
| SQL Server | JDBC | |
| IBM DB2 | JDBC | |
| Hive / Spark | JDBC | |
| Snowflake | JDBC | |
| BigQuery | JDBC | |

### File-Based Connections
- **Excel** (.xlsx, .xls) — upload directly, creates Dataset
- **CSV / TSV** — upload, creates Dataset
- **JSON** — flat file upload
- **Dropbox / Google Drive** — cloud file integration

### Cloud Application Connections
- Oracle Fusion (ERP, HCM, SCM) — preconfigured connector
- Salesforce — REST API connector
- Oracle NetSuite — REST connector
- ServiceNow — REST connector

### REST API Connections
Generic REST connector allows connecting to any HTTP/HTTPS API endpoint.

---

## Connection Scope

| Scope | Visible to | Created by |
|---|---|---|
| **Shared** | All users with permission | Admin or authorized user |
| **Private** | Creator only | Any user |

> ⚠️ **Warning:** Credentials in shared connections are stored encrypted in OAC's credential store. Do not share private DB user credentials through shared connections.

---

## Private Access Channel (PAC)

Used to connect OAC to data sources inside a **private VCN** (Virtual Cloud Network) or on-premise network.

### Architecture
```
OAC (OCI Public)  ←──── PAC (reverse proxy) ←──── Private Network / On-Premise DB
```

### Setup Steps
1. In Service Console → Private Access Channel → Create
2. Provide VCN and subnet details (must be in same region)
3. DNS zones: add private DNS entries for your on-premise hostnames
4. Connection uses PAC automatically when the hostname matches a configured DNS zone

### PAC DNS Zones
- Configure private DNS zones so OAC resolves internal hostnames through PAC
- Example: `db.internal.company.com` → routes through PAC

> 💡 **Tip:** PAC is the preferred method for on-premise connectivity. It does not require opening inbound firewall ports.

---

## Remote Data Gateway (RDG)

An agent installed on-premise that proxies data requests from OAC.

### When to Use
- Legacy databases not reachable via PAC
- File system data sources
- Windows-only JDBC drivers

### Architecture
```
OAC ──── Oracle Cloud Relay ──── RDG Agent (on-premise) ──── Data Source
```

### Installation
1. Download RDG agent from Service Console
2. Install on a Windows/Linux server with network access to the data source
3. Register agent in Service Console with a token
4. Configure connections to use the RDG agent

---

## Creating a Connection (UI Steps)

1. **Home** → **Create** → **Connection**
2. Select connection type
3. Enter host, port, service name / SID
4. Enter credentials (username/password or wallet)
5. Test connection
6. Save as shared or private

---

## Connection Security

- Credentials stored in Oracle Vault (encrypted)
- Connection passwords never visible after save
- Row-level security can be applied at the Subject Area level using connection pool credentials
- See [[Security & Row-Level Security]]

---

## Connection Pools (Semantic Model)
In the Semantic Model, connection pools define how the BI Server connects to a physical database:
- **Shared login** — all users use one DB account (most common)
- **Individual login** — each OAC user maps to a DB account
- **Session variables** — pass user context (e.g., `VALUEOF(NQ_SESSION.USER)`) to DB for VPD/RLS

---

## Troubleshooting Connections

| Error | Likely Cause |
|---|---|
| `Connection refused` | Wrong host/port, firewall blocking |
| `ORA-12541` | TNS listener not running or wrong port |
| `Invalid credentials` | Wrong username/password |
| `Wallet error` | Wallet not uploaded or wrong wallet for ADW |
| PAC timeout | DNS zone not configured or PAC not deployed |

---

## Related
- [[Semantic Model]]
- [[Subject Areas & Datasets]]
- [[Security & Row-Level Security]]
- [[Administration & Service Console]]
