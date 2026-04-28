#!/usr/bin/env python3
"""
Add a '📖 Full Oracle Documentation' reference line at the top of each wiki page.

Maps each wiki page to the most relevant Oracle docs guide(s) on docs.oracle.com.
Inserts the reference line right after the front-matter (between blockquote tags
section and the first '## Summary' section).
"""
import re
from pathlib import Path

# Map of wiki page name -> (docs label, docs URL)
# Based on Oracle's official guide structure on docs.oracle.com/en/cloud/paas/analytics-cloud/
DOC_REFERENCES = {
    # Platform
    "OAC Overview & Architecture": [
        ("Getting Started with OAC", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acsgs/"),
        ("OAC Documentation Hub", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/"),
    ],
    "OAC vs OBIEE vs OAS Comparison": [
        ("Migrating to OAC", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acmig/"),
        ("Oracle Analytics Server", "https://docs.oracle.com/en/middleware/bi/analytics-server/"),
    ],
    "Subscribe & Provisioning": [
        ("Administering OAC (Gen 2)", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acoag/"),
        ("Subscribe and Set Up", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acoag/manage-services.html"),
    ],
    "Whats New & Release Updates": [
        ("What's New in OAC", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acwhn/"),
        ("Preview Features", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acwhn/preview-features.html"),
    ],

    # Data Layer
    "Data Sources & Connections": [
        ("Connecting OAC to Your Data", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acdpr/"),
    ],
    "Semantic Model": [
        ("Building Semantic Models in OAC", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acmdg/"),
        ("SMML Schema Reference", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acsmm/"),
    ],
    "Subject Areas & Datasets": [
        ("Visualizing Data and Building Reports", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/"),
        ("Building Semantic Models", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acmdg/"),
    ],

    # Analytics & Reporting
    "Workbooks & Visualizations": [
        ("Visualizing Data and Building Reports", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/"),
    ],
    "Maps & Geospatial Analytics": [
        ("Visualizing Data — Maps", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/"),
    ],
    "Classic Dashboards & Analyses": [
        ("Visualizing Data and Building Reports — Dashboards", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/"),
    ],
    "BI Publisher": [
        ("Designing and Publishing Pixel-Perfect Reports", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acpub/"),
        ("Designing Pixel-Perfect Layouts", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acpld/"),
    ],

    # Data Engineering
    "Data Flows & Data Preparation": [
        ("Connecting OAC to Your Data — Curate Data", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acdpr/"),
        ("Visualizing Data — Data Flows", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/"),
    ],
    "Machine Learning & AI Features": [
        ("Visualizing Data — Machine Learning", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/"),
        ("OCI AI Services", "https://docs.oracle.com/en-us/iaas/Content/services.htm"),
    ],

    # AI Ecosystem
    "OAC AI Ecosystem": [
        ("Oracle Analytics Blog — AI Ecosystem", "https://blogs.oracle.com/analytics/the-oracle-analytics-cloud-ai-ecosystem-shaping-the-future-of-enterprise-analytics"),
        ("Visualizing Data — AI Assistant", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/"),
    ],
    "OAC AI Agents": [
        ("Visualizing Data — AI Assistants", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/"),
        ("Building Effective OAC AI Agents (Medium)", "https://medium.com/@ravishankerb/building-effective-oac-ai-agents-the-framework-the-techniques-and-the-resource-hub-to-get-you-eba3797ca991"),
    ],
    "OAC MCP Server": [
        ("Oracle Analytics Blog — MCP Server", "https://blogs.oracle.com/analytics/oracle-analytics-cloud-mcp-server-bridging-enterprise-analytics-and-ai"),
        ("Model Context Protocol", "https://modelcontextprotocol.io/"),
    ],

    # Governance & Security
    "Security & Row-Level Security": [
        ("Administering OAC — Security", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acoag/"),
        ("Building Semantic Models — Data Access Security", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acmdg/"),
    ],
    "Administration & Service Console": [
        ("Administering OAC", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acoag/"),
        ("Configuring OAC", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/aciag/"),
    ],

    # Developer Reference
    "Logical SQL Reference": [
        ("Logical SQL Reference Guide", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acmdg/"),
    ],
    "APIs, Embedding & Integration": [
        ("Developing in OAC", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acdev/"),
        ("OAC REST APIs", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acpra/"),
    ],
    "OCI REST APIs & CLI for OAC": [
        ("OCI Analytics Cloud REST API", "https://docs.oracle.com/en-us/iaas/api/#/en/analytics/"),
        ("OCI CLI for Analytics", "https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/analytics.html"),
    ],
    "Custom Visualizations & Plug-ins": [
        ("Developing in OAC — Custom Visualizations", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acdev/"),
        ("Oracle Analytics Library", "https://www.oracle.com/business-analytics/analytics-library/"),
    ],

    # End User
    "Consumer Guide (Explore)": [
        ("Visualizing Data and Building Reports", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/"),
    ],
    "Mobile (Oracle Analytics App)": [
        ("Oracle Analytics Mobile App", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/"),
    ],

    # Operations
    "KPIs, Alerts & Notifications": [
        ("Visualizing Data — KPIs and Agents", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acubi/"),
    ],
    "Migration, Snapshots & Lifecycle": [
        ("Migrating to OAC", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acmig/"),
        ("Administering OAC — Snapshots", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/acoag/"),
    ],
    "FAQs & Troubleshooting": [
        ("FAQs for OAC", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/faqs/"),
        ("Troubleshooting Guide", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/troubleshoot/"),
    ],

    # Reference
    "Docs Coverage Matrix": [
        ("OAC Documentation Hub (all guides)", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/"),
    ],
    "Tutorials, Solutions & Learning Resources": [
        ("OAC Tutorials Hub", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/tutorials"),
        ("Oracle Analytics Blog", "https://blogs.oracle.com/analytics/"),
    ],
    "Source PDFs Index": [
        ("OAC Documentation Hub", "https://docs.oracle.com/en/cloud/paas/analytics-cloud/"),
    ],
}

REFERENCE_MARKER = "📖 **Full Oracle Documentation**:"

def build_reference_line(refs):
    """Build the reference line markdown."""
    parts = [f"[{label}]({url})" for label, url in refs]
    return f"{REFERENCE_MARKER} {' · '.join(parts)}"

def insert_reference(md_file: Path, refs):
    """Insert reference line after the front-matter blockquote in a wiki page."""
    text = md_file.read_text(encoding="utf-8")

    # If already has the marker, replace it
    if REFERENCE_MARKER in text:
        # Replace the existing line
        lines = text.split("\n")
        new_lines = []
        for line in lines:
            if line.startswith(REFERENCE_MARKER):
                new_lines.append(build_reference_line(refs))
            else:
                new_lines.append(line)
        new_text = "\n".join(new_lines)
        md_file.write_text(new_text, encoding="utf-8")
        return "updated"

    # Otherwise insert it after the > Tags blockquote line(s) and before "## Summary"
    # Pattern: find first line starting with "## Summary" or "## "
    lines = text.split("\n")
    insert_at = None
    for i, line in enumerate(lines):
        if line.startswith("## "):
            insert_at = i
            break

    if insert_at is None:
        return "no insertion point"

    reference_line = build_reference_line(refs)
    # Insert with a blank line before and after
    lines.insert(insert_at, "")
    lines.insert(insert_at, reference_line)
    lines.insert(insert_at, "")
    new_text = "\n".join(lines)
    md_file.write_text(new_text, encoding="utf-8")
    return "inserted"

def main():
    wiki_dir = Path("wiki")
    if not wiki_dir.is_dir():
        print(f"[ERROR] wiki/ not found")
        return

    total = 0
    updated = 0
    inserted = 0
    missing = []

    for md_file in sorted(wiki_dir.glob("*.md")):
        page_name = md_file.stem
        refs = DOC_REFERENCES.get(page_name)
        total += 1
        if not refs:
            missing.append(page_name)
            continue
        result = insert_reference(md_file, refs)
        if result == "updated":
            updated += 1
        elif result == "inserted":
            inserted += 1
        print(f"  [{result:8}] {page_name}")

    print(f"\nTotal: {total} pages | Inserted: {inserted} | Updated: {updated}")
    if missing:
        print(f"\nNo doc reference defined for: {missing}")

if __name__ == "__main__":
    main()
