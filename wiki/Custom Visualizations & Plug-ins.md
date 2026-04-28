# Custom Visualizations & Plug-ins

> **Last updated:** 2026-04-27
> **Tags:** custom visualization, plug-in, extension, D3, JavaScript, SDK, marketplace


📖 **Full Oracle Documentation**: [Developing in OAC — Custom Visualizations](https://docs.oracle.com/en/cloud/paas/analytics-cloud/acdev/) · [Oracle Analytics Library](https://www.oracle.com/business-analytics/analytics-library/)

## Summary
OAC supports **custom visualizations** built with JavaScript (and D3, Chart.js, Highcharts, or any web library) that integrate seamlessly into Workbooks and Classic Analyses. This enables organizations to build domain-specific charts (Sankey, Gantt, Network Graphs, custom KPI cards) and share them across the platform.

---

## When to Build Custom Visualizations

Use built-in visualizations whenever possible. Custom viz is needed when:

- Specialized chart type not in OAC (Sankey, network diagram, force-directed graph)
- Brand-specific styling requirements (custom KPI tile design)
- Domain-specific charts (medical, scientific, engineering)
- Interactive prototypes for unique workflows

---

## Architecture

A custom visualization is a JavaScript module packaged as a `.dva` file (Data Visualization Archive):

```
my-viz.dva
├── extension.json       # Metadata: name, version, capabilities
├── src/
│   ├── viz.js           # Main rendering logic
│   ├── viz.css          # Styling
│   └── icons/           # Icons for the toolbar
└── dist/                # Compiled JS bundle
```

---

## Plugin SDK

Oracle provides a CLI for developing custom visualizations:

### Install SDK
```bash
npm install -g @oracle/bdvcli
```

### Create New Visualization
```bash
bdvcli new visualization --id my-company.sankey --name "Sankey Diagram"
```

### Develop Locally
```bash
cd my-company-sankey
bdvcli dev
# Opens browser preview at http://localhost:9090
```

### Build & Package
```bash
bdvcli build
# Creates dist/my-company.sankey.dva
```

---

## extension.json (Manifest)

```json
{
  "id": "my-company.sankey",
  "name": "Sankey Diagram",
  "version": "1.0.0",
  "description": "Flow diagram for showing source → target relationships",
  "type": "visualization",
  "capabilities": {
    "supportsTooltip": true,
    "supportsBrushing": true,
    "supportsHighlighting": true
  },
  "dataSlots": [
    { "id": "source", "label": "Source", "type": "attribute", "required": true },
    { "id": "target", "label": "Target", "type": "attribute", "required": true },
    { "id": "value",  "label": "Value",  "type": "measure",   "required": true }
  ],
  "properties": [
    { "id": "nodeWidth", "label": "Node Width", "type": "number", "default": 20 }
  ]
}
```

---

## Rendering Code (viz.js)

```javascript
import * as d3 from 'd3';
import { sankey, sankeyLinkHorizontal } from 'd3-sankey';

export default class SankeyViz {
  constructor(context, container) {
    this.container = container;
    this.context = context;
  }

  render(data) {
    // data is an array of { source, target, value } from OAC
    const width = this.container.clientWidth;
    const height = this.container.clientHeight;

    const svg = d3.select(this.container)
      .append('svg')
      .attr('width', width)
      .attr('height', height);

    const sankeyLayout = sankey()
      .nodeWidth(this.context.properties.nodeWidth)
      .extent([[1, 1], [width - 1, height - 5]]);

    const graph = sankeyLayout(this.transformData(data));

    svg.append('g').selectAll('path')
      .data(graph.links)
      .enter()
      .append('path')
      .attr('d', sankeyLinkHorizontal())
      .style('stroke-width', d => Math.max(1, d.width));

    svg.append('g').selectAll('rect')
      .data(graph.nodes)
      .enter()
      .append('rect')
      .attr('x', d => d.x0)
      .attr('y', d => d.y0)
      .attr('height', d => d.y1 - d.y0)
      .attr('width', d => d.x1 - d.x0);
  }

  transformData(rawData) {
    // Transform OAC data array to { nodes, links } format
    // ...
  }
}
```

---

## Installing a Custom Visualization

### As an End User
1. Download `.dva` file (from internal repo, marketplace, or built locally)
2. **Console** → **Extensions** → **Upload Extension**
3. Browse to `.dva` file
4. Confirm
5. Visualization appears in Workbook → Visualization Picker → "Custom"

### Marketplace
Oracle hosts a public **Oracle Analytics Library** with community-shared visualizations:

- Calendar Heatmap
- Sankey Diagram
- Decomposition Tree
- Network Graph
- Calendar Chart
- Story Map
- ... 50+ others

URL: search "Oracle Analytics Library" or check the in-app **Console** → **Extensions** → **Browse Library**

---

## Capabilities

A custom viz can declare which features it supports:

| Capability | What It Enables |
|---|---|
| `supportsTooltip` | Tooltips on hover (OAC-styled) |
| `supportsBrushing` | Selection / drag-to-filter |
| `supportsHighlighting` | Highlight on cross-viz interaction |
| `supportsSorting` | User can sort data slots |
| `supportsTrellis` | Small-multiples (grid of viz) |

---

## Data Slots

Define how data binds to your visualization:

```json
"dataSlots": [
  {
    "id": "category",
    "label": "Category",
    "type": "attribute",
    "required": true,
    "minColumns": 1,
    "maxColumns": 5
  },
  {
    "id": "value",
    "label": "Value",
    "type": "measure",
    "required": true
  }
]
```

End user drags columns into slots in the Grammar Panel.

---

## Properties (User-Configurable)

Expose options users can tweak:

```json
"properties": [
  { "id": "showLabels",   "label": "Show Labels",   "type": "boolean", "default": true },
  { "id": "labelColor",   "label": "Label Color",   "type": "color",   "default": "#000" },
  { "id": "animationMs",  "label": "Animation (ms)","type": "number",  "default": 800 }
]
```

These appear in the Properties panel when the user selects the visualization.

---

## Lifecycle Methods

```javascript
class MyViz {
  // Called once on creation
  constructor(context, container) { }

  // Called when data or properties change
  render(data) { }

  // Called when container resizes
  resize(width, height) { }

  // Called before destruction (cleanup)
  destroy() { }

  // Called when user clicks an element (for filtering)
  onSelect(selection) {
    this.context.api.applyFilter(selection);
  }
}
```

---

## Custom Plug-In Types Beyond Visualizations

OAC SDK supports several extension types:

| Type | Purpose |
|---|---|
| **Visualization** | Custom chart type |
| **Data Source** | Custom connector to external API |
| **Data Action** | Custom action triggered from a column click |
| **Theme/Skin** | Custom branding/styling |

---

## Best Practices

> 💡 **Tip:** Use existing chart libraries (D3, ECharts, Chart.js) — don't build SVG from scratch.

> 💡 **Tip:** Test responsiveness — visualization must work at 200x200 (mini) up to 1920x1080 (full).

> ⚠️ **Warning:** Custom visualizations execute in the browser. Avoid heavy computation — push aggregation to the data layer.

> ⚠️ **Warning:** Validate data inputs — users may bind unexpected column types. Handle null, empty, and edge cases.

> 💡 **Tip:** Sign your `.dva` files with a code-signing certificate for trust in enterprise deployments.

---

## Distribution

- **Internal**: share `.dva` file across teams; admins upload to OAC instances
- **Marketplace**: submit to Oracle Analytics Library (review process)
- **Open Source**: publish on GitHub with build instructions

---

## Related
- [Workbooks & Visualizations](Workbooks%20%26%20Visualizations.md){ .wikilink }
- [APIs, Embedding & Integration](APIs%2C%20Embedding%20%26%20Integration.md){ .wikilink }
- [Administration & Service Console](Administration%20%26%20Service%20Console.md){ .wikilink }
