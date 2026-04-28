# Logical SQL Reference

> **Last updated:** 2026-04-27
> **Tags:** logical SQL, LSQL, query language, functions, time series, variables, XSA, syntax

## Summary
Logical SQL is Oracle Analytics Cloud's query language for the Presentation/Semantic layer. It looks like standard SQL but operates on Subject Area column names rather than physical table/column names. The BI Server translates Logical SQL into optimized physical SQL for the underlying database. All OAC analyses, Workbook data requests, and API queries ultimately use Logical SQL.

---

## Basic Syntax

```sql
SELECT 
  "Subject Area"."Folder"."Column1",
  "Subject Area"."Folder"."Measure1"
FROM "Subject Area"
WHERE "Subject Area"."Folder"."Column1" = 'Value'
ORDER BY "Subject Area"."Folder"."Measure1" DESC
FETCH FIRST 100 ROWS ONLY
```

### Naming Convention
- Three-part name: `"Subject Area"."Folder"."Column"`
- Always use double quotes
- Case-sensitive for Subject Area and folder names
- Spaces are allowed inside double quotes

---

## SELECT Clause

```sql
-- Attribute
SELECT "Sales"."Product"."Category"

-- Measure (aggregated automatically)
SELECT "Sales"."Facts"."Revenue"

-- Expression / calculation
SELECT "Sales"."Facts"."Revenue" / "Sales"."Facts"."Units" AS "Avg Price"

-- Distinct count
SELECT COUNT(DISTINCT "Sales"."Customer"."Customer ID")
```

---

## WHERE Clause

```sql
-- Equality
WHERE "Sales"."Time"."Year" = 2024

-- IN list
WHERE "Sales"."Product"."Category" IN ('Electronics', 'Clothing')

-- Range
WHERE "Sales"."Facts"."Revenue" BETWEEN 10000 AND 50000

-- LIKE
WHERE "Sales"."Customer"."Name" LIKE 'Oracle%'

-- NULL check
WHERE "Sales"."Order"."Ship Date" IS NULL

-- Multiple conditions
WHERE "Sales"."Time"."Year" = 2024 
  AND "Sales"."Product"."Category" = 'Electronics'
```

---

## ORDER BY and FETCH

```sql
ORDER BY "Sales"."Facts"."Revenue" DESC

-- Limit rows
FETCH FIRST 50 ROWS ONLY

-- Pagination
FETCH FIRST 50 ROWS ONLY OFFSET 100
```

---

## Aggregate Functions

```sql
SUM("Sales"."Facts"."Revenue")
COUNT("Sales"."Order"."Order ID")
COUNT(DISTINCT "Sales"."Customer"."Customer ID")
AVG("Sales"."Facts"."Revenue")
MIN("Sales"."Facts"."Revenue")
MAX("Sales"."Facts"."Revenue")
MEDIAN("Sales"."Facts"."Revenue")
```

> 💡 **Tip:** Measures defined in the Semantic Model have predefined aggregation. Simply SELECTing a measure applies its default aggregation. Only use explicit aggregation functions for custom calculations.

---

## Time Series Functions

### AGO — Period Comparison
```sql
-- Revenue same period 1 year ago
AGO("Sales"."Facts"."Revenue", "Sales"."Time"."Month", 12)

-- Revenue previous quarter
AGO("Sales"."Facts"."Revenue", "Sales"."Time"."Quarter", 1)
```

### TODATE — Year-to-Date / Period-to-Date
```sql
-- Year-to-date revenue
TODATE("Sales"."Facts"."Revenue", "Sales"."Time"."Year")

-- Quarter-to-date
TODATE("Sales"."Facts"."Revenue", "Sales"."Time"."Quarter")
```

### PERIODROLLING — Rolling Window
```sql
-- Rolling 3-month sum
PERIODROLLING("Sales"."Facts"."Revenue", -2, 0)

-- Rolling 12-month average
PERIODROLLING("Sales"."Facts"."Revenue", -11, 0) / 12
```

> ⚠️ **Warning:** Time series functions require a time dimension column in the SELECT. They will error if no time grain is selected.

---

## Ranking Functions

```sql
-- Rank by measure (1 = highest)
RANK("Sales"."Facts"."Revenue" BY "Sales"."Product"."Category")

-- Dense rank (no gaps)
DENSE_RANK("Sales"."Facts"."Revenue" BY "Sales"."Product"."Category")

-- Top N filter
TOPN("Sales"."Facts"."Revenue", 10)

-- Bottom N filter
BOTTOMN("Sales"."Facts"."Revenue", 5)

-- Percentile rank (0-100)
NTILE("Sales"."Facts"."Revenue", 4)  -- Quartile
```

---

## Running Aggregates (Cumulative)

```sql
-- Running sum
RSUM("Sales"."Facts"."Revenue")

-- Running average
RAVG("Sales"."Facts"."Revenue")

-- Running count
RCOUNT("Sales"."Facts"."Revenue")

-- Running minimum / maximum
RMIN("Sales"."Facts"."Revenue")
RMAX("Sales"."Facts"."Revenue")
```

---

## String Functions

```sql
UPPER("Sales"."Customer"."Name")
LOWER("Sales"."Customer"."Name")
INITCAP("Sales"."Customer"."Name")
LENGTH("Sales"."Customer"."Name")
SUBSTRING("Sales"."Customer"."Name", 1, 10)
CONCAT("First Name", ' ', "Last Name")
REPLACE("Sales"."Product"."SKU", '-', '')
TRIM("Sales"."Customer"."Name")
LEFT("Sales"."Customer"."Name", 5)
RIGHT("Sales"."Customer"."Name", 3)
```

---

## Numeric Functions

```sql
ROUND("Sales"."Facts"."Revenue", 2)
CEIL("Sales"."Facts"."Revenue")
FLOOR("Sales"."Facts"."Revenue")
ABS("Sales"."Facts"."Variance")
MOD("Sales"."Order"."Order ID", 10)
POWER("Sales"."Facts"."Growth", 2)
SQRT("Sales"."Facts"."Variance")
LOG("Sales"."Facts"."Revenue", 10)
EXP("Sales"."Facts"."Rate")
```

---

## Date Functions

```sql
-- Extract parts
YEAR("Sales"."Time"."Order Date")
MONTH("Sales"."Time"."Order Date")
DAYOFMONTH("Sales"."Time"."Order Date")
DAYOFWEEK("Sales"."Time"."Order Date")
QUARTER("Sales"."Time"."Order Date")
HOUR("Sales"."Time"."Order Timestamp")

-- Difference between dates
TIMESTAMPDIFF(SQL_TSI_DAY, "Ship Date", "Order Date")
TIMESTAMPDIFF(SQL_TSI_MONTH, "Start Date", "End Date")

-- Date arithmetic
TIMESTAMPADD(SQL_TSI_DAY, 7, "Sales"."Time"."Order Date")

-- Current date/time
CURRENT_DATE
CURRENT_TIMESTAMP
NOW()
```

---

## Conditional (CASE/IF)

```sql
-- Simple CASE
CASE "Sales"."Product"."Category"
  WHEN 'Electronics' THEN 'Tech'
  WHEN 'Clothing' THEN 'Apparel'
  ELSE 'Other'
END

-- Searched CASE
CASE 
  WHEN "Sales"."Facts"."Revenue" > 100000 THEN 'High'
  WHEN "Sales"."Facts"."Revenue" > 50000 THEN 'Medium'
  ELSE 'Low'
END

-- IF shorthand
IFNULL("Sales"."Facts"."Revenue", 0)
NULLIF("Sales"."Facts"."Cost", 0)
COALESCE("Sales"."Facts"."Alt Revenue", "Sales"."Facts"."Revenue", 0)
```

---

## Variables in Logical SQL

```sql
-- Session variable
VALUEOF(NQ_SESSION.USER)
VALUEOF(NQ_SESSION.REGION)

-- Repository variable
VALUEOF(CURRENT_FISCAL_YEAR)

-- Presentation variable (set by dashboard prompts)
'@{myPromptVar}{default_value}'

-- Request variable (pass in query)
VALUEOF(NQ_REQUEST.MY_VAR)
```

---

## XSA (Extended Subject Area / Dataset) Queries

```sql
-- Basic XSA query
SELECT 
  XSA('admin'.'sales_upload')."Sheet1"."Region",
  SUM(OVERRIDEAGGR(XSA('admin'.'sales_upload')."Sheet1"."Revenue"))
FROM XSA('admin'.'sales_upload')
ORDER BY 2 DESC
FETCH FIRST 50 ROWS ONLY
```

> 💡 **Tip:** Use `OVERRIDEAGGR()` around XSA measures because they don't have predefined aggregation rules like Subject Area measures do.

---

## FILTER Function (Conditional Aggregation)

```sql
-- Revenue only for Electronics category
FILTER("Sales"."Facts"."Revenue" USING "Sales"."Product"."Category" = 'Electronics')

-- Count of orders above $1000
FILTER(COUNT("Sales"."Order"."Order ID") USING "Sales"."Facts"."Revenue" > 1000)
```

---

## EVALUATE (Native DB Function Passthrough)

Call database-specific functions not available in Logical SQL:
```sql
-- Oracle-specific regex
EVALUATE('REGEXP_SUBSTR(%1, %2)', "Sales"."Customer"."Email", '@(.+)$')

-- Oracle-specific analytic function
EVALUATE('LISTAGG(%1, %2) WITHIN GROUP (ORDER BY %3)', 
  "Sales"."Product"."Name", ', ', "Sales"."Facts"."Revenue")
```

> ⚠️ **Warning:** `EVALUATE` bypasses the Logical SQL layer and sends raw SQL to the database. It is DB-specific and not portable.

---

## Common Query Patterns

### YTD vs Prior YTD Comparison
```sql
SELECT 
  "Sales"."Time"."Year",
  TODATE("Sales"."Facts"."Revenue", "Sales"."Time"."Year") AS "YTD Revenue",
  AGO(TODATE("Sales"."Facts"."Revenue", "Sales"."Time"."Year"), 
      "Sales"."Time"."Year", 1) AS "Prior YTD Revenue"
FROM "Sales"
```

### Top 10 with Percentage of Total
```sql
SELECT 
  "Sales"."Product"."Product Name",
  "Sales"."Facts"."Revenue",
  "Sales"."Facts"."Revenue" / SUM("Sales"."Facts"."Revenue") * 100 AS "% of Total"
FROM "Sales"
WHERE TOPN("Sales"."Facts"."Revenue", 10) <= 10
ORDER BY "Sales"."Facts"."Revenue" DESC
```

---

## Related
- [Semantic Model](Semantic%20Model.md){ .wikilink }
- [Subject Areas & Datasets](Subject%20Areas%20%26%20Datasets.md){ .wikilink }
- [Classic Dashboards & Analyses](Classic%20Dashboards%20%26%20Analyses.md){ .wikilink }
- [APIs, Embedding & Integration](APIs%2C%20Embedding%20%26%20Integration.md){ .wikilink }
