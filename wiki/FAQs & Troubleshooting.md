# FAQs & Troubleshooting

> **Last updated:** 2026-04-27
> **Tags:** FAQ, troubleshooting, errors, performance, common issues, diagnostics


📖 **Full Oracle Documentation**: [FAQs for OAC](https://docs.oracle.com/en/cloud/paas/analytics-cloud/faqs/) · [Troubleshooting Guide](https://docs.oracle.com/en/cloud/paas/analytics-cloud/troubleshoot/)

## Summary
Catalog of frequently asked questions and the most common troubleshooting scenarios in OAC: connection errors, query failures, RPD upload issues, performance problems, security errors, embedding issues, and BI Publisher problems.

---

## General FAQs

**Q: What's the difference between OAC and OAS?**
OAC = managed cloud on OCI. OAS = on-premise version. Same product internally, OAS has manual ops. See [OAC vs OBIEE vs OAS Comparison](OAC%20vs%20OBIEE%20vs%20OAS%20Comparison.md){ .wikilink }.

**Q: Can I connect OAC to on-premise databases?**
Yes — via Private Access Channel (PAC) or Remote Data Gateway (RDG). See [Data Sources & Connections](Data%20Sources%20%26%20Connections.md){ .wikilink }.

**Q: Does OAC support row-level security?**
Yes, multiple methods. Best practice: define data filters in the Subject Area using session variables. See [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }.

**Q: Can I move content between OAC environments (Dev → Test → Prod)?**
Yes — via snapshots (full) or REST API bundles (selective). See [Migration, Snapshots & Lifecycle](Migration%2C%20Snapshots%20%26%20Lifecycle.md){ .wikilink }.

**Q: Does OAC have an SDK for embedding in custom apps?**
Yes — JavaScript Embedding API. Requires Safe Domain registration. See [APIs, Embedding & Integration](APIs%2C%20Embedding%20%26%20Integration.md){ .wikilink }.

**Q: How are OAC users billed?**
By OCPU. Service is sized in OCPUs (typically 2-12+). Each OCPU has a per-hour rate.

**Q: Is OAC SaaS or PaaS?**
PaaS — you provision instances, manage content, but don't manage infrastructure.

---

## Connection Errors

### Error: `ORA-12541: TNS:no listener`
**Cause**: Database listener not running, or wrong port.
**Fix**:
- Verify DB listener: `lsnrctl status`
- Check OAC connection: hostname, port (default 1521 for Oracle)
- For PAC: verify DNS zone configuration

### Error: `ORA-28547: connection to server failed, probable Oracle Net admin error`
**Cause**: Wallet not configured for ADB.
**Fix**:
- Download wallet from Oracle Cloud → Autonomous Database
- Upload wallet to OAC connection
- Use TNS alias from `tnsnames.ora` (e.g., `mydb_high`)

### Error: `Failed to connect to <host>:<port>`
**Cause**: Network reachability issue.
**Fix**:
- Verify host is reachable from OAC's region
- For private IPs: confirm PAC is configured
- Check firewall rules on the DB side

### Error: `Authentication failed`
**Cause**: Credentials wrong or expired.
**Fix**:
- Re-test credentials in DB tool (SQL Developer)
- Update stored connection in OAC
- Check DB account: not locked, not expired, has SELECT privileges

---

## Query Errors

### Error: `nQSError: 22037 - Adaptive Subrequest Optimization is not supported`
**Cause**: Cross-source query without proper logical model setup.
**Fix**: Federate sources properly in Logical Layer with multiple LTSs and matching keys.

### Error: `nQSError: 14025 - No fact table exists at the requested level of detail`
**Cause**: Logical model has no fact table providing measures at the dimensions you've selected.
**Fix**:
- Check Content tab in BMM Layer LTS — verify the LTS is at the right grain
- Add a logical fact table that joins to the requested dimensions

### Error: `nQSError: 10058 - General error: Specify the database type connection pool returns`
**Cause**: Connection pool not configured properly.
**Fix**: Edit Physical Layer connection pool, set correct database type, test connection.

### Query is very slow
**Diagnostic steps**:
1. Enable BI Server query log: Manage Sessions → set Log Level 4 for the user
2. Run the query
3. Review `nqquery.log` for the physical SQL generated
4. Run physical SQL directly against DB — measure performance there
5. If physical SQL is slow → DB tuning (indexes, stats, hints)
6. If physical SQL is fast → BI Server processing issue (check joins, aggregations)

---

## RPD / Semantic Model Issues

### RPD upload fails
**Cause**: RPD password missing or wrong, RPD has consistency errors.
**Fix**:
- Open RPD locally in Model Administration Tool
- Tools → **Show Consistency Checker** → fix all errors and warnings
- Save with explicit RPD password
- Re-upload

### "Logical column has no source" error
**Cause**: A logical column isn't mapped to any physical column.
**Fix**: BMM Layer → logical column → Source tab → map to physical column.

### Subject Area not visible to user
**Cause**: Permissions on the Subject Area exclude the user/role.
**Fix**: Semantic Model → Subject Area → Permissions → grant Read or higher to the appropriate role.

### Initialization Block fails at login
**Cause**: SQL syntax error, connection error, or block returns wrong number of rows/columns.
**Fix**:
- Test the init block SQL directly in DB (replace `:USER` with a real username)
- Verify expected output: row count matches variable count
- Check init block log: nqserver.log filter for "Init block failed"

---

## Workbook / Dataset Issues

### Workbook fails to load — "Dataset error"
**Cause**: Dataset's underlying connection broken or refreshed.
**Fix**:
- Open the Dataset → Refresh
- If connection is broken, re-test/re-create connection
- Save the Workbook again

### Dataset upload fails (Excel)
**Cause**: File too large (>250MB compressed) or unsupported format.
**Fix**:
- Compress data: remove unused columns/sheets
- Save as CSV (smaller than xlsx)
- For large data: use Data Flow to load to Database, then connect via Subject Area

### Calculation in Workbook returns blank
**Cause**: Null values in the source data, or syntax error.
**Fix**:
- Wrap in `IFNULL("Column", 0)` to handle nulls
- Use the formula validator (red squiggle indicators)

---

## Security Errors

### "Access denied" when opening a dashboard
**Cause**: User lacks Read permission on the dashboard or its underlying analyses.
**Fix**: Catalog → right-click dashboard → Permissions → grant Read to the user/role. Also check parent folder permissions.

### User sees no data (empty results) but query runs
**Cause**: Data filter (RLS) is filtering out all rows.
**Fix**:
- Check Subject Area Data Filters
- Verify session variable populated correctly: `SELECT VALUEOF(NQ_SESSION.<var>) FROM dual` (in test query)
- Check init block returns the expected value for this user

### SSO login fails / loops
**Cause**: SAML configuration mismatch.
**Fix**:
- Verify SP entity ID and ACS URL match between IDCS and IdP
- Check signing certificate not expired
- Review OCI Audit logs for the failed login

---

## Performance Issues

### Dashboard takes 30+ seconds to load
**Diagnostics**:
1. Enable performance dashboard: append `?enablePerformanceDashboard=true` to URL
2. Identify slow analyses
3. For each slow analysis:
   - Check rows returned (limit if huge)
   - Check joins in BMM Layer (avoid cross-joins)
   - Check if cache is being used (X-Oracle-BICache header)
   - Push aggregation to DB: define aggregate tables in semantic model

### BI Server runs out of memory
**Cause**: Large in-memory operations (cross-source joins, large aggregations).
**Fix**:
- Push joins to DB (federated query optimization)
- Increase OCPUs (more memory)
- Limit query row caps (`Max Rows` in System settings)
- Use database-resident aggregate tables

---

## BI Publisher Issues

### Report runs but output is blank
**Cause**: Data Model returns 0 rows for the parameter values.
**Fix**:
- Run the data model directly: Data Model → View Data
- Check parameters are passed correctly
- Verify SQL filter conditions

### RTF template doesn't render correctly
**Cause**: Tag mismatches, incorrect for-each loops.
**Fix**:
- Use BI Publisher Word add-in → Validate Template
- Check XML output structure matches template field references

### Burst delivery fails
**Cause**: Bursting query returned wrong column names, SMTP issue, or recipient address invalid.
**Fix**:
- Bursting query MUST return columns: `SPLIT_KEY`, `DEL_CHANNEL`, `DEL_ADDRESS`, `LOCALE`, `TEMPLATE`, `OUTPUT_FORMAT`
- Test SMTP separately: Administration → Test Email
- Verify recipient emails are valid format

---

## Embedding Issues

### "Refused to display in iframe" error
**Cause**: X-Frame-Options header blocking embedding.
**Fix**:
- Add embedding domain to **Safe Domains** list
- Use the JavaScript Embedding API rather than iframe

### Embedded workbook shows login page
**Cause**: User session cookie not shared with embedding context.
**Fix**:
- Configure SSO so embedding context has the same session
- Use OAuth flow with token-based auth for embedded contexts

### Filters not passing to embedded workbook
**Cause**: Filter object format wrong or column reference incorrect.
**Fix**:
- Use the exact column formula (three-part name): `"Subject Area"."Folder"."Column"`
- Use Browser DevTools to inspect the filter object passed

---

## OCI / Service-Level Issues

### Cannot start instance
**Cause**: OCPU quota exhausted, region capacity issue, or billing hold.
**Fix**:
- Check tenancy quotas: OCI → Limits, Quotas
- Try different availability domain
- Contact Oracle Support if billing-related

### Snapshot restore fails
**Cause**: Source and target versions incompatible (e.g., trying to restore newer snapshot to older OAC).
**Fix**:
- Update target OAC instance to match or exceed source version
- Re-attempt restore

---

## How to Get Help

| Resource | When to Use |
|---|---|
| Oracle Support (My Oracle Support) | Production issues, suspected bugs |
| Oracle Analytics Community | Best practices, design questions |
| Oracle Analytics Blog | Recent feature how-tos |
| Oracle docs | Reference material |
| Stack Overflow `oracle-analytics-cloud` tag | Specific code/SQL problems |

---

## Related
- [Administration & Service Console](Administration%20%26%20Service%20Console.md){ .wikilink }
- [Data Sources & Connections](Data%20Sources%20%26%20Connections.md){ .wikilink }
- [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }
- [Semantic Model](Semantic%20Model.md){ .wikilink }
- [Consumer Guide (Explore)](Consumer%20Guide%20%28Explore%29.md){ .wikilink }
- [OAC vs OBIEE vs OAS Comparison](OAC%20vs%20OBIEE%20vs%20OAS%20Comparison.md){ .wikilink }
- [Migration, Snapshots & Lifecycle](Migration%2C%20Snapshots%20%26%20Lifecycle.md){ .wikilink }
- [Source PDFs Index](Source%20PDFs%20Index.md){ .wikilink }
