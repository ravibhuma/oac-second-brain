# Classic Dashboards & Analyses

> **Last updated:** 2026-04-27
> **Tags:** analysis, dashboard, answers, criteria, filters, prompts, actions, views, pivot, subject area


📖 **Full Oracle Documentation**: [Visualizing Data and Building Reports — Dashboards](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/)

## Summary
Classic Analyses and Dashboards are OAC's enterprise-grade reporting layer, inherited from OBIEE. Analyses are parameterized, multi-view queries against Subject Areas. Dashboards assemble analyses and other content into governed, multi-page portals. This layer supports complex conditional formatting, drill-down hierarchies, dashboard prompts, and action links.

---

## Analyses (Answers)

### What Is an Analysis?
An Analysis is a saved query against a Subject Area that can have multiple **Views** (table, chart, pivot, gauge, etc.) displayed simultaneously. It is the fundamental building block for Classic Dashboards.

### Creating an Analysis

1. **Home** → **Create** → **Analysis**
2. Select a Subject Area
3. **Criteria Tab**: drag columns to the analysis
4. **Results Tab**: view and add visualization types
5. Save to catalog

### Criteria Tab
- **Columns pane**: selected columns (dimensions + measures)
- **Filters pane**: conditions applied to the query
- **Column Properties**: format, conditional format, interaction, data format
- **Column Formulas**: override the default column formula with Logical SQL expressions

### Column Formula Override
```sql
-- Override a measure to calculate running total
RSUM("Sales"."Facts"."Revenue")

-- Override to rank
RANK("Sales"."Facts"."Revenue" BY "Sales"."Product"."Category")

-- Time comparison
AGO("Sales"."Facts"."Revenue", "Sales"."Time"."Month", 12)
```

---

## Views (Results Tab)

Each Analysis can have multiple simultaneous views:

| View Type | Description |
|---|---|
| **Table** | Flat tabular display |
| **Pivot Table** | Cross-tab with row/column/section pivoting |
| **Chart** | 30+ chart types (bar, line, pie, scatter, etc.) |
| **Gauge** | KPI dial / speedometer |
| **Funnel Chart** | Stage conversion |
| **Heat Matrix** | Density grid |
| **Trellis** | Small multiples (grid of charts) |
| **Map** | Spatial visualization |
| **Narrative** | Dynamic text with embedded measure values |
| **Ticker** | Scrolling marquee for KPI values |
| **Title** | Report header with date/time stamps |
| **Logical SQL** | Display the generated Logical SQL (debug) |
| **No Results** | Custom message when query returns no data |

---

## Filters in Analyses

### Column Filters
- Applied in the Criteria tab
- Operators: `is equal to`, `is in`, `is between`, `contains`, `starts with`, `is null`, etc.
- Protected filters: hidden from dashboard prompts
- Optional filters: user can toggle on/off

### Selection Steps
Applied after the query — rank-based, condition-based, or explicit member selection (useful for hierarchical data).

### Saved Filters
Reusable filter conditions saved to the catalog and applied across multiple analyses.

---

## Conditional Formatting

Applied per-column in Column Properties → Conditional Format:

- Highlight cells by threshold (Green/Yellow/Red traffic lights)
- Apply to measures or attributes
- Supports gradient coloring
- Conditional format on a different column (e.g., color Revenue based on Margin)

```
Rule: If Revenue < 50000 → Background = Red, Font = White
Rule: If Revenue between 50000 and 100000 → Background = Yellow
Rule: If Revenue > 100000 → Background = Green
```

---

## Dashboards

### What Is a Dashboard?
A Dashboard is an organized collection of **Dashboard Pages**, each containing analyses, images, text, links, embedded content, and **Dashboard Prompts**.

### Dashboard Structure
```
Dashboard: "Sales Executive Dashboard"
  ├── Page 1: "Summary"
  │     ├── Dashboard Prompt: Year (applies to all analyses on this page)
  │     ├── Section: KPI Row
  │     │     ├── Analysis: Total Revenue (Gauge)
  │     │     └── Analysis: YTD vs Target (Gauge)
  │     └── Section: Trend
  │           └── Analysis: Revenue by Month (Line Chart)
  ├── Page 2: "Product Detail"
  │     └── Analysis: Product Performance (Pivot Table)
  └── Page 3: "Map View"
        └── Analysis: Sales by Region (Map)
```

### Creating a Dashboard

1. **Home** → **Create** → **Dashboard**
2. Add pages
3. Drag analyses and other objects from the catalog onto the page
4. Add Dashboard Prompts
5. Configure page layout (columns, sections)
6. Set as default dashboard or publish

### Dashboard Prompts
Dashboard Prompts are interactive filters on the dashboard page that filter all analyses on that page (or across pages if scoped globally).

| Prompt Type | Description |
|---|---|
| **Column Prompt** | Filter on a specific column value |
| **Variable Prompt** | Set a presentation variable used in column formulas |
| **Image Prompt** | Clickable image triggers a filter |
| **Currency Prompt** | Switch currency display |

#### Column Prompt Options
- Control type: Select List, Check Box, Radio Button, Text Field, Slider, Calendar
- Default values: no default, specific value, SQL-based dynamic default
- Cascading prompts: values in Prompt B depend on selection in Prompt A

---

## Actions (Action Links & Action Menus)

Actions enable navigation and interactivity:

### Action Types
| Type | What It Does |
|---|---|
| **Navigate to Analysis** | Drill from one analysis to another |
| **Navigate to Dashboard Page** | Navigate between dashboard pages |
| **Navigate to URL** | Open any URL (pass column values as parameters) |
| **Navigate to BI Publisher Report** | Link to a Publisher report with parameters |
| **Invoke a Web Service** | Call a SOAP/REST endpoint |
| **Invoke an Agent** | Trigger an OAC Agent delivery |
| **Navigate to E-Business Suite** | Deep link to EBS form |
| **Navigate to Siebel CRM** | Deep link to Siebel record |

### Action Links
Attach actions to column values, column headings, or graph elements.

### Named Actions
Saved reusable actions in the catalog.

---

## Analysis Interactions

### Drill
Click a hierarchy member to drill to the next level:

- Drill is enabled by default for hierarchy columns
- Behavior defined in Subject Area hierarchy settings

### Sort
Click column headers to sort ascending/descending.

### Move Columns
Drag columns in results to reorder.

### Include/Exclude
Right-click a value → **Keep Only** / **Remove** for ad-hoc filtering.

---

## Catalog Management

Analyses and Dashboards are stored in the **Catalog**:

- `/Shared Folders/` — shared content, governed
- `/My Folders/` — personal content, not shared
- Folders support permissions (Full Control, Modify, Read, No Access)

### Best Practices
> 💡 Tip: Store production dashboards under `/Shared Folders/` with restricted modify permissions.

> ⚠️ Warning: Objects in `/My Folders/` are deleted when a user is removed from the system.

---

## Related
- [Subject Areas & Datasets](Subject%20Areas%20%26%20Datasets.md){ .wikilink }
- [Semantic Model](Semantic%20Model.md){ .wikilink }
- [BI Publisher](BI%20Publisher.md){ .wikilink }
- [KPIs, Alerts & Notifications](KPIs%2C%20Alerts%20%26%20Notifications.md){ .wikilink }
- [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }
- [Workbooks & Visualizations](Workbooks%20%26%20Visualizations.md){ .wikilink }
