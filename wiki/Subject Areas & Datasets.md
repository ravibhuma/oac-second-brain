# Subject Areas & Datasets

> **Last updated:** 2026-04-27
> **Tags:** subject area, dataset, XSA, measures, attributes, dimensions, data blending

## Summary
OAC exposes data to users through two mechanisms: **Subject Areas** (enterprise-grade, defined in the Semantic Model) and **Datasets** (self-service, uploaded or queried directly). Subject Areas are the backbone of Classic Analyses and Dashboards; Datasets power Workbooks and can be joined together through data blending.

---

## Subject Areas

### What Is a Subject Area?
A Subject Area is a curated, business-friendly view of data defined in the Presentation Layer of the Semantic Model. It groups related dimensions and measures into **folders**, presenting a consistent, governed view to all users.

```
Subject Area: "Sales Performance"
  ├── Folder: Time
  │     ├── Year
  │     ├── Quarter
  │     └── Month
  ├── Folder: Product
  │     ├── Category
  │     └── Product Name
  ├── Folder: Customer
  │     └── Region
  └── Folder: Facts - Sales
        ├── Revenue       [MEASURE]
        ├── Units Sold    [MEASURE]
        └── Avg Price     [MEASURE]
```

### Column Types
| Type | Description | Example |
|---|---|---|
| **Attribute** | Descriptive / dimensional | Customer Name, Region, Product |
| **Measure** | Numeric, aggregatable | Revenue, Units, Count |
| **Hierarchy Level** | Part of a drill path | Year > Quarter > Month |

### Navigating Subject Areas
- **Classic Analyses**: Subject Area panel → drag columns to Criteria tab
- **Workbooks**: Add Data → Subject Area → choose columns
- **Logical SQL**: Reference as `"Subject Area"."Folder"."Column"`

---

## Datasets

### What Is a Dataset?
A Dataset is a self-service data source created by a user. It can be:
- An uploaded file (Excel, CSV)
- A query against a database connection
- A result from a Data Flow
- A blend of multiple sources

### Dataset vs. Subject Area

| Aspect | Dataset | Subject Area |
|---|---|---|
| Created by | Any user | Data modeler / Admin |
| Governed | No (self-service) | Yes (enterprise) |
| Joins | User-defined (data blending) | Pre-defined in Semantic Model |
| Used in | Workbooks | Workbooks, Analyses, Dashboards |
| Data location | OAC in-memory cache | Live query to DB via BI Server |
| Row limit | Configurable (default 250k) | No limit (live query) |

### Creating a Dataset
1. **Home** → **Create** → **Dataset**
2. Choose source: Connection, File, Subject Area, etc.
3. Select tables/sheets
4. Optionally transform in the Data Preparation editor
5. Save → Dataset available in Workbooks

### Dataset Columns
- All columns start as attributes
- User can change to **Measure** with aggregation rule
- User can set **data type**, **format**, and **aggregation**
- Hidden columns possible

---

## Extended Subject Areas (XSA)

XSAs expose Datasets as queryable sources via Logical SQL using the `XSA()` function.

```sql
-- Query a dataset via Logical SQL
SELECT XSA('admin'.'sales_data')."Orders"."Customer",
       SUM(OVERRIDEAGGR(XSA('admin'.'sales_data')."Orders"."Revenue"))
FROM XSA('admin'.'sales_data')
FETCH FIRST 100 ROWS ONLY
```

### XSA Naming
- `XSA('namespace'.'dataset_name')`
- Namespace = the username who owns the dataset (or a shared namespace)
- Dataset name = the dataset's technical name (not display name)

> 💡 **Tip:** Use `discover_data` (OAC MCP tool) to discover XSA names and subject areas available in your instance.

---

## Data Blending

Blend two or more Datasets (or Datasets + Subject Areas) in a single Workbook.

### How Blending Works
- Each data source gets its own "layer"
- OAC joins them client-side on matching column names or user-defined join keys
- Result: a merged view for visualization

### Setting Up Blends
1. In Workbook → **Data** panel → Add second dataset
2. OAC auto-detects matching columns (same name, same type)
3. Adjust match columns manually if needed
4. Choose join type: **Inner**, **Left Outer**, **Right Outer**, **Full Outer**

> ⚠️ **Warning:** Data blending joins happen in memory in the browser. Very large datasets can cause performance issues. Consider using Data Flows to pre-join data server-side.

---

## Data Preparation (Dataset Editor)

When creating or editing a dataset, the Data Preparation editor allows:
- **Rename** columns
- **Change data type** (String, Number, Date)
- **Hide** columns
- **Add enrichments**: geographic encoding, date extraction (year, quarter, month)
- **Add calculations**: formula-based derived columns
- **Recommendations**: OAC suggests data quality fixes (nulls, format issues)

---

## Related
- [[Semantic Model]]
- [[Workbooks & Visualizations]]
- [[Data Flows & Data Preparation]]
- [[Logical SQL Reference]]
- [[Classic Dashboards & Analyses]]
