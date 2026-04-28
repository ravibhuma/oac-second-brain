# Migration, Snapshots & Lifecycle

> **Last updated:** 2026-04-27
> **Tags:** migration, snapshot, bundle, promotion, OBIEE, OAS, lifecycle, deployment, environments

## Summary
OAC lifecycle management covers: taking snapshots (full backup/restore), promoting content between environments (dev→test→prod), migrating from on-premise OBIEE/OAS to OAC, and managing the Semantic Model RPD through environments. These processes are critical for enterprise deployments with multiple environments and change management requirements.

---

## Snapshots

### What a Snapshot Contains
| Included | Not Included |
|---|---|
| Full catalog (analyses, dashboards, workbooks, reports) | Dataset data (must re-load) |
| Semantic Model (RPD / Semantic Modeler) | User passwords |
| Connections (metadata only, not credentials) | Usage tracking data |
| BI Publisher catalog | Active sessions |
| System configuration | Credentials/wallet files |
| Application roles and permissions | |

### Creating a Snapshot

**OCI Console** → Analytics Cloud → your instance → **Snapshots** → **Create**:
- Name: e.g., `PROD_2026-04-27_pre-release`
- Snapshot completes in 5-30 minutes depending on catalog size

**Via OAC REST API**:
```bash
POST /api/20210901/snapshots
{
  "name": "PROD_2026-04-27",
  "description": "Pre-release backup"
}
```

### Restoring a Snapshot

**OCI Console** → Snapshots → select snapshot → **Restore**:
- Restores to the same instance (all current content is overwritten)
- Or restore to a new OAC instance (used for cloning / migration)

> ⚠️ Warning: Restore is destructive. Always take a fresh snapshot of the target instance before restoring.

### Downloading a Snapshot
- Download to local `.bar` file or OCI Object Storage
- Provides off-instance backup for DR

---

## Content Promotion (Dev → Test → Prod)

### Method 1: Catalog Manager (Classic Tool)
Desktop tool for bulk catalog operations:
- Archive/unarchive catalog sections
- Compare catalogs between environments
- Move selected items with permission preservation

### Method 2: REST API Bundles
Export specific catalog objects and import to another instance:

```bash
# Export specific objects
POST /api/20210901/export
{
  "items": [
    { "objectPath": "/shared/Finance/Revenue Dashboard" },
    { "objectPath": "/shared/Finance/Revenue Analysis" }
  ],
  "targetFolder": "/shared/Finance"
}
# Returns .catalog bundle file

# Import to target instance
POST /api/20210901/import
# Multipart form: bundle file + options
```

### Method 3: Snapshot Promotion
Take a full snapshot from DEV → restore to TEST → restore to PROD:
- Simple but promotes everything (not selective)
- Good for initial environment setup

### Semantic Model Promotion
The RPD must be promoted separately from the catalog:

1. **Download RPD** from DEV: Service Console → Semantic Model → Download
2. Open in Model Administration Tool, make any environment-specific changes (connection pool passwords, server names)
3. **Upload RPD** to TEST/PROD: Service Console → Semantic Model → Upload

For Semantic Modeler (browser-based): export the model file and import to target.

---

## Migrating from OBIEE / OAS to OAC

### Supported Migration Paths
| Source | Target | Method |
|---|---|---|
| OBIEE 11g | OAC | RPD migration + catalog migration |
| OBIEE 12c | OAC | RPD upload + catalog archiving |
| OAS (Oracle Analytics Server) | OAC | Snapshot or catalog migration |

### OBIEE 11g → OAC Steps
1. **Upgrade RPD**: Use OBIEE 12c upgrade tools to upgrade 11g RPD → 12c format
2. **Test RPD on OAS/12c**: Validate queries work
3. **Upload RPD to OAC**: Service Console → Semantic Model
4. **Catalog Migration**:
   - Archive OBIEE 11g catalog to `.catalog` file
   - Import to OAC using Catalog Manager or REST API
5. **Fix compatibility issues**:
   - Prompts, actions, and URLs may need updating
   - Inline HTML/JavaScript in analyses may be blocked by security
   - Custom skins/styles need recreation

### OBIEE 12c / OAS → OAC Steps
1. Take OAS snapshot (full `.bar` file)
2. Create new OAC instance
3. Restore OAS snapshot to OAC (OCI Console → Restore Snapshot)
4. Update connection pool credentials
5. Validate analyses and dashboards

> ⚠️ Warning: OAC uses HTTPS and stricter Content Security Policy (CSP). Custom JavaScript in analyses/dashboards that worked in OBIEE may be blocked. Review and fix.

### Migration Checker Tool
Oracle provides a migration assessment tool:
- Scans OBIEE catalog for compatibility issues
- Reports items needing manual remediation
- Available on Oracle support (My Oracle Support)

---

## Semantic Model Migration Tool (RPD → Semantic Modeler)

Oracle provides a migration tool to convert classic `.rpd` format to the new Semantic Modeler browser format:

**OAC** → **Semantic Model** → **Migrate from RPD**:
1. Upload `.rpd` file
2. Tool converts to Semantic Modeler format
3. Review and fix any unsupported features (e.g., complex initialization blocks)

> ⚠️ Warning: Not all RPD features are supported in Semantic Modeler yet (e.g., complex derived physical tables, some variable types). Check the migration report for unsupported items.

---

## Environment Strategy Best Practices

### Recommended 3-Environment Setup
```
DEV ──→ TEST ──→ PROD
  (develop)  (validate)  (production)
```

| Environment | Purpose | Data |
|---|---|---|
| DEV | Development and testing by analysts/modelers | Sample/anonymized |
| TEST | UAT, performance testing | Production-like |
| PROD | Live production users | Full production |

### Change Management Checklist
- [ ] Take snapshot of target before promoting
- [ ] Promote RPD separately from catalog
- [ ] Update connection pool credentials in target environment
- [ ] Test key dashboards and reports after promotion
- [ ] Verify row-level security works with target users
- [ ] Clear BI Server cache after promotion
- [ ] Monitor query log for errors post-promotion

---

## OAC Version Updates

Oracle releases monthly updates to OAC:
- Applied by Oracle (no customer action for patches)
- Customers can defer one release cycle
- Review **What's New** in Oracle docs before each update
- Test in DEV after update before PROD cutover

---

## Related
- [Administration & Service Console](Administration%20%26%20Service%20Console.md){ .wikilink }
- [Semantic Model](Semantic%20Model.md){ .wikilink }
- [OAC vs OBIEE vs OAS Comparison](OAC%20vs%20OBIEE%20vs%20OAS%20Comparison.md){ .wikilink }
- [Security & Row-Level Security](Security%20%26%20Row-Level%20Security.md){ .wikilink }
