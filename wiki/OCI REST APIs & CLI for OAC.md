# OCI REST APIs & CLI for OAC

> **Last updated:** 2026-04-27
> **Tags:** OCI, REST API, CLI, instance management, automation, terraform, IaC, scaling

## Summary
The **OCI Analytics Cloud REST API** and **OCI CLI** manage OAC at the **infrastructure level** — creating instances, scaling, taking snapshots, configuring PAC, starting/stopping. This is distinct from the [[APIs, Embedding & Integration|OAC application REST API]] which manages content (analyses, dashboards) inside an instance.

---

## Two API Layers — Don't Confuse Them

| Layer | Purpose | Endpoint |
|---|---|---|
| **OCI Management API** | Manage the OAC instance (create, scale, snapshot) | `analytics.<region>.oci.oraclecloud.com` |
| **OAC Application API** | Manage content inside OAC (analyses, queries) | `<instance>.analytics.ocp.oraclecloud.com/api/` |

This page covers the **OCI Management API and CLI**.

---

## OCI CLI — Setup

### Install
```bash
# Linux/Mac
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"

# Windows PowerShell
powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.ps1'))"
```

### Configure
```bash
oci setup config
# Prompts for: User OCID, Tenancy OCID, Region, key file location
```

### Verify
```bash
oci iam region list
```

---

## Common OCI CLI Commands for OAC

### List All Analytics Instances
```bash
oci analytics analytics-instance list \
  --compartment-id <compartment-ocid>
```

### Get Instance Details
```bash
oci analytics analytics-instance get \
  --analytics-instance-id <ocid>
```

### Create Instance
```bash
oci analytics analytics-instance create \
  --compartment-id <compartment-ocid> \
  --name oac-prod \
  --description "Production OAC" \
  --feature-set ENTERPRISE_ANALYTICS \
  --capacity '{"capacityType":"OLPU_COUNT","capacityValue":4}' \
  --license-type LICENSE_INCLUDED \
  --idcs-access-token-file /path/to/token \
  --hostname-prefix oac-prod
```

### Start / Stop Instance
```bash
# Start
oci analytics analytics-instance start \
  --analytics-instance-id <ocid>

# Stop
oci analytics analytics-instance stop \
  --analytics-instance-id <ocid>
```

### Scale OCPU Count
```bash
oci analytics analytics-instance scale \
  --analytics-instance-id <ocid> \
  --capacity '{"capacityType":"OLPU_COUNT","capacityValue":8}'
```

### Create Snapshot
```bash
oci analytics analytics-instance create-snapshot \
  --analytics-instance-id <ocid> \
  --display-name "snapshot-2026-04-27"
```

### List Snapshots
```bash
oci analytics analytics-instance list-snapshots \
  --analytics-instance-id <ocid>
```

### Restore from Snapshot
```bash
oci analytics analytics-instance restore-snapshot \
  --analytics-instance-id <target-ocid> \
  --snapshot-id <snapshot-ocid>
```

### Delete Instance
```bash
oci analytics analytics-instance delete \
  --analytics-instance-id <ocid> \
  --force
```

---

## OCI REST API Endpoints

Base URL pattern:
```
https://analytics.<region>.oci.oraclecloud.com/20190331/
```

### Authentication
OCI APIs use **request signing** with your API private key:
```bash
# Most useful: use OCI SDK or CLI which handles signing automatically
# Manual signing is complex — see Oracle docs for spec
```

### Key Endpoints

| Method | Endpoint | Action |
|---|---|---|
| `GET` | `/analyticsInstances` | List instances |
| `GET` | `/analyticsInstances/{id}` | Get instance details |
| `POST` | `/analyticsInstances` | Create instance |
| `PUT` | `/analyticsInstances/{id}` | Update instance |
| `DELETE` | `/analyticsInstances/{id}` | Delete instance |
| `POST` | `/analyticsInstances/{id}/actions/start` | Start instance |
| `POST` | `/analyticsInstances/{id}/actions/stop` | Stop instance |
| `POST` | `/analyticsInstances/{id}/actions/scale` | Scale OCPUs |
| `GET` | `/analyticsInstances/{id}/snapshots` | List snapshots |
| `POST` | `/analyticsInstances/{id}/snapshots` | Create snapshot |
| `POST` | `/analyticsInstances/{id}/actions/restoreSnapshot` | Restore |
| `GET` | `/analyticsInstances/{id}/privateAccessChannels` | List PAC configs |

### Example: List Instances (curl)
```bash
# Build signed request (or use OCI CLI raw-request)
oci raw-request \
  --target-uri "https://analytics.us-ashburn-1.oci.oraclecloud.com/20190331/analyticsInstances?compartmentId=<ocid>" \
  --http-method GET
```

---

## Terraform / IaC

OCI provides Terraform provider for OAC.

### Example: Provision OAC Instance
```hcl
provider "oci" {
  region = "us-ashburn-1"
}

resource "oci_analytics_analytics_instance" "oac_prod" {
  compartment_id        = var.compartment_ocid
  name                  = "oac-prod"
  feature_set           = "ENTERPRISE_ANALYTICS"
  license_type          = "LICENSE_INCLUDED"
  idcs_access_token     = var.idcs_token
  hostname_prefix       = "oac-prod"

  capacity {
    capacity_type  = "OLPU_COUNT"
    capacity_value = 4
  }

  network_endpoint_details {
    network_endpoint_type = "PUBLIC"
  }
}
```

### Apply
```bash
terraform init
terraform plan
terraform apply
```

> 💡 **Tip:** Use Terraform for reproducible multi-environment setups (DEV/TEST/PROD identical except OCPU count).

---

## Common Automation Use Cases

### 1. Scheduled Stop/Start (Cost Savings)
Use OCI Functions or external cron to stop OAC outside business hours:
```bash
# Cron example (Linux)
# Stop at 8 PM, start at 7 AM weekdays
0 20 * * 1-5  oci analytics analytics-instance stop --analytics-instance-id <ocid>
0 7  * * 1-5  oci analytics analytics-instance start --analytics-instance-id <ocid>
```

### 2. Daily Snapshot
```bash
# Cron at 2 AM daily
0 2 * * *  oci analytics analytics-instance create-snapshot \
  --analytics-instance-id <ocid> \
  --display-name "daily-$(date +%Y-%m-%d)"
```

### 3. Auto-Scale Based on Demand
- Use OCI Monitoring + Alarms + Notifications
- Trigger Function that calls scale API
- Scale up during peak hours, down at night

### 4. Snapshot Retention Cleanup
```bash
# List snapshots older than 30 days, delete them
oci analytics analytics-instance list-snapshots \
  --analytics-instance-id <ocid> \
  --query "data[?\"time-created\" < '$(date -d '-30 days' --iso-8601)']" \
  | jq -r '.[].id' \
  | xargs -I {} oci analytics analytics-instance-snapshot delete --analytics-instance-snapshot-id {}
```

---

## Permissions Required

To call these APIs, your OCI user needs:

```hcl
# IAM Policy
allow group BI_Admins to manage analytics-instance in compartment <name>
allow group BI_Admins to manage analytics-instance-snapshot in compartment <name>
```

---

## Monitoring OCI-Level Operations

### Audit Logs
**OCI Console** → **Audit** → filter by service `analytics`:
- Track who created/scaled/deleted instances
- Compliance evidence

### Work Requests
Long-running operations (create, scale, restore) generate Work Requests:
```bash
oci analytics work-request list --compartment-id <ocid>
oci analytics work-request get --work-request-id <work-request-ocid>
```

---

## Related
- [[Subscribe & Provisioning]]
- [[Administration & Service Console]]
- [[Migration, Snapshots & Lifecycle]]
- [[APIs, Embedding & Integration]]
