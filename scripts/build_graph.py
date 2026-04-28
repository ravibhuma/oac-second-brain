#!/usr/bin/env python3
"""
Build an interactive knowledge graph from wiki/*.md files.

Outputs:
  docs/graph.html       — standalone interactive graph page (vis.js)
  docs/graph-data.json  — nodes + edges as JSON

Run from the repo root:
  python scripts/build_graph.py
"""
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path

# Match markdown links to .md files: [Display](path/to/file.md) or [Display](file.md)
LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+\.md)(?:#[^)]*)?\)')

# Categorize nodes by topic for color grouping
CATEGORIES = {
    "Architecture": [
        "OAC Overview & Architecture",
        "OAC vs OBIEE vs OAS Comparison",
        "Subscribe & Provisioning",
        "Whats New & Release Updates",
    ],
    "Data Layer": [
        "Data Sources & Connections",
        "Semantic Model",
        "Subject Areas & Datasets",
    ],
    "Analytics": [
        "Workbooks & Visualizations",
        "Maps & Geospatial Analytics",
        "Classic Dashboards & Analyses",
        "BI Publisher",
    ],
    "Data Engineering": [
        "Data Flows & Data Preparation",
        "Machine Learning & AI Features",
    ],
    "AI Ecosystem": [
        "OAC AI Ecosystem",
        "OAC AI Agents",
        "OAC MCP Server",
    ],
    "Security & Admin": [
        "Security & Row-Level Security",
        "Administration & Service Console",
    ],
    "Developer": [
        "Logical SQL Reference",
        "APIs, Embedding & Integration",
        "OCI REST APIs & CLI for OAC",
        "Custom Visualizations & Plug-ins",
    ],
    "End User": [
        "Consumer Guide (Explore)",
        "Mobile (Oracle Analytics App)",
    ],
    "Operations": [
        "KPIs, Alerts & Notifications",
        "Migration, Snapshots & Lifecycle",
        "FAQs & Troubleshooting",
    ],
    "Reference": [
        "Docs Coverage Matrix",
        "Tutorials, Solutions & Learning Resources",
        "Source PDFs Index",
    ],
}

# OAC green palette per category
CATEGORY_COLORS = {
    "Architecture":     "#1F5A3D",
    "Data Layer":       "#2D7D55",
    "Analytics":        "#00A36C",
    "Data Engineering": "#4FB58A",
    "AI Ecosystem":     "#C74634",  # Oracle red — stands out for AI
    "Security & Admin": "#5A6772",
    "Developer":        "#3E8E68",
    "End User":         "#7BB89B",
    "Operations":       "#52A07C",
    "Reference":        "#8C99A4",
    "Other":            "#B6BEC6",
}

def get_category(name: str) -> str:
    for cat, names in CATEGORIES.items():
        if name in names:
            return cat
    return "Other"

def slugify_for_url(name: str) -> str:
    """MkDocs preserves filename case; URLs are file-name based."""
    return urllib.parse.quote(name)


# Wiki URLs need to be relative to /graph/ now (one level up)

def extract_links(text: str) -> set[str]:
    """Extract all .md link targets, normalize to bare filenames."""
    targets = set()
    for match in LINK_RE.finditer(text):
        target = match.group(2).strip()
        # Decode URL-encoded paths
        target = urllib.parse.unquote(target)
        # Strip any directory prefix like ./ or ../
        target = os.path.basename(target)
        # Strip .md extension to get the page name
        if target.endswith(".md"):
            target = target[:-3]
        targets.add(target)
    return targets

def build_graph(wiki_dir: Path) -> dict:
    nodes = []
    edges = []
    name_to_id = {}

    md_files = sorted(wiki_dir.glob("*.md"))

    # Pass 1: build nodes
    for i, md_file in enumerate(md_files):
        name = md_file.stem  # e.g., "Semantic Model"
        category = get_category(name)
        nodes.append({
            "id": i,
            "name": name,
            "label": name,
            "group": category,
            "color": CATEGORY_COLORS[category],
            "url": f"../wiki/{slugify_for_url(name)}/",
        })
        name_to_id[name] = i

    # Pass 2: build edges from internal links
    edge_set = set()  # avoid duplicate edges
    for i, md_file in enumerate(md_files):
        text = md_file.read_text(encoding="utf-8")
        targets = extract_links(text)
        source_name = md_file.stem
        for target_name in targets:
            if target_name in name_to_id and target_name != source_name:
                src = name_to_id[source_name]
                dst = name_to_id[target_name]
                edge_key = tuple(sorted([src, dst]))
                if edge_key in edge_set:
                    continue
                edge_set.add(edge_key)
                edges.append({"from": src, "to": dst})

    # Calculate node sizes based on connection count
    connection_count = {n["id"]: 0 for n in nodes}
    for edge in edges:
        connection_count[edge["from"]] += 1
        connection_count[edge["to"]] += 1

    max_count = max(connection_count.values()) if connection_count else 1
    for node in nodes:
        count = connection_count[node["id"]]
        # Size from 16 to 50 based on connections
        node["value"] = count
        node["size"] = 16 + (count / max_count) * 34
        node["connections"] = count

    return {
        "nodes": nodes,
        "edges": edges,
        "categories": [
            {"name": cat, "color": CATEGORY_COLORS[cat]}
            for cat in CATEGORIES.keys()
        ],
        "stats": {
            "total_nodes": len(nodes),
            "total_edges": len(edges),
        },
    }


HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Knowledge Graph — OAC Second Brain</title>
<meta name="description" content="Interactive knowledge graph showing how 30+ Oracle Analytics Cloud topics connect — built without RAG or vector databases.">
<link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
<style>
  :root {
    --oac-green: #2D7D55;
    --oac-green-bright: #00A36C;
    --oac-green-dark: #1F5A3D;
    --oac-green-soft: #E8F4ED;
    --oracle-red: #C74634;
    --slate-900: #161B1F;
    --slate-700: #2A323A;
    --slate-500: #5A6772;
    --slate-300: #B6BEC6;
    --slate-100: #EFF2F4;
    --slate-50: #F7F9FA;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body {
    height: 100%;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
    background: #ffffff;
    color: var(--slate-900);
    overflow: hidden;
  }
  body { display: flex; flex-direction: column; }

  header {
    padding: 16px 24px;
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: saturate(180%) blur(20px);
    -webkit-backdrop-filter: saturate(180%) blur(20px);
    border-bottom: 1px solid var(--slate-100);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    flex-wrap: wrap;
    z-index: 10;
  }
  .brand {
    display: flex; align-items: center; gap: 12px;
    font-weight: 700;
    font-size: 1.1rem;
    letter-spacing: -0.02em;
    color: var(--slate-900);
    text-decoration: none;
  }
  .brand .dot {
    width: 12px; height: 12px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--oac-green-dark), var(--oac-green-bright));
  }
  .brand .red { color: var(--oracle-red); }
  nav.controls { display: flex; align-items: center; gap: 12px; }
  .search {
    padding: 8px 12px;
    border: 1px solid var(--slate-100);
    border-radius: 6px;
    font-size: 0.85rem;
    width: 220px;
    background: var(--slate-50);
    transition: border-color 0.15s, box-shadow 0.15s;
    font-family: inherit;
  }
  .search:focus {
    outline: none;
    border-color: var(--oac-green);
    background: white;
    box-shadow: 0 0 0 3px rgba(45, 125, 85, 0.1);
  }
  .btn {
    padding: 8px 16px;
    border: 1px solid var(--slate-100);
    background: white;
    color: var(--slate-700);
    border-radius: 6px;
    font-size: 0.85rem;
    cursor: pointer;
    font-weight: 500;
    transition: all 0.15s;
    text-decoration: none;
    font-family: inherit;
  }
  .btn:hover {
    border-color: var(--oac-green);
    color: var(--oac-green);
  }
  .btn-primary {
    background: var(--oac-green);
    color: white;
    border-color: var(--oac-green);
  }
  .btn-primary:hover {
    background: var(--oac-green-bright);
    border-color: var(--oac-green-bright);
    color: white;
  }

  #graph-container {
    flex: 1;
    position: relative;
    background: #fcfdfd;
    background-image:
      radial-gradient(circle at 1px 1px, var(--slate-100) 1px, transparent 0);
    background-size: 24px 24px;
  }
  #graph { width: 100%; height: 100%; }

  .legend {
    position: absolute;
    bottom: 16px;
    left: 16px;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    border: 1px solid var(--slate-100);
    border-radius: 10px;
    padding: 12px 14px;
    font-size: 0.8rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    max-width: 240px;
  }
  .legend-title {
    font-weight: 700;
    margin-bottom: 8px;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--slate-500);
  }
  .legend-item {
    display: flex; align-items: center; gap: 8px;
    margin-bottom: 4px;
  }
  .legend-swatch {
    width: 10px; height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .info-panel {
    position: absolute;
    top: 16px;
    right: 16px;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    border: 1px solid var(--slate-100);
    border-radius: 10px;
    padding: 16px;
    width: 300px;
    max-height: calc(100vh - 200px);
    overflow-y: auto;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    display: none;
  }
  .info-panel.active { display: block; }
  .info-panel h2 {
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 6px;
    letter-spacing: -0.01em;
  }
  .info-panel .category {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 12px;
    font-size: 0.7rem;
    font-weight: 600;
    color: white;
    margin-bottom: 12px;
  }
  .info-panel .stat {
    color: var(--slate-500);
    font-size: 0.8rem;
    margin-bottom: 12px;
  }
  .info-panel ul { list-style: none; margin: 0; padding: 0; }
  .info-panel li {
    font-size: 0.85rem;
    padding: 6px 0;
    border-bottom: 1px solid var(--slate-50);
  }
  .info-panel a {
    color: var(--oac-green-dark);
    text-decoration: none;
  }
  .info-panel a:hover { color: var(--oac-green-bright); }

  .stats-bar {
    position: absolute;
    bottom: 16px;
    right: 16px;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    border: 1px solid var(--slate-100);
    border-radius: 10px;
    padding: 10px 14px;
    font-size: 0.75rem;
    color: var(--slate-500);
    display: flex;
    gap: 16px;
  }
  .stats-bar strong { color: var(--slate-900); font-weight: 700; }

  .loading {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: white;
    color: var(--slate-500);
    font-size: 0.9rem;
    z-index: 5;
  }

  @media (max-width: 768px) {
    header { padding: 12px 16px; }
    .search { width: 140px; }
    .info-panel { width: calc(100vw - 32px); right: 16px; max-height: 50vh; }
    .legend { font-size: 0.7rem; padding: 8px 10px; max-width: 180px; }
    .stats-bar { font-size: 0.7rem; bottom: 70px; }
  }
</style>
</head>
<body>

<header>
  <a href="../" class="brand">
    <span class="dot"></span>
    <span><span class="red">OAC</span> Second Brain</span>
    <span style="color: var(--slate-500); font-weight: 500; font-size: 0.85rem; margin-left: 8px;">Knowledge Graph</span>
  </a>
  <nav class="controls">
    <input type="text" class="search" id="search" placeholder="Search topics..." />
    <a href="../" class="btn">← Back to docs</a>
  </nav>
</header>

<div id="graph-container">
  <div class="loading" id="loading">Loading knowledge graph...</div>
  <div id="graph"></div>

  <div class="legend" id="legend">
    <div class="legend-title">Categories</div>
    <div id="legend-items"></div>
  </div>

  <div class="info-panel" id="info-panel">
    <h2 id="info-title">—</h2>
    <span class="category" id="info-category">—</span>
    <div class="stat" id="info-stat">—</div>
    <a id="info-link" class="btn btn-primary" href="#" style="display: inline-block; padding: 8px 16px; margin-bottom: 14px;">Open page →</a>
    <div class="legend-title" style="margin-top: 8px;">Connected to</div>
    <ul id="info-connections"></ul>
  </div>

  <div class="stats-bar">
    <span><strong id="stat-nodes">0</strong> topics</span>
    <span><strong id="stat-edges">0</strong> connections</span>
  </div>
</div>

<script>
const GRAPH_DATA = __GRAPH_DATA__;

// Build vis.js network
const nodes = new vis.DataSet(GRAPH_DATA.nodes.map(n => ({
  id: n.id,
  label: n.label,
  group: n.group,
  color: { background: n.color, border: n.color, highlight: { background: n.color, border: '#000' } },
  size: n.size,
  font: {
    color: '#161B1F',
    size: 13,
    face: 'Inter, system-ui, sans-serif',
    strokeWidth: 3,
    strokeColor: 'rgba(255,255,255,0.95)'
  },
  shape: 'dot',
  // Custom properties stored
  _name: n.name,
  _url: n.url,
  _connections: n.connections,
  _category: n.group,
  _color: n.color,
})));

const edges = new vis.DataSet(GRAPH_DATA.edges.map((e, i) => ({
  id: i,
  from: e.from,
  to: e.to,
  color: { color: 'rgba(90, 103, 114, 0.25)', highlight: '#2D7D55' },
  width: 1,
  smooth: { type: 'continuous', roundness: 0.5 },
})));

const container = document.getElementById('graph');
const data = { nodes, edges };
const options = {
  physics: {
    forceAtlas2Based: {
      gravitationalConstant: -50,
      centralGravity: 0.012,
      springLength: 130,
      springConstant: 0.08,
      damping: 0.6,
    },
    solver: 'forceAtlas2Based',
    stabilization: { iterations: 200, updateInterval: 25 },
  },
  interaction: {
    hover: true,
    tooltipDelay: 200,
    navigationButtons: false,
    keyboard: true,
  },
  nodes: {
    borderWidth: 2,
    shadow: { enabled: true, color: 'rgba(0,0,0,0.1)', size: 8, x: 0, y: 2 },
  },
  edges: {
    selectionWidth: 2,
  },
};

const network = new vis.Network(container, data, options);

network.once('stabilizationIterationsDone', () => {
  document.getElementById('loading').style.display = 'none';
});

// Stats
document.getElementById('stat-nodes').textContent = GRAPH_DATA.stats.total_nodes;
document.getElementById('stat-edges').textContent = GRAPH_DATA.stats.total_edges;

// Build legend
const legendItems = document.getElementById('legend-items');
GRAPH_DATA.categories.forEach(cat => {
  const item = document.createElement('div');
  item.className = 'legend-item';
  item.innerHTML = `<span class="legend-swatch" style="background: ${cat.color}"></span><span>${cat.name}</span>`;
  legendItems.appendChild(item);
});

// Hover highlights
network.on('hoverNode', params => {
  const nodeId = params.node;
  const connectedNodes = network.getConnectedNodes(nodeId);
  const connectedEdges = network.getConnectedEdges(nodeId);

  nodes.forEach(n => {
    if (n.id === nodeId || connectedNodes.includes(n.id)) {
      nodes.update({ id: n.id, opacity: 1, font: { ...n.font, color: '#161B1F' } });
    } else {
      nodes.update({ id: n.id, opacity: 0.15 });
    }
  });
});
network.on('blurNode', () => {
  nodes.forEach(n => nodes.update({ id: n.id, opacity: 1 }));
});

// Click → show info panel
network.on('click', params => {
  if (params.nodes.length === 0) {
    document.getElementById('info-panel').classList.remove('active');
    return;
  }
  const nodeId = params.nodes[0];
  const node = nodes.get(nodeId);
  showInfo(node);
});

// Double-click → navigate
network.on('doubleClick', params => {
  if (params.nodes.length === 0) return;
  const nodeId = params.nodes[0];
  const node = nodes.get(nodeId);
  if (node._url) window.location.href = node._url;
});

function showInfo(node) {
  const panel = document.getElementById('info-panel');
  document.getElementById('info-title').textContent = node._name;
  const catBadge = document.getElementById('info-category');
  catBadge.textContent = node._category;
  catBadge.style.background = node._color;
  document.getElementById('info-stat').textContent = `${node._connections} connection${node._connections !== 1 ? 's' : ''}`;
  document.getElementById('info-link').href = node._url;

  // List connections
  const connectedIds = network.getConnectedNodes(node.id);
  const connList = document.getElementById('info-connections');
  connList.innerHTML = '';
  connectedIds.forEach(id => {
    const conn = nodes.get(id);
    const li = document.createElement('li');
    li.innerHTML = `<a href="${conn._url}">${conn._name}</a>`;
    connList.appendChild(li);
  });

  panel.classList.add('active');
}

// Search
const searchInput = document.getElementById('search');
searchInput.addEventListener('input', e => {
  const q = e.target.value.toLowerCase().trim();
  if (!q) {
    nodes.forEach(n => nodes.update({ id: n.id, opacity: 1 }));
    return;
  }
  nodes.forEach(n => {
    const match = n._name.toLowerCase().includes(q);
    nodes.update({ id: n.id, opacity: match ? 1 : 0.1 });
  });
});

// Press Enter on search → focus first match
searchInput.addEventListener('keydown', e => {
  if (e.key !== 'Enter') return;
  const q = e.target.value.toLowerCase().trim();
  if (!q) return;
  const match = GRAPH_DATA.nodes.find(n => n.name.toLowerCase().includes(q));
  if (match) {
    network.focus(match.id, { scale: 1.2, animation: { duration: 600, easingFunction: 'easeInOutQuad' } });
    network.selectNodes([match.id]);
    showInfo(nodes.get(match.id));
  }
});
</script>

</body>
</html>
'''

def main():
    repo_root = Path(__file__).resolve().parent.parent
    wiki_dir = repo_root / "wiki"
    docs_dir = repo_root / "docs"

    if not wiki_dir.is_dir():
        print(f"[ERROR] wiki/ directory not found at {wiki_dir}", file=sys.stderr)
        sys.exit(1)

    # Allow override of output dir via argv
    if len(sys.argv) > 1:
        docs_dir = Path(sys.argv[1])

    docs_dir.mkdir(parents=True, exist_ok=True)

    print(f"[*] Scanning {wiki_dir}...")
    graph = build_graph(wiki_dir)
    print(f"[OK] Found {graph['stats']['total_nodes']} nodes, {graph['stats']['total_edges']} edges")

    # Output to docs/graph/ as a static asset (subfolder = MkDocs leaves it alone)
    graph_dir = docs_dir / "graph"
    graph_dir.mkdir(parents=True, exist_ok=True)

    # Write graph data
    json_path = graph_dir / "graph-data.json"
    json_path.write_text(json.dumps(graph, indent=2), encoding="utf-8")
    print(f"[OK] Wrote {json_path}")

    # Write HTML page as index.html so URL becomes /graph/
    html_path = graph_dir / "index.html"
    html = HTML_TEMPLATE.replace("__GRAPH_DATA__", json.dumps(graph))
    html_path.write_text(html, encoding="utf-8")
    print(f"[OK] Wrote {html_path}")

    print(f"\n[DONE] Open {html_path} in a browser to view the graph.")


if __name__ == "__main__":
    main()
