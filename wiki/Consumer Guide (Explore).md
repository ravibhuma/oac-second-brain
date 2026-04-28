# Consumer Guide (Explore)

> **Last updated:** 2026-04-27
> **Tags:** consumers, end users, viewing, exploring, interacting, business users, navigation

## Summary
This guide is for **OAC consumers** — business users who view, interact with, and explore content built by others. Consumers don't build dashboards or models; they navigate, filter, drill, comment, and share. This page covers everything an end user needs to know.

---

## Logging In

1. Navigate to your OAC URL: `https://<instance>.analytics.ocp.oraclecloud.com/ui/`
2. Sign in with corporate credentials (SSO if configured)
3. You'll land on the **Home Page**

---

## The Home Page

The home page surfaces:
- **Recent**: items you opened recently
- **Favorites**: items you starred
- **Featured**: content highlighted by admins
- **Search bar**: search across all content you have access to

### Navigation Bar
- **Hamburger menu** (☰) — full nav: Catalog, Console, Machine Learning, Mobile
- **Search** — global search
- **Create** (+) — create new workbook, dataset, etc. (if you have author permissions)
- **Notifications** (bell) — Agent deliveries, system messages
- **Profile** — preferences, sign out

---

## Finding Content

### Catalog Browser
**Hamburger** → **Catalog**:
- `/Shared Folders/` — organization-wide content
- `/My Folders/` — your personal items
- Folders represent business areas (Finance, HR, Sales)

### Search
- Type in the global search bar
- Results: dashboards, analyses, workbooks, KPIs, reports
- Filters: by type, by owner, by date

---

## Interacting with a Workbook

### Opening
Click a workbook to open it. You'll see:
- **Canvas tabs** at the bottom — click to switch pages
- **Filter bar** at the top — current filters
- **Visualizations** filling the canvas

### Filtering
- Click a filter chip → modify the filter
- Click any value in a chart → "Use as Filter" or "Drill"
- Right-click → **Keep Only** (filter to that value) or **Remove** (exclude)

### Drilling
For hierarchical data:
- Click a value (e.g., 2024) → drills to next level (Quarters)
- Breadcrumb shows current drill path
- Click any breadcrumb level to jump back

### Sorting
- Click a column header in a table → sort
- In charts: right-click → **Sort**

### Tooltips
Hover over any data point → tooltip shows exact values and additional context.

### Asking Questions (Ask)
- Click **Ask** at the top of the canvas
- Type a question: "Show revenue by region for 2024"
- OAC generates a visualization

---

## Interacting with a Classic Dashboard

Different from Workbooks (older UI):
- **Page tabs** at the top — click to navigate
- **Dashboard prompts** at the top — apply, then click Apply or hit Enter
- **Analyses** populate the page — interact: drill, sort, navigate

### Right-click Actions
On any value in an analysis:
- **Drill**: go to next hierarchy level
- **Keep Only / Remove**: ad-hoc filter
- **Action Links**: navigate to another analysis, URL, or report

---

## Viewing KPIs (Watchlists)

KPI Watchlists show key metrics with status indicators:
- **Green/Yellow/Red** — performance vs. target
- Click a KPI tile → drill to detail breakdown
- See trend sparkline next to the value

---

## Exporting Data

From any visualization or analysis:
- Right-click → **Export**
- Choose format: **PDF, PNG, PowerPoint, Excel, CSV, Data**
- "Data" exports raw query results

> 💡 **Tip:** Export to Excel for offline analysis. Export to PowerPoint for presentations — formatting is preserved.

---

## Sharing Content

### Share a Link
- Right-click an item → **Copy Link**
- Paste into email/chat — recipient must have OAC access + permissions

### Email a Snapshot
- Open workbook → **Share** → **Email**
- Sends current view as PDF

### Subscribe to Updates (Agent Subscription)
- Some analyses have an Agent set up to email scheduled updates
- Subscribe via the bell/notification icon on the analysis

---

## Personal Customizations

### Favorites
Star any item → it appears in **Home → Favorites**.

### Personal Filters
Set your default filter values for a dashboard:
- Apply filters → **Save Customization** → "Make this my default"

### Comments / Annotations
On Workbooks:
- **Comments** panel → add a comment about a data point
- @mention colleagues to notify them
- Comments are persistent across sessions

---

## Mobile Access

### Oracle Analytics Mobile App
- Download from App Store / Google Play
- Sign in with same OAC credentials
- View workbooks, dashboards, KPIs on phone or tablet
- Receive push notifications for Agent alerts

### Day by Day (Legacy)
Older mobile app for OBIEE; being replaced by Oracle Analytics app.

---

## Getting Help

### In-App Help
- Click **?** icon (top-right) → context-sensitive help
- "Show me how" tour for first-time users

### Search Documentation
- Help → **Documentation** → Oracle Analytics Cloud docs site

### Ask Your Admin
For:
- Access to a dashboard you can't see → ask the content owner
- Wrong data → contact the dashboard's owner (shown in Properties)
- Need new analysis → request from your BI team

---

## Best Practices for Consumers

> 💡 Tip: Use **Favorites** for dashboards you visit weekly — saves clicking through folders.

> 💡 Tip: Save personal filter defaults — saves applying them every time.

> 💡 Tip: Subscribe to Agents for daily/weekly KPI summaries delivered to your inbox.

> ⚠️ Warning: Don't trust exported Excel forever — data may be stale. Re-run dashboards for current data.

---

## Related
- [Workbooks & Visualizations](Workbooks%20%26%20Visualizations.md){ .wikilink }
- [Classic Dashboards & Analyses](Classic%20Dashboards%20%26%20Analyses.md){ .wikilink }
- [KPIs, Alerts & Notifications](KPIs%2C%20Alerts%20%26%20Notifications.md){ .wikilink }
- [Mobile (Oracle Analytics App)](Mobile%20%28Oracle%20Analytics%20App%29.md){ .wikilink }
