# Data Flows & Data Preparation

> **Last updated:** 2026-04-27
> **Tags:** data flow, data preparation, ETL, transform, machine learning, output, dataset

## Summary
Data Flows are OAC's built-in ETL/ELT tool for preparing, cleansing, enriching, joining, and transforming data. They read from one or more sources (connections, datasets, Subject Areas), apply transformation steps, and write to an output (Dataset, Database, Object Storage). Data Flows can also apply Machine Learning models as pipeline steps.

---

## What Is a Data Flow?

A Data Flow is a visual, step-by-step pipeline:

```
[Source 1] ──┐
              ├── [Join] → [Filter] → [Rename Columns] → [Add Calculation] → [Output: Dataset]
[Source 2] ──┘
```

### When to Use Data Flows
- Pre-join multiple tables before visualization
- Cleanse and standardize raw data (nulls, formats, case)
- Aggregate/summarize data for performance
- Apply ML models (scoring / prediction)
- Load results into a database table
- Schedule recurring data preparation jobs

---

## Data Flow Sources

| Source Type | Description |
|---|---|
| **Dataset** | Existing OAC dataset |
| **Connection** (DB table) | Direct table from a registered connection |
| **Subject Area** | Logical SQL query result |
| **Object Storage** | OCI Object Storage file |
| **Dropbox / Google Drive** | Cloud file source |

---

## Transformation Steps

### Data Shaping
| Step | Purpose |
|---|---|
| **Select Columns** | Choose which columns to keep |
| **Rename Columns** | Change column display names |
| **Add Columns** | Add a calculated/derived column |
| **Filter Rows** | Keep or remove rows by condition |
| **Sort** | Order rows |

### Data Cleaning
| Step | Purpose |
|---|---|
| **Null Handling** | Replace nulls with default value |
| **Data Type Convert** | Change column type (string→date, etc.) |
| **Case Conversion** | Upper, lower, title case |
| **Trim Whitespace** | Remove leading/trailing spaces |

### Data Enrichment
| Step | Purpose |
|---|---|
| **Add Custom Date** | Extract year, quarter, month from date |
| **Enrich (Geography)** | Geocode address columns |
| **Sentiment Analysis** | Classify text column sentiment (positive/negative) |
| **System Connection (ML)** | Apply a trained OML model |

### Data Integration
| Step | Purpose |
|---|---|
| **Join** | Inner, left, right, full outer join between two sources |
| **Union Rows** | Append rows from two sources (same schema) |
| **Group By** | Aggregate — SUM, COUNT, AVG by dimension |
| **Branch** | Split pipeline into two paths |
| **Merge** | Combine two branches back |

### Machine Learning Steps
| Step | Purpose |
|---|---|
| **Train Numeric Prediction** | Train a regression model |
| **Train Binary Classifier** | Train a binary classification model |
| **Train Multi-Classifier** | Train a multi-class classification model |
| **Train Clustering** | Train a K-Means clustering model |
| **Apply Model** | Score rows using a trained model |

---

## Output Targets

| Output | Description |
|---|---|
| **Dataset** | Save result as OAC in-memory dataset |
| **Database Table** | Write to a table in a registered connection |
| **OCI Object Storage** | Write as Parquet/CSV to OCI bucket |
| **Dropbox / Google Drive** | Write file to cloud storage |

### Output Modes
- **Replace**: overwrite existing data
- **Append**: add rows to existing dataset
- **Merge (Upsert)**: update matching rows, insert new ones

---

## Scheduling Data Flows

Data Flows can run on a schedule:

1. Open Data Flow → **Schedule** tab
2. Set frequency: hourly, daily, weekly
3. Set start time and timezone
4. Optionally chain: run Data Flow B after Data Flow A completes

---

## Sequences

A **Sequence** is an orchestration container that runs multiple Data Flows in order:
```
Sequence: "Daily ETL"
  Step 1: Run "Load Sales Data" Data Flow
  Step 2: Run "Calculate KPIs" Data Flow
  Step 3: Run "Load to Reporting DB" Data Flow
```

---

## Data Preparation (Dataset Editor)

Separate from Data Flows, the Dataset Editor provides in-situ data prep:
- Applied when creating/editing a Dataset
- Non-destructive transformations stored as metadata
- Recommendations engine suggests fixes (nulls, obvious mismatches)
- Changes are applied at query time (not persisted to source)

### Recommendations
OAC analyzes the dataset and suggests:
- Fill nulls with median/mean/mode
- Correct date formats
- Standardize text values (e.g., "USA" and "United States" → same value)
- Extract parts from strings

---

## Data Flow Expression Language

Used in **Add Columns** and **Filter** steps:

```
-- Calculated column
REVENUE - COST

-- Conditional
CASE WHEN REGION = 'EMEA' THEN 'Europe' 
     WHEN REGION = 'AMER' THEN 'Americas'
     ELSE 'Other' END

-- Date extract
YEAR(ORDER_DATE)

-- String operations
UPPER(TRIM(CUSTOMER_NAME))

-- Null handling
COALESCE(DISCOUNT, 0)
```

---

## Performance Tips

> 💡 Tip: Use **Group By** in a Data Flow to pre-aggregate large tables. Workbook queries against aggregated datasets are much faster.

> 💡 Tip: Write large Data Flow outputs to Oracle Autonomous Database (ADW) for best downstream query performance.

> ⚠️ Warning: Data Flows loading data into OAC in-memory datasets have a size limit (~250MB compressed). For larger data, write to a database and connect via Subject Area.

> 💡 Tip: Use Sequences to orchestrate dependent Data Flows and ensure proper execution order.

---

## Related
- [Subject Areas & Datasets](Subject%20Areas%20%26%20Datasets.md){ .wikilink }
- [Machine Learning & AI Features](Machine%20Learning%20%26%20AI%20Features.md){ .wikilink }
- [Data Sources & Connections](Data%20Sources%20%26%20Connections.md){ .wikilink }
- [Workbooks & Visualizations](Workbooks%20%26%20Visualizations.md){ .wikilink }
- [Administration & Service Console](Administration%20%26%20Service%20Console.md){ .wikilink }
