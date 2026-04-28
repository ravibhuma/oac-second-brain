# Source PDFs Index — Deep Reference Layer

> **Last updated:** 2026-04-27
> **Tags:** sources, PDFs, deep reference, citations

## Summary
The `raw/pdfs/` folder contains the authoritative Oracle documentation in PDF + searchable text. When wiki pages don't have enough depth, I (Claude) **grep these text files at query time** and cite the result. This is the deep-reference layer that makes the second brain comprehensive.

---

## Available Source Documents

| PDF | Text Size | Content | Maps to Wiki |
|---|---|---|---|
| `getting-started-oracle-analytics-cloud` | 37 KB | Orientation, editions, service mgmt | [OAC Overview & Architecture](OAC%20Overview%20%26%20Architecture.md){ .wikilink }, [Subscribe & Provisioning](Subscribe%20%26%20Provisioning.md){ .wikilink } |
| `whats-new-oracle-analytics-cloud` | 262 KB | Release notes (current + historical) | [Whats New & Release Updates](Whats%20New%20%26%20Release%20Updates.md){ .wikilink } |
| `building-semantic-models-oracle-analytics-cloud` | 1.1 MB | Semantic Modeler full guide | [Semantic Model](Semantic%20Model.md){ .wikilink } |
| `smml-schema-reference-oracle-analytics-cloud` | 162 KB | SMML JSON schema reference | [Semantic Model](Semantic%20Model.md){ .wikilink }, [APIs, Embedding & Integration](APIs%2C%20Embedding%20%26%20Integration.md){ .wikilink } |
| `connecting-oracle-analytics-cloud-your-data` | 589 KB | All data source connections | [Data Sources & Connections](Data%20Sources%20%26%20Connections.md){ .wikilink } |
| `visualizing-data-and-building-reports-oracle-analytics-cloud` | 2.7 MB | Workbooks, dashboards, BI Publisher | [Workbooks & Visualizations](Workbooks%20%26%20Visualizations.md){ .wikilink }, [Classic Dashboards & Analyses](Classic%20Dashboards%20%26%20Analyses.md){ .wikilink }, [BI Publisher](BI%20Publisher.md){ .wikilink }, [Maps & Geospatial Analytics](Maps%20%26%20Geospatial%20Analytics.md){ .wikilink } |
| `administering-oracle-analytics-cloud-oracle-cloud-infrastructure-gen-2` | 570 KB | Service admin (Gen 2) | [Administration & Service Console](Administration%20%26%20Service%20Console.md){ .wikilink }, [Subscribe & Provisioning](Subscribe%20%26%20Provisioning.md){ .wikilink } |
| `configuring-oracle-analytics-cloud` | 1.1 MB | System configuration deep dive | [Administration & Service Console](Administration%20%26%20Service%20Console.md){ .wikilink } |
| `OAC_REST_API_Guide` | 217 KB | OpenAPI spec for OAC REST API | [APIs, Embedding & Integration](APIs%2C%20Embedding%20%26%20Integration.md){ .wikilink }, [OCI REST APIs & CLI for OAC](OCI%20REST%20APIs%20%26%20CLI%20for%20OAC.md){ .wikilink } |

**Total deep reference**: ~6.8 MB of text (~1.5M tokens) — fully searchable.

---

## How to Query Deep Content (For Claude)

When a user asks a question:

```
Step 1: Grep raw/pdfs/*.txt for keywords from the question
Step 2: Read the matching sections (use line offsets)
Step 3: Read the related wiki page for structure
Step 4: Synthesize answer with citations:
   - Wiki Page Name
   - (Source: <pdf-name>, near line N)
```

### Example
**Q:** "How do I set up an event polling table?"

**Process:**
1. `grep -l "event polling" raw/pdfs/*.txt` → finds matches in `building-semantic-models.txt` and `smml-schema-reference.txt`
2. Read those sections (~50 lines context)
3. Read [Semantic Model](Semantic%20Model.md){ .wikilink } for high-level structure
4. Answer with full procedure + cite source PDF + line numbers

---

## Why This Beats Pre-Synthesized Wiki

| Approach | Coverage | Accuracy | Effort | Currency |
|---|---|---|---|---|
| Pre-synthesize 6.8 MB into wiki | 100% but lossy | Risk of summarization errors | Days | Stale on next docs update |
| **Grep raw text at query time** | 100% full fidelity | Direct quotes from Oracle | None — automated | Always current with PDF |

The Karpathy LLM Wiki pattern explicitly endorses this: synthesize **structure** in the wiki, keep **sources** raw and citable.

---

## Refreshing Sources

When Oracle releases new doc versions:

1. Download updated PDFs from `docs.oracle.com/en/cloud/paas/analytics-cloud/`
2. Replace files in `raw/pdfs/`
3. Re-run `pdftotext`:
   ```bash
   cd raw/pdfs
   for f in *.pdf; do pdftotext -layout "$f" "${f%.pdf}.txt"; done
   ```
4. Update `log.md` with refresh date
5. Optionally ask Claude to **re-lint** the wiki against the new PDFs

---

## Related
- index
- [Docs Coverage Matrix](Docs%20Coverage%20Matrix.md){ .wikilink }
- [Tutorials, Solutions & Learning Resources](Tutorials%2C%20Solutions%20%26%20Learning%20Resources.md){ .wikilink }
