# Semantic Model

> **Last updated:** 2026-04-27
> **Tags:** semantic model, RPD, data model, BI server, logical layer, physical layer, presentation layer, measures, dimensions, hierarchies

## Summary
The Semantic Model (historically called the RPD — Repository Definition File) is the heart of Oracle Analytics Cloud's enterprise analytics capability. It provides a business-friendly abstraction over raw database schemas, enabling consistent metric definitions, automatic join resolution, and cross-source federation. OAC offers two tools to build it: the modern **Semantic Modeler** (browser-based) and the legacy **Model Administration Tool** (desktop, `.rpd` file-based).

---

## Three-Layer Architecture

```
┌──────────────────────────────────────────────────┐
│  PRESENTATION LAYER  (what users see)            │
│  Subject Areas → Folders → Columns               │
│  Controls display names, visibility, sort order  │
├──────────────────────────────────────────────────┤
│  BUSINESS MODEL & MAPPING LAYER (logical model)  │
│  Logical tables, joins, measures, calculations   │
│  Single "logical" view across all physical tables│
├──────────────────────────────────────────────────┤
│  PHYSICAL LAYER  (raw database objects)          │
│  Tables, views, stored procs, physical joins     │
│  One node per connection / database              │
└──────────────────────────────────────────────────┘
```

### Physical Layer
- Represents actual database tables and views
- Each **physical database** node = one connection
- **Physical tables** map to DB tables or views
- **Physical columns** map to DB columns with data types
- **Physical joins** define foreign key relationships
- Can include **opaque views** (inline SQL as a virtual table)

### Business Model & Mapping (BMM) Layer
- One or more **Logical Tables** (dimensions or facts)
- **Logical columns** can map to multiple physical columns (federation)
- **Logical table sources (LTS)** define which physical table backs a logical table
- **Logical joins** (simplified — no ON clause needed, BI Server handles it)
- **Measures** have aggregation rules: SUM, COUNT, AVG, MIN, MAX, COUNT DISTINCT
- **Derived measures**: calculated from other logical columns (e.g., `"Revenue" / "Units"`)

### Presentation Layer
- One or more **Subject Areas** exposed to users
- Each Subject Area → folders → columns
- Can rename, hide, or reorder columns from the BMM layer
- Presentation columns can be marked as hidden (not visible in UI)

---

## Semantic Modeler (Browser-Based)

Introduced in OAC 2022. Fully browser-based, no desktop tool needed.

### Key Capabilities
- Visual table diagram editor
- Integrated expression editor with auto-complete
- Import tables from connections with drag-and-drop
- Direct deploy to OAC (no file upload needed)
- Version history and change tracking
- Workspaces for collaborative development

### Navigation
```
Home → Semantic Model (tile) → Open / Create Model
  ├── Physical Layer  (tables, joins)
  ├── Logical Layer   (BMM)
  └── Presentation Layer (Subject Areas)
```

### Creating a Semantic Model (Steps)
1. **Home** → **Create** → **Semantic Model**
2. Name the model
3. **Physical Layer** → Add database → Import tables
4. Define physical joins
5. **Logical Layer** → Create business model → Map physical tables
6. Define measures (aggregation rules)
7. Create hierarchies for drill-down
8. **Presentation Layer** → Create Subject Area → Add logical columns
9. **Deploy** → saves and activates for querying

---

## Model Administration Tool (Classic RPD)

Legacy desktop tool for `.rpd` file management. Still supported in OAC.

### When to Use
- Migrating existing OBIEE/OAS RPDs to OAC
- Advanced features not yet in Semantic Modeler (e.g., initialization blocks, session variables)
- Batch scripting with OBIEE utilities

### Upload RPD to OAC
```
Service Console → Semantic Model → Upload RPD
```

> ⚠️ **Warning:** Once you start using the browser-based Semantic Modeler for a model, you cannot edit it with the Model Administration Tool (they are different formats internally).

---

## Key Concepts

### Dimensions vs. Facts
| Type | Logical Table Type | Typical Contents |
|---|---|---|
| Dimension | Dimension | Customer, Product, Time, Geography |
| Fact | Fact (measure source) | Revenue, Units, Cost, Transactions |

### Hierarchies
Enable drill-down in analyses and workbooks.

**Level-Based Hierarchy** (most common):
```
Total → Region → Country → State → City
```

**Parent-Child Hierarchy**:
Used for recursive structures (org charts, GL accounts).

### Variables

| Type | Scope | Purpose |
|---|---|---|
| **Repository Variable** | Server-wide | Static or dynamic values (e.g., current fiscal year) |
| **Session Variable** | Per-user session | User context (e.g., `NQ_SESSION.USER`, `NQ_SESSION.GROUP`) |
| **Presentation Variable** | Per-request | Dashboard prompt selections |
| **Request Variable** | Per-query | Override session variables temporarily |

**Initialization Blocks** populate Repository and Session variables at login by running a SQL query against a data source.

```sql
-- Example: Populate CURRENT_YEAR session variable
SELECT TO_CHAR(SYSDATE, 'YYYY') FROM DUAL
```

### Aggregate Navigation
The BI Server can automatically route queries to pre-aggregated tables (aggregate tables) to improve performance:
1. Define aggregate tables in the Physical Layer
2. Map them as additional Logical Table Sources in the BMM Layer
3. BI Server chooses the most appropriate aggregate level automatically

### Fragmentation / Content Filtering
Used to partition data across multiple physical sources:
- Filter by time period (e.g., LTS1 = current year, LTS2 = historical)
- Filter by region (e.g., LTS1 = EMEA, LTS2 = AMER)

---

## Expression Language (Logical)

Common expressions in logical column definitions:

```
-- Derived measure
"Fact - Sales"."Revenue" / "Fact - Sales"."Units"

-- Conditional
CASE WHEN "Dim - Customer"."Segment" = 'Premium' THEN 1 ELSE 0 END

-- Time series (within semantic model)
AGO("Fact - Sales"."Revenue", "Dim - Time"."Month", 1)
```

---

## Physical SQL vs. Logical SQL

| | Physical SQL | Logical SQL |
|---|---|---|
| Language | DB-specific (Oracle SQL, T-SQL, etc.) | OAC Logical SQL |
| Generated by | BI Server → sent to DB | Users/developers → sent to BI Server |
| Joins | Explicit | Automatic (BI Server resolves) |
| References | Physical column names | Logical presentation layer names |

---

## Best Practices

> 💡 Tip: Always define measures in the BMM layer with explicit aggregation rules. Never let them default to "none."

> 💡 Tip: Keep the Presentation Layer display names user-friendly — this is what business users see in the Subject Area picker.

> ⚠️ Warning: Circular logical joins cause infinite query loops. Always check for cycles in the BMM layer.

> 💡 Tip: Use opaque views in the Physical Layer to push complex SQL down to the database rather than processing in the BI Server.

---

## Related
- [[OAC Overview & Architecture]]
- [[Subject Areas & Datasets]]
- [[Logical SQL Reference]]
- [[Data Sources & Connections]]
- [[Migration, Snapshots & Lifecycle]]
