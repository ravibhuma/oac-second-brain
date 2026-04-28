# APIs, Embedding & Integration

> **Last updated:** 2026-04-27
> **Tags:** REST API, JavaScript API, embedding, Smart View, data actions, safe domains, Oracle Analytics Publisher API


📖 **Full Oracle Documentation**: [Developing in OAC](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acdev/) · [OAC REST APIs](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acpra/)

## Summary
OAC provides multiple integration points: a REST API for catalog and administration operations, a JavaScript Embedding API for embedding analytics in external web applications, Data Actions for cross-application navigation, and Smart View for Excel-based analytics. All embedding scenarios require Safe Domain registration.

---

## REST API

### Overview
OAC exposes a REST API for automating administration tasks, managing catalog objects, and querying data.

**Base URL**:
```
https://<instance>.analytics.ocp.oraclecloud.com/api/20210901
```

**Authentication**: OCI API Key (JWT token) or username/password (Basic Auth for SOAP compatibility)

### Key Endpoints

| Category | Endpoint | Description |
|---|---|---|
| **Catalog** | `GET /folders` | List catalog folders |
| | `GET /folders/{id}/objects` | List objects in a folder |
| | `POST /folders` | Create folder |
| | `DELETE /objects/{id}` | Delete catalog object |
| **Connections** | `GET /connections` | List data connections |
| | `POST /connections` | Create connection |
| **Analytics** | `POST /analytics/queries` | Execute Logical SQL |
| **Snapshots** | `GET /snapshots` | List snapshots |
| | `POST /snapshots` | Create snapshot |
| **Users** | `GET /users` | List users |

### Execute a Logical SQL Query via REST

```bash
curl -X POST \
  https://<instance>.analytics.ocp.oraclecloud.com/api/20210901/analytics/queries \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "SELECT \"Sales\".\"Product\".\"Category\", \"Sales\".\"Facts\".\"Revenue\" FROM \"Sales\" FETCH FIRST 100 ROWS ONLY",
    "limit": 100
  }'
```

### Catalog Import/Export (Bundle API)

```bash
# Export a dashboard
POST /export
{ "items": [{ "objectId": "<catalog-path>", "type": "ANALYSIS" }] }

# Import to another OAC
POST /import
{ bundle_file, targetFolder }
```

---

## JavaScript Embedding API

Embed OAC visualizations, workbooks, and dashboards into external web applications (portals, Salesforce, custom apps).

### How It Works
1. Register the external app's domain in OAC's Safe Domain list
2. Include the OAC embedding JavaScript file
3. Reference the OAC canvas/dashboard with an embed tag

### Safe Domains
Required before any embedding works:

**Administration** → **Safe Domains** → **Add domain**:
```
https://myportal.company.com
https://salesforce.com
```

### Embedding a Workbook Canvas

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://<oac-instance>/public/dv/js/embedding/standalone/embedding.js"
          type="module"></script>
</head>
<body>
  <oracle-dv
    project-path="/@Catalog/shared/Sales/RevenueWorkbook"
    active-page="canvas!1"
    active-tab-id="1">
  </oracle-dv>
</body>
</html>
```

### Embedding a Classic Dashboard

```html
<iframe 
  src="https://<oac-instance>/ui/analytics.jsp?PortalPath=%2F_portal%2FMySalesDashboard"
  width="1200" height="800" frameborder="0">
</iframe>
```

> ⚠️ **Warning:** iFrame embedding for Classic Dashboards requires the X-Frame-Options header to allow your domain. Configure in Service Console.

### Embedding Parameters

| Parameter | Description |
|---|---|
| `project-path` | Catalog path to the workbook |
| `active-page` | Canvas to display (`canvas!1`, `canvas!2`, etc.) |
| `filters` | JSON array of filter conditions to apply |
| `active-tab-id` | Tab/canvas index |

### Passing Filters to Embedded Content

```javascript
const viz = document.querySelector('oracle-dv');
viz.filters = JSON.stringify([
  {
    sColFormula: '"Sales"."Time"."Year"',
    sColName: 'Year',
    sOperator: 'in',
    isNumericCol: false,
    bIsDoubleColumn: false,
    aCodeValues: [],
    aDisplayValues: ['2024']
  }
]);
```

---

## Data Actions

Data Actions enable cross-application navigation from OAC visualizations.

### Types

| Type | What Happens When User Clicks |
|---|---|
| **Navigate to Analytics** | Open another analysis or workbook |
| **Navigate to URL** | Open any URL with column values as parameters |
| **Navigate to External URL** | Open external app (ERP, CRM, custom app) |
| **Invoke REST API** | Call a REST endpoint (trigger workflow, etc.) |
| **HTTP API** | HTTP GET/POST with data context |

### Creating a Data Action

1. Workbook → **Data Actions** panel → **Add Action**
2. Choose type
3. Configure:
   - **URL Pattern**: `https://myapp.com/orders?orderid=${Sales.Order.OrderID}`
   - **Anchor To**: column value click, menu, or button
   - **Pass context values**: include selected filters or column values

### Example: Link to ERP Order Detail
```
URL: https://erp.company.com/orders/detail?id=${Sales.Order."Order Number"}
Anchor: "Order Number" column
Open in: New tab
```

---

## Smart View (Excel Add-in)

Oracle Smart View connects Microsoft Excel, Word, and PowerPoint to OAC Subject Areas.

### Capabilities
- Query OAC Subject Areas directly from Excel
- Refresh data in place
- Ad-hoc analysis using Excel pivot-style interface
- Create Excel-based reports backed by live OAC data
- Submit data back to planning applications (Oracle EPM)

### Connection Setup
1. Download Smart View from Oracle (free)
2. Install Excel add-in
3. In Excel → Smart View → Connect
4. Enter OAC URL: `https://<instance>/xmlpserver/SmartViewProvider`
5. Authenticate with OAC credentials

### Smart View Panels
- **Home**: recent connections, favorites
- **Member Selection**: hierarchy browsing and selection
- **POV (Point of View)**: filter context (time period, scenario)

---

## Publisher Web Services (SOAP)

BI Publisher exposes SOAP web services for:
- Running reports programmatically
- Scheduling reports via API
- Browsing the catalog

```xml
<!-- Example: Run report via SOAP -->
<soapenv:Envelope>
  <soapenv:Body>
    <pub:runReport>
      <pub:reportRequest>
        <pub:reportAbsolutePath>/Shared/Sales/Monthly_Sales.xdo</pub:reportAbsolutePath>
        <pub:sizeOfDataChunkDownload>-1</pub:sizeOfDataChunkDownload>
      </pub:reportRequest>
    </pub:runReport>
  </soapenv:Body>
</soapenv:Envelope>
```

---

## OAC + Oracle Integration Cloud (OIC)

Use OIC to trigger OAC Agents (scheduled deliveries) or consume OAC REST APIs:
- OIC REST Adapter → OAC REST API
- Trigger data refresh after ERP data loads
- Post-processing of report outputs

---

## OAC + Oracle APEX

Embed OAC content in Oracle APEX applications:
1. Register APEX domain in Safe Domains
2. Use APEX page with HTML region containing the `<oracle-dv>` embed tag
3. Pass APEX session context as filter values

---

## Related
- [Classic Dashboards & Analyses](Classic%20Dashboards%20%26%20Analyses.md){ .wikilink }
- [Workbooks & Visualizations](Workbooks%20%26%20Visualizations.md){ .wikilink }
- [BI Publisher](BI%20Publisher.md){ .wikilink }
- [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }
- [Logical SQL Reference](Logical%20SQL%20Reference.md){ .wikilink }
- [Custom Visualizations & Plug-ins](Custom%20Visualizations%20%26%20Plug-ins.md){ .wikilink }
- [OCI REST APIs & CLI for OAC](OCI%20REST%20APIs%20%26%20CLI%20for%20OAC.md){ .wikilink }
