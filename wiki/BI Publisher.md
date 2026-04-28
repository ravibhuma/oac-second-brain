# BI Publisher (Pixel-Perfect Reports)

> **Last updated:** 2026-04-27
> **Tags:** BI Publisher, pixel-perfect, reports, templates, RTF, XPT, bursting, scheduling, data model


📖 **Full Oracle Documentation**: [Designing and Publishing Pixel-Perfect Reports](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acpub/) · [Designing Pixel-Perfect Layouts](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acpld/)

## Summary
Oracle BI Publisher (part of OAC Enterprise) generates pixel-perfect, formatted reports for printing, distribution, and regulatory compliance. It separates data retrieval (Data Model) from layout (Template), enabling the same data to be rendered in RTF Word documents, Excel spreadsheets, PDFs, HTML, and more. Key capabilities include bursting (splitting and delivering reports per recipient) and scheduling.

---

## Architecture

```
Data Model (SQL / Subject Area / Web Service)
        ↓
  Publisher Engine
        ↓
Template (RTF / XPT / Excel / eText / XSL)
        ↓
  Output: PDF / Excel / Word / HTML / CSV
        ↓
  Delivery: Email / FTP / Printer / Content Server / OAC Catalog
```

---

## Data Models

A Data Model defines **where data comes from** and **how it's structured** for a report.

### Data Set Types
| Type | Description |
|---|---|
| **SQL Query** | Direct SQL against any connection |
| **OBIEE (Subject Area)** | Logical SQL against OAC Subject Area |
| **Web Service** | SOAP/REST call returns XML/JSON data |
| **XML File** | Static or parameter-driven XML |
| **Excel** | Excel file as data source |
| **View Object** | ADF View Object (Fusion Apps) |

### Data Model Features
- **Parameters**: user-input values that filter the report
- **List of Values (LOV)**: dropdowns for parameter selection (SQL-backed)
- **Bursting Definition**: defines how to split and deliver the report
- **Event Triggers**: PL/SQL procedures before/after report execution
- **Structure**: hierarchical data sets linked by keys (parent-child data)

---

## Templates

Templates control the visual layout of the report output.

### RTF Template (Most Common)
- Created in Microsoft Word with BI Publisher add-in (Template Builder)
- Uses field codes in `<?...?>` syntax
- Supports: tables, charts, images, conditional sections, loops

```rtf
<?for-each:ROW?>
  <?PRODUCT_NAME?>  <?REVENUE?>
<?end for-each?>

-- Conditional
<?if:REVENUE > 100000?>
  Top Performer
<?end if?>

-- Total
<?sum(REVENUE)?>
```

### XPT Template
- OAC's native template format
- Built in the Layout Editor (browser-based, drag-and-drop)
- Best for: complex tabular layouts, pivot tables in reports
- Supports charts natively

### Excel Template
- Excel-based template for tabular data delivery
- Field references: `<?COLUMN_NAME?>`

### eText Template
- For EDI, fixed-width text outputs (bank files, government filings)

### PDF Template
- Fill existing PDF form fields with data

---

## Creating a Report (End-to-End)

1. **Publisher Catalog** → **New** → **Report**
2. Select or create a **Data Model**
3. **Layout** tab → **Add** → choose template type
4. Design layout using Layout Editor or upload RTF template
5. Preview with sample data
6. Save report to catalog
7. Schedule or run on-demand

---

## Parameters

Report parameters let users filter data before running the report.

### Parameter Types
| Type | Control |
|---|---|
| Text | Free-text input |
| Menu (LOV) | Dropdown from SQL query |
| Date | Calendar picker |
| Boolean | Checkbox |
| Hidden | Passed programmatically (bursting, links) |

### Passing Parameters
- **Run Report**: UI shows parameter form before rendering
- **URL**: `https://<oac>/xmlpserver/path/to/report.xdo?P_YEAR=2024&P_REGION=EMEA`
- **Schedule**: embed values in the schedule job
- **Bursting**: values driven by bursting query

---

## Bursting

Bursting splits a single report into multiple outputs and delivers each to a different recipient.

### How It Works
1. A **bursting query** in the Data Model returns: `SPLIT_KEY`, `DELIVERY_CHANNEL`, `DELIVERY_ADDRESS`, `LOCALE`, `TEMPLATE`
2. Publisher groups data by `SPLIT_KEY`, renders each group with the specified template/locale
3. Delivers each output to the specified address

### Example Bursting Query
```sql
SELECT 
  REGION_CODE          AS SPLIT_KEY,
  'EMAIL'              AS DEL_CHANNEL,
  MANAGER_EMAIL        AS DEL_ADDRESS,
  'en-US'              AS LOCALE,
  'Sales_Report'       AS TEMPLATE,
  'PDF'                AS OUTPUT_FORMAT
FROM REGION_MANAGERS
```

### Delivery Channels
| Channel | Config Required |
|---|---|
| Email | SMTP server configuration |
| FTP/SFTP | Server host, port, credentials |
| WebDAV | URL, credentials |
| Printer | CUPS/IPP printer definition |
| OAC Catalog | Save to /Shared Folders path |
| Content Server (UCM) | UCM connection |
| FAX | FTP-to-fax gateway |

---

## Scheduling

Reports can be scheduled to run automatically.

### Schedule Options
- **Frequency**: once, hourly, daily, weekly, monthly, cron expression
- **Output format**: PDF, Excel, HTML, CSV
- **Delivery**: email list, FTP, catalog folder
- **Notification**: email on success/failure

### Creating a Schedule
**Report** → **Schedule** → **New Schedule**:
1. Set frequency and start/end dates
2. Set parameter values
3. Choose delivery
4. Save schedule

---

## Report Security

- Reports inherit catalog folder permissions
- Data Model permissions control who can use/modify the data model
- Row-level security applied at the Data Model SQL or via Subject Area RLS
- Parameters can be hidden and pre-populated to restrict data

---

## BI Publisher vs. Classic Analysis

| Aspect | BI Publisher | Classic Analysis |
|---|---|---|
| Output format | PDF, Excel, Word, HTML | HTML, PDF, Excel |
| Pixel-perfect layout | Yes | No |
| Template tool | Word + add-in | Browser-based |
| Bursting | Yes | No (use Agents) |
| Best for | Invoices, regulatory reports | Interactive dashboards, ad-hoc |

---

## Related
- [Classic Dashboards & Analyses](Classic%20Dashboards%20%26%20Analyses.md){ .wikilink }
- [KPIs, Alerts & Notifications](KPIs%2C%20Alerts%20%26%20Notifications.md){ .wikilink }
- [Data Sources & Connections](Data%20Sources%20%26%20Connections.md){ .wikilink }
- [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }
- [Logical SQL Reference](Logical%20SQL%20Reference.md){ .wikilink }
- [Migration, Snapshots & Lifecycle](Migration%2C%20Snapshots%20%26%20Lifecycle.md){ .wikilink }
- [APIs, Embedding & Integration](APIs%2C%20Embedding%20%26%20Integration.md){ .wikilink }
