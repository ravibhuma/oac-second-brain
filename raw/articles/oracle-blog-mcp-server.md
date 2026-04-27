# OAC MCP Server: Bridging Enterprise Analytics and AI — Source Article

> **Source**: Oracle Analytics Blog
> **URL**: https://blogs.oracle.com/analytics/oracle-analytics-cloud-mcp-server-bridging-enterprise-analytics-and-ai
> **Ingested**: 2026-04-27
> **Used to build**: [[OAC MCP Server]]

## Key Concepts

### Three Core Tools
1. `oracle_analytics-discoverData` — list datasets/Subject Areas
2. `oracle_analytics-describeData` — get column-level metadata
3. `oracle_analytics-executeLogicalSQL` — run governed Logical SQL

Plus: Logical SQL Grammar Reference resource for AI clients.

### Supported Clients
Claude Desktop, Cline (VS Code), GitHub Copilot, n8n, LangChain — any MCP-compliant client.

### Authentication
- Browser-based (recommended, auto token refresh)
- Token-based via tokens.json (for automation)

### Workflow
**Discover → Describe → Execute** ensures AI has correct schema before generating queries.

### Installation
- Node.js v18+
- Generate access tokens from OAC Profile → Access Tokens
- Download MCP Connect package from Profile → MCP Connect
- Configure Claude Desktop config JSON
- Restart, verify three tools connected

### Security Note
> "Once data leaves OAC and is processed by an external AI client, the data becomes subject to that client's own data-handling, storage, and governance policies."

Recommendations: enterprise LLMs (zero retention), local/OCI-hosted LLMs, masked datasets, compliance alignment.

### Architecture Insight
With Semantic Model: trusted business abstraction layer.
Without: datasets (XSA) serve as governed access.
