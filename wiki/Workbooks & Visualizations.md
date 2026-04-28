# Workbooks & Visualizations

> **Last updated:** 2026-04-27
> **Tags:** workbook, canvas, visualization, chart, filter, calculation, storytelling, self-service

## Summary
Workbooks are OAC's modern self-service analytics interface. A Workbook contains one or more **Canvases** (pages), each with **Visualizations** built from Datasets or Subject Areas. Workbooks support rich interactivity, AI-powered insights, map visualizations, and narration for storytelling.

---

## Workbook Structure

```
Workbook
  ├── Canvas 1 (e.g., "Executive Summary")
  │     ├── Visualization: Revenue Trend (Line Chart)
  │     ├── Visualization: Top Products (Bar Chart)
  │     └── Filter: Year = 2024
  ├── Canvas 2 (e.g., "Regional Detail")
  │     └── Visualization: Sales by Region (Map)
  └── Canvas 3 (e.g., "Story")
        └── Narration text + embedded viz
```

---

## Creating a Workbook

1. **Home** → **Create** → **Workbook**
2. Select a Dataset or Subject Area as the data source
3. Drag columns from the Data Panel onto the canvas
4. OAC auto-suggests a visualization type based on the data
5. Customize the chart, add filters, save

---

## Visualization Types

### Standard Charts
| Type | Best For |
|---|---|
| **Bar / Horizontal Bar** | Comparing categories |
| **Line** | Trends over time |
| **Area** | Cumulative trends |
| **Combo (Bar+Line)** | Two metrics with different scales |
| **Scatter** | Correlation between two measures |
| **Bubble** | Three-measure correlation (size = 3rd metric) |
| **Pie / Donut** | Part-to-whole (use sparingly, max 5-7 slices) |
| **Treemap** | Hierarchical part-to-whole |
| **Waterfall** | Incremental changes |
| **Funnel** | Stage-based conversion |
| **Box Plot** | Statistical distribution |
| **Radar / Spider** | Multi-dimensional comparison |

### Data Tables
| Type | Best For |
|---|---|
| **Table** | Detailed row data |
| **Pivot Table** | Cross-tabulation |
| **Heat Matrix** | Density / frequency across two dimensions |

### Spatial
| Type | Best For |
|---|---|
| **Map** | Geographic data |
| **Flow Map** | Origin-destination |

### KPI / Summary
| Type | Best For |
|---|---|
| **Tile (KPI Card)** | Single metric highlight |
| **Language Narrative** | Auto-generated text summary |
| **Custom Plug-in** | Third-party chart types |

---

## Grammar Panel (Properties)

Each visualization has a Grammar Panel with:
- **Columns**: assign data to X, Y, Color, Size, Shape, Tooltip, Trellis axes
- **Properties**: title, legend, axis labels, data labels, colors, sorting
- **Filters**: local filters scoped to this viz only
- **Analytics**: trend lines, reference lines, clusters, outliers, forecast

---

## Filters

### Canvas Filters
Apply to all visualizations on a canvas:
- Add via the Filter Bar at the top of the canvas
- Range, list, date range, or expression filters
- Can be pinned across canvases

### Visualization Filters
Apply only to one visualization:
- Right-click column → **Add Filter**

### Dashboard Filters (Workbook-Level)
Pin a filter to apply across all canvases.

### Filter Types
| Type | Usage |
|---|---|
| **List** | Select one or more values from a list |
| **Range** | Min/Max numeric range |
| **Date Range** | Relative ("Last 30 Days") or absolute |
| **Expression** | Custom formula filter |
| **Top/Bottom N** | Filter to top or bottom N values |

---

## Calculations

### Add Calculation to Dataset
1. Data Panel → Right-click column → **Add Calculation**
2. Expression editor with functions, operators, and column references

### Common Functions
```
-- String
CONCAT("First Name", ' ', "Last Name")
UPPER("Product Name")
SUBSTRING("Description", 1, 50)

-- Numeric
ROUND("Revenue" / "Units", 2)
ABS("Variance")
POWER("Growth Rate", 2)

-- Date
YEAR("Order Date")
MONTH("Order Date")
TIMESTAMPDIFF(SQL_TSI_DAY, "Ship Date", "Order Date")

-- Conditional
CASE WHEN "Revenue" > 100000 THEN 'High' 
     WHEN "Revenue" > 50000 THEN 'Medium'
     ELSE 'Low' END
```

---

## Canvas Properties

- **Background**: color, image
- **Canvas Size**: auto, fixed pixel, 1920×1080 (presentation mode)
- **Grid**: snap to grid, grid spacing
- **Refresh**: manual or auto-refresh interval

---

## Presentation Mode & Stories

### Presentation Mode
Full-screen view of a canvas for dashboarding/presenting.
- `View` → `Present`
- Navigate between canvases with arrows

### Story Mode (Narration)
Add text, images, and embedded visualizations for guided analytics:
1. Add a **Narration** canvas
2. Drag in text boxes and viz thumbnails
3. Present as a slide-style story

---

## Collaboration & Sharing

- **Share link**: copy URL to share (recipient needs OAC access)
- **Export**: download as PDF, PNG, PowerPoint, Data (CSV/XLSX)
- **Embed**: embed canvas in external web pages (see [APIs, Embedding & Integration](APIs%2C%20Embedding%20%26%20Integration.md){ .wikilink })
- **Email**: schedule delivery via Agents (see [KPIs, Alerts & Notifications](KPIs%2C%20Alerts%20%26%20Notifications.md){ .wikilink })

---

## AI-Powered Features in Workbooks

### Explain
Auto-generates insights for a selected measure:
- Basic facts (total, average, distribution)
- Key drivers (which dimensions drive the metric)
- Segments (clusters of data)
- Anomalies (outliers)
Access: Right-click a column/measure → **Explain**

### Ask (Natural Language Query)
Type a question in plain English → OAC generates a visualization:
- "Show me revenue by region for last year"
- "Top 10 products by profit margin"

### Auto-Insights
OAC proactively surfaces interesting patterns when opening a workbook.

### AI Assistant
Generative AI (OCI AI Services backed) for chart recommendations, data descriptions, and Q&A.

---

## Performance Tips

> 💡 Tip: Limit the number of visualizations per canvas to 8-10 for best rendering performance.

> 💡 Tip: Use Dataset caching for frequently accessed self-service data.

> ⚠️ Warning: Blending large datasets client-side is slow. Pre-join in a Data Flow instead.

> 💡 Tip: Use Subject Areas (BI Server) for large data volumes — they support aggregate navigation and database pushdown.

---

## Related
- [Subject Areas & Datasets](Subject%20Areas%20%26%20Datasets.md){ .wikilink }
- [Data Flows & Data Preparation](Data%20Flows%20%26%20Data%20Preparation.md){ .wikilink }
- [Machine Learning & AI Features](Machine%20Learning%20%26%20AI%20Features.md){ .wikilink }
- [KPIs, Alerts & Notifications](KPIs%2C%20Alerts%20%26%20Notifications.md){ .wikilink }
- [APIs, Embedding & Integration](APIs%2C%20Embedding%20%26%20Integration.md){ .wikilink }
- [Classic Dashboards & Analyses](Classic%20Dashboards%20%26%20Analyses.md){ .wikilink }
