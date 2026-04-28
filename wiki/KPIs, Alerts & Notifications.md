# KPIs, Alerts & Notifications

> **Last updated:** 2026-04-27
> **Tags:** KPI, alert, agent, notification, scorecard, watchlist, delivery


📖 **Full Oracle Documentation**: [Visualizing Data — KPIs and Agents](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/)

## Summary
OAC provides two systems for metric monitoring and alerting: **KPI Watchlists** (self-service, Workbook-based metric tracking) and **Agents** (Classic, rule-based scheduled delivery of analyses with conditional alerts). Together they enable business users to monitor KPIs, receive automated alerts, and schedule report distributions.

---

## KPI Watchlists (Modern)

### What Is a KPI Watchlist?
A Watchlist is a personalized dashboard of KPI cards that each show a single metric with status (green/yellow/red), trend, and target comparison.

### Creating a KPI

1. **Home** → **Create** → **KPI**
2. Select a Dataset or Subject Area
3. Configure:
   - **Metric**: the measure to display (e.g., Revenue)
   - **Target**: fixed value, or a column from the data
   - **Status rules**: define thresholds for Good / Warning / Critical
   - **Related dimensions**: for context (e.g., by Region, by Product)
   - **Time dimension**: for trend line
4. Save KPI to catalog

### KPI Status Rules Example
```
Revenue KPI:
  Good (Green):    Actual >= 100% of Target
  Warning (Amber): Actual >= 80% of Target
  Critical (Red):  Actual < 80% of Target
```

### KPI Watchlist
A Watchlist groups multiple KPIs on one page:

- **Create** → **Watchlist** → add KPIs
- Displays KPI cards in a grid
- Each card shows: current value, status indicator, trend sparkline, vs. target
- Drill into a KPI to see detail breakdown

### Adding KPIs to a Workbook
Drag a KPI tile from the Catalog onto a Workbook canvas for integrated dashboards.

---

## Scorecards (Classic)

### What Is a Scorecard?
Scorecards (from Classic/OBIEE) implement Balanced Scorecard methodology:

- **Objectives** — strategic goals
- **KPIs** — measurable outcomes
- **Initiatives** — programs to achieve objectives
- **Perspectives** — groupings (Financial, Customer, Process, Learning)

### Scorecard Components
| Component | Description |
|---|---|
| **Objective** | A strategic goal with status rollup |
| **KPI** | A metric that measures progress toward an objective |
| **Initiative** | An activity that supports an objective |
| **Cause-Effect Link** | Visual dependency between objectives |
| **Strategy Map** | Visual diagram of objective relationships |
| **Strategy Tree** | Hierarchy view of objectives → KPIs |

### KPI in Classic Scorecards
Classic KPIs differ from modern KPI Watchlists:

- Defined via KPI Editor (Answers → New → KPI)
- Support dimensional pinning (e.g., "Revenue" always shown for "Region = EMEA")
- Support override and annotation (user can explain status)
- Status rollup from child to parent objectives

---

## Agents (Scheduled Alerts & Deliveries)

### What Is an Agent?
An Agent is a scheduled job that:

1. Runs an Analysis or Dashboard
2. Evaluates a condition (optional)
3. Delivers the results to recipients via email, OAC Inbox, or other channels

### Agent Types
| Type | Trigger | Delivery |
|---|---|---|
| **Scheduled** | Time-based cron schedule | Email, Catalog, FTP |
| **Condition-Based** | Fires only when condition is met | Email alert |
| **Chained** | Triggered by another agent | Any delivery |

### Creating an Agent

1. **Catalog** → **New** → **Agent**
2. **General** tab:
   - Trigger: Daily/Weekly/Monthly + time
   - Priority: Normal / High
3. **Condition** tab (optional):
   - Select an analysis
   - Condition: "If analysis returns rows" → only fire if data matches
   - Example: Revenue drops below threshold → send alert
4. **Delivery Content** tab:
   - Select analysis or dashboard to deliver
   - Format: HTML, PDF, CSV, Excel
5. **Recipients** tab:
   - Specific users/groups
   - Dynamic: from a column in the analysis (e.g., manager email)
6. **Destinations** tab:
   - Email (requires SMTP config)
   - OAC Inbox (in-app notification)
   - Saved to Catalog folder
   - Mobile push notification (if OAC Mobile configured)
7. Save and enable

### Condition Example
```
Analysis: "Daily Revenue Alert"
SQL: SELECT REGION, REVENUE FROM "Sales" WHERE REVENUE < 50000

Agent Condition: "Deliver if analysis returns rows"
→ Agent fires only on days when any region has Revenue < 50000
→ Email sent to the Regional Manager with the alert
```

### Dynamic Delivery (Bursting to Users)
Use an analysis that returns recipient details:
```sql
SELECT MANAGER_EMAIL, REGION, REVENUE 
FROM "Sales"."Manager Assignment"
WHERE REVENUE < 50000
```
Agent delivers to each `MANAGER_EMAIL` with their specific `REGION` data.

---

## OAC Inbox (In-App Notifications)

When Agents deliver to "OAC Inbox":

- Recipients see a bell notification icon in OAC header
- Clicking opens the delivered content
- Notifications persist until dismissed

---

## Setting Up Email for Agents

**Administration** → **Manage Email**:
- SMTP host, port
- TLS/SSL settings
- Sender name and email address
- Test email configuration

---

## Push Notifications (Mobile)

For Oracle Analytics mobile app users:

- Agents can send push notifications
- Configure Mobile in Service Console
- Recipient must have the OAC mobile app installed and logged in

---

## Alert Best Practices

> 💡 Tip: Use condition-based Agents rather than always-fire agents for exception alerting — reduce email noise.

> 💡 Tip: Set Agent priority to **High** for critical business alerts (e.g., system downtime, revenue threshold breach).

> ⚠️ Warning: Agents run on the OAC server. Many concurrent agents at the same time can impact query performance. Stagger schedules.

> 💡 Tip: Test delivery by setting the agent to fire immediately ("Run Now") before scheduling it.

---

## Related
- [Classic Dashboards & Analyses](Classic%20Dashboards%20%26%20Analyses.md){ .wikilink }
- [Workbooks & Visualizations](Workbooks%20%26%20Visualizations.md){ .wikilink }
- [Administration & Service Console](Administration%20%26%20Service%20Console.md){ .wikilink }
- [BI Publisher](BI%20Publisher.md){ .wikilink }
- [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }
