# Data Sources & Connections

> **Last updated:** 2026-04-27
> **Tags:** connections, data sources, PAC, remote data gateway, database, cloud

📖 **Full Oracle Documentation**: [Connecting OAC to Your Data](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acdpr/)

## Summary
OAC can connect to virtually any data source — **80+ supported types** across cloud databases, on-premise databases, files, REST APIs, big-data engines, and SaaS applications. Connections are managed centrally and can be shared or private.

For the complete, always-current list of supported data sources, see Oracle's official documentation: [Supported Data Sources](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acdpr/supported-data-sources.html).

---

## Connection Types — Full Reference

### Oracle Databases
| Type | Protocol | Notes |
|---|---|---|
| Oracle Database (on-premise) | JDBC/TNS | Native, best performance |
| Oracle Autonomous Data Warehouse (ADW) | mTLS wallet or TLS | Recommended for cloud DW |
| Oracle Autonomous Transaction Processing (ATP) | mTLS wallet or TLS | OLTP workloads |
| Oracle Database Cloud Service | JDBC/TNS | Older Oracle Cloud DB |
| Oracle Essbase | Native API | Multidimensional / OLAP |
| Oracle MySQL HeatWave | JDBC | Cloud MySQL with analytics acceleration |
| Oracle TimesTen | JDBC | In-memory database |

### Open-Source / Third-Party Databases
| Type | Protocol |
|---|---|
| MySQL | JDBC |
| PostgreSQL | JDBC |
| Microsoft SQL Server | JDBC |
| MariaDB | JDBC |
| IBM DB2 | JDBC |
| IBM Informix | JDBC |
| Sybase ASE / IQ | JDBC |
| Teradata | JDBC |
| Vertica | JDBC |
| Greenplum | JDBC |
| Apache Drill | JDBC |
| Apache Pinot | JDBC |
| Cassandra | JDBC |
| MongoDB | JDBC (BI Connector) |
| ClickHouse | JDBC |
| YugabyteDB | JDBC (PostgreSQL-compatible) |

### Cloud Data Warehouses
| Type | Notes |
|---|---|
| Snowflake | JDBC |
| Google BigQuery | JDBC |
| Amazon Redshift | JDBC |
| Amazon Aurora (MySQL/PostgreSQL) | JDBC |
| Amazon RDS | JDBC |
| Microsoft Azure SQL Database | JDBC |
| Microsoft Azure Synapse Analytics | JDBC |
| SAP HANA | JDBC |
| SAP S/4 HANA Cloud | JDBC |
| Databricks | JDBC |

### Big Data Engines
| Type | Notes |
|---|---|
| Apache Hive | JDBC (HiveServer2) |
| Apache Spark SQL | JDBC (Thrift Server) |
| Apache Impala | JDBC |
| Cloudera CDP | JDBC |
| Hortonworks (legacy) | JDBC |
| Amazon EMR | JDBC |

### File-Based Sources
| Type | Notes |
|---|---|
| **Excel** (.xlsx, .xls) | Upload directly → creates Dataset |
| **CSV / TSV** | Upload → creates Dataset (auto-detect delimiter) |
| **JSON** | Flat file upload, schema inferred |
| **Apache Parquet** | Columnar, used heavily for object storage data |
| **Apache Avro** | For Hadoop ecosystems |

### Cloud File Storage
- **OCI Object Storage** — native, recommended for OAC
- **Dropbox** — personal/team file integration
- **Google Drive** — personal/team file integration
- **Box** — enterprise file storage
- **Microsoft OneDrive / SharePoint** — via REST connector
- **Amazon S3** — via JDBC or generic connectors

### Cloud Applications (SaaS)
| Application | Connector Type |
|---|---|
| **Oracle Fusion ERP** | Preconfigured Oracle Fusion connector |
| **Oracle Fusion HCM** | Preconfigured Oracle Fusion connector |
| **Oracle Fusion SCM** | Preconfigured Oracle Fusion connector |
| **Oracle Fusion CX (Sales/Service/Marketing)** | Preconfigured Oracle Fusion connector |
| **Oracle NetSuite** | REST API connector |
| **Oracle Eloqua** | REST API connector |
| **Oracle E-Business Suite (EBS)** | JDBC + Subject Area |
| **Oracle JD Edwards** | JDBC |
| **Oracle Siebel CRM** | JDBC |
| **Oracle PeopleSoft** | JDBC |
| **Salesforce** | REST API connector (with OAuth) |
| **Salesforce Commerce Cloud** | REST API |
| **ServiceNow** | REST API connector |
| **Workday** | REST API + WSDL |
| **SAP S/4 HANA** | JDBC + REST |
| **SAP BW** | JDBC |
| **HubSpot** | REST connector |
| **Marketo** | REST connector |
| **Zendesk** | REST connector |
| **Microsoft Dynamics 365** | OData/REST |

### REST API & Web Services
- **Generic REST connector** — any HTTP/HTTPS endpoint with JSON/XML response
- **Generic OAuth REST connector** — for OAuth 2.0 authenticated APIs
- **OData v4** — built-in for OData-compliant APIs
- **SOAP Web Services** — XML-based legacy APIs

### Oracle Fusion Analytics Warehouse (FAW) Sources
When OAC is paired with FAW, additional pre-built connections include Fusion ERP/HCM/SCM/CX with auto-pipelined data into Oracle Autonomous Data Warehouse.

### Streaming / Real-Time Sources
- **Kafka** (via Hive/Drill bridges)
- **OCI Streaming** (via REST)
- For true streaming, use Oracle GoldenGate to land into a connected DB

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
- See [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }

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
- [Semantic Model](Semantic%20Model.md){ .wikilink }
- [Subject Areas & Datasets](Subject%20Areas%20%26%20Datasets.md){ .wikilink }
- [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }
- [Administration & Service Console](Administration%20%26%20Service%20Console.md){ .wikilink }
