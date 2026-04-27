# What's New & Release Updates

> **Last updated:** 2026-04-27
> **Tags:** release notes, what's new, preview features, monthly updates, version history

## Summary
Oracle Analytics Cloud follows a monthly release cadence. New features ship continuously. This page tracks the structure of OAC's release model, where to find official what's-new info, the preview-features program, and how to opt in or defer updates.

---

## Where Oracle Publishes Release Info

| Resource | URL |
|---|---|
| What's New (current) | `docs.oracle.com/en/cloud/paas/analytics-cloud/whats-new` |
| Preview Features | `docs.oracle.com/en/cloud/paas/analytics-cloud/preview-features` |
| Release Update Schedule | OCI Console → Analytics Cloud → instance → Update history |
| Oracle Analytics Blog | https://blogs.oracle.com/analytics/ |
| YouTube "What's New" series | https://www.youtube.com/c/OracleAnalytics |

---

## Release Cadence

- **Monthly updates** to OAC (typically first or second week of each month)
- Updates are applied automatically by Oracle
- Customers can **defer one release cycle** (one month delay)
- Major paradigm shifts (e.g., new Semantic Modeler) are introduced as **Preview Features** first

---

## Preview Features Program

Preview Features are new capabilities Oracle releases for customer testing **before** general availability.

### How to Enable Preview Features
1. **Console** → **System Settings** → **Preview Features**
2. Toggle individual features on/off
3. No restart required for most features

### Typical Lifecycle
```
Preview Feature → 2-3 months in preview → General Availability (default ON) → Existing default behavior retired
```

> ⚠️ **Warning:** Preview Features may have bugs or change behavior between releases. Don't rely on them for production reports until they reach GA.

### Common Preview Features Over Time
- AI Assistant (generative AI in workbooks) — went GA in 2024
- Semantic Modeler (browser-based) — GA in 2022
- New Home Page — GA in 2023
- Dataset Recommendations — GA in 2023
- Auto Insights — GA in 2024
- Natural Language Query (Ask) — GA in 2024

---

## Major Feature Themes by Year

### 2026 (Current)
- AI Assistant deep integrations with OCI Generative AI
- Improved AutoML in Data Flows
- Expanded Semantic Modeler parity with classic RPD
- Enhanced embedding APIs

### 2025
- Conversational Analytics (chat-based Q&A)
- Improved Map visualizations
- Fusion Analytics (FAW) integration enhancements
- New REST API endpoints for catalog operations

### 2024
- AI Assistant (GenAI integration) GA
- Auto Insights GA
- Improved Semantic Modeler (more RPD features supported)
- New Workbook home page

### 2023
- Semantic Modeler (browser) — major upgrade
- New Workbook UI
- Maps performance improvements
- Predictive (AutoML) in Data Flows

### 2022
- Semantic Modeler (browser) introduced as preview
- AI Assistant introduced as preview
- New Catalog UI

---

## Deferring Updates

If you need to delay an update to test in DEV first:

1. **OCI Console** → Analytics Cloud → instance → **Update Settings**
2. Set update delay to "1 month"
3. Apply

> 💡 Tip: Deferring updates is useful for production environments. Keep DEV on the latest, defer TEST and PROD by one month each — gives you time to test before production.

---

## How to Track Changes

### Per-Release Checklist
- Read the What's New page before each release
- Review Preview Features list
- Check OCI Console → instance → "Update available" notification
- Subscribe to Oracle Analytics blog feed
- Join Oracle Analytics Community forums

### Internal Change Log
Best practice: maintain your own change log per environment:
```
2026-04 — Update applied to DEV — Tested AI Assistant new endpoint, no issues
2026-04 — Update applied to PROD — Verified all dashboards working
2026-03 — Deferred update on PROD due to weekend release
```

---

## API Versioning

OAC REST APIs are versioned by date:
- `/api/20210901/` (current major version)
- Older versions available for compatibility
- Oracle deprecates old versions with 12+ month notice

---

## Backward Compatibility

OAC maintains:
- **Catalog backward compatibility**: Older analyses/dashboards continue to work after updates
- **RPD compatibility**: RPDs uploaded years ago continue to work
- **Logical SQL**: stable across releases
- **REST API**: versioned, no breaking changes within a version

---

## Related
- [[OAC Overview & Architecture]]
- [[Subscribe & Provisioning]]
- [[Administration & Service Console]]
- [[FAQs & Troubleshooting]]
