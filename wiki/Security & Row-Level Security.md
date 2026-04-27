# Security & Row-Level Security

> **Last updated:** 2026-04-27
> **Tags:** security, roles, permissions, row-level security, RLS, IDCS, SSO, data-level, object-level, VPD

## Summary
OAC security is multi-layered: identity management (who can log in), application roles (what they can do), object permissions (what content they can see), and data-level security (which rows they see in query results). Identity is managed via Oracle Identity Cloud Service (IDCS) / OCI IAM. Data security is enforced in the Semantic Model via session variables and row-level filters.

---

## Identity & Authentication

### Oracle Identity Cloud Service (IDCS) / OCI IAM
OAC delegates all identity management to IDCS (or the newer OCI IAM with Identity Domains):
- User provisioning, deprovisioning
- Password policies
- MFA (multi-factor authentication)
- SSO (SAML 2.0, OAuth 2.0)
- Group membership

### SSO Configuration
OAC supports SAML 2.0 federation with corporate identity providers (Okta, Azure AD, Ping, ADFS):
1. Register OAC as a Service Provider in IDCS
2. Configure corporate IdP as Identity Provider in IDCS
3. Map IdP attributes (email, groups) to IDCS user attributes

---

## OAC Application Roles

Application roles determine feature access within OAC. Assigned to users or groups in IDCS/OCI IAM.

### Predefined Roles

| Role | Access Level |
|---|---|
| **BI Service Administrator** | Full admin: service console, security, all content |
| **BI Author** | Create and edit analyses, dashboards, workbooks, datasets |
| **BI Consumer** | View and interact with shared content only |
| **DV Author** | Create workbooks, datasets, data flows |
| **DV Consumer** | View workbooks only |

> 💡 **Tip:** BI Service Administrator does NOT grant all data access — Row-Level Security still applies.

### Custom Application Roles
Administrators can create custom roles in IDCS and grant them specific OAC permissions in the Security Console.

---

## Object-Level Permissions (Catalog)

Each object in the catalog (folder, analysis, dashboard, workbook, data model) has access control:

| Permission | What It Allows |
|---|---|
| **Full Control** | Read, write, delete, change permissions |
| **Modify** | Read and write (not delete/permissions) |
| **Read** | View only |
| **No Access** | Object is invisible to the user |

### Setting Permissions
Catalog → right-click object/folder → **Permissions**:
- Add users or application roles
- Set permission level
- Optionally inherit from parent folder

### Folder Strategy
```
/Shared Folders/
  Finance/          → Finance_Readers: Read, Finance_Authors: Modify
  HR/               → HR_Readers: Read, HR_Authors: Modify
  Executive/        → Exec_Group: Read
  Admin Only/       → ServiceAdmin: Full Control
```

---

## Data-Level Security (Row-Level Security)

Ensures users only see rows they are authorized to see, regardless of how they query the data.

### Method 1: Subject Area Data Filters (Semantic Model)

Define data filters on Subject Area columns tied to session variables.

**Steps**:
1. In Semantic Model → Subject Area → Permissions → Data Filters
2. Add filter: `"Dim - Customer"."Region" = VALUEOF(NQ_SESSION.USER_REGION)`
3. At login, an Initialization Block populates `USER_REGION` from a lookup table

**Session Variable Initialization Block (example)**:
```sql
SELECT REGION
FROM USER_REGION_MAP
WHERE USERNAME = ':USER'
```
This runs at login and sets `NQ_SESSION.USER_REGION` for the session.

### Method 2: Virtual Private Database (VPD / Oracle Label Security)

For Oracle DB sources:
- DB-level VPD policy automatically filters rows based on the DB user
- OAC connection pool configured with **per-user login** or passes `USER` variable
- Transparent to OAC — filtering happens at the database level

### Method 3: Connection Pool with User Credentials

- Each OAC user maps to a distinct DB schema
- DB schema has row-level access via views or VPD
- OAC passes user credentials to the DB connection pool
- Setup: Physical Layer connection → select "Individual login"

### Method 4: Table-Level Filters in BMM Layer

Logical Table Source in the BMM layer can have a **WHERE clause** tied to session variables:
```sql
WHERE REGION_CODE = VALUEOF(NQ_SESSION.REGION)
```
Applied automatically to all queries using that LTS.

---

## Data-Level Security for Workbooks / Datasets

For self-service datasets (not Semantic Model):
- **No automatic RLS** — datasets are user-managed
- Control via: limiting who can see the dataset (catalog permissions)
- For governed data access, route through Subject Areas

---

## Security Console

**Service Console** → **Security Console**:
- View all application roles
- Assign users/groups to roles
- View which users have which permissions
- Audit user access

---

## Audit & Logging

OAC records usage events:
- **Usage Tracking**: SQL queries executed, user, time, subject area, performance
  - Enable in Service Console → Usage Tracking
  - Write to a target DB table for analysis
- **Audit Log**: login/logout events, admin actions
  - Available in OCI Audit service
- **Query Log**: detailed BI Server query log
  - nqquery.log (accessible via Service Console → Diagnostics)

---

## Best Practices

> 💡 Tip: Use Application Roles (not individual users) for catalog permissions — easier to manage as users join/leave.

> ⚠️ Warning: Never grant BI Service Administrator to regular business users. This role can access all data and modify service configuration.

> 💡 Tip: Implement RLS at the Semantic Model (Subject Area Data Filters) rather than at the application layer — it applies consistently to all query types.

> ⚠️ Warning: Session variable initialization blocks run on every user login. Keep the SQL simple and indexed; slow blocks delay OAC login for all users.

> 💡 Tip: Test RLS by impersonating a specific user: Service Console → Security → Test User

---

## Related
- [[Semantic Model]]
- [[OAC Overview & Architecture]]
- [[Administration & Service Console]]
- [[Data Sources & Connections]]
- [[Classic Dashboards & Analyses]]
