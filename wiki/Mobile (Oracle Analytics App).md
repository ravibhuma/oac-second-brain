# Mobile (Oracle Analytics App)

> **Last updated:** 2026-04-27
> **Tags:** mobile, iOS, Android, Oracle Analytics app, Day by Day, push notifications, voice

## Summary
OAC provides a native mobile app — **Oracle Analytics** — for iOS and Android. It enables consumers to access Workbooks, Dashboards, and KPIs on phone or tablet, receive push notifications from Agents, and (in modern versions) use voice and AI Assistant for hands-free analytics.

---

## Apps Overview

| App | Status | Best For |
|---|---|---|
| **Oracle Analytics** | Current | All OAC users (modern app) |
| **Day by Day** | Legacy / Deprecated | Older OBIEE users; being retired |
| **Synopsis** | Deprecated | Was for ad-hoc spreadsheet analytics |

---

## Installation

**iOS**: App Store → search "Oracle Analytics" → install
**Android**: Google Play → search "Oracle Analytics" → install

---

## First-Time Setup

1. Open app
2. **Add Connection** → enter OAC URL: `https://<instance>.analytics.ocp.oraclecloud.com`
3. Sign in with corporate credentials (SSO supported)
4. App caches workbooks and dashboards for offline viewing

---

## Capabilities

### View Content
- Workbooks (full canvas + drill / filter)
- Classic Dashboards
- KPI Watchlists
- BI Publisher reports
- All native interaction (tap to filter, drill, sort)

### AI Assistant on Mobile
- Voice-enabled queries: "Show revenue by region"
- Podcast-style audio insights ("Listen to your data")
- Auto-generated daily briefings

### Push Notifications
- Configure in Console → **Mobile Settings**
- Agents deliver to mobile push (alerts, scheduled deliveries)
- Tap notification → opens the relevant content

### Offline Access
- Cache workbooks for offline use
- Static snapshot — no live filtering of cached data
- Auto-refreshes when network is available

### Search
- Full-text search across catalog
- Recent items pinned to home

---

## Mobile-Specific Features

### Today / Briefing
Automated daily summary:
- Top KPIs
- Significant changes from yesterday
- Anomalies detected
- Auto-generated narration

### Voice Queries
- Hold microphone button → speak question
- Voice-to-text → AI Assistant → visualization
- Read-aloud responses for hands-free use

### Apple Watch / Wear OS (Limited)
- View KPI values
- Receive Agent notifications

---

## Mobile Dashboard Design Tips

When designing for mobile consumers:

> 💡 **Tip:** Use **stacked layouts** rather than wide tables — they fit phone screens.

> 💡 **Tip:** Limit visualizations per canvas to 4-6 — easier to navigate by swipe.

> 💡 **Tip:** Use **large fonts and high contrast** — improves readability outdoors.

> 💡 **Tip:** Test on actual mobile devices — preview mode in browser doesn't catch all issues.

> ⚠️ **Warning:** Some classic dashboard features (complex pivot tables, heavy interactivity) don't translate well to mobile — use Workbooks instead.

---

## Security

- Same SSO and session management as desktop
- App-level PIN/biometric lock (configurable)
- Remote wipe via MDM (mobile device management)
- Cached data encrypted at rest

---

## Mobile Embedding (Advanced)

You can embed OAC content in your custom mobile app:
- Use **JavaScript Embedding API** in a WebView
- Native iOS / Android SDKs not provided directly — wrap web embedding
- Pass authentication via OAuth token

See [[APIs, Embedding & Integration]] for details.

---

## Common Mobile Issues

| Issue | Fix |
|---|---|
| Login loops | Verify SSO config supports mobile redirect URI |
| Cached content stale | Pull-to-refresh; or clear cache in app settings |
| Push notifications not received | Verify app notifications enabled in OS; verify Mobile Settings in Console |
| Workbook renders incorrectly | Use Workbook Mobile Preview in desktop OAC to fix layout issues |

---

## Deprecation Notice — Day by Day

The original OBIEE mobile app **Day by Day** is deprecated:
- No longer receives feature updates
- May still work for OBIEE 12c / OAS connections
- Migrate users to **Oracle Analytics** app
- For OAC users: install Oracle Analytics app directly

---

## Related
- [[Consumer Guide (Explore)]]
- [[Workbooks & Visualizations]]
- [[KPIs, Alerts & Notifications]]
- [[OAC AI Agents]]
- [[Administration & Service Console]]
