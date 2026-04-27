# Maps & Geospatial Analytics

> **Last updated:** 2026-04-27
> **Tags:** maps, geospatial, GeoJSON, Oracle Maps, Esri, geocoding, location, map layers

## Summary
OAC provides rich map visualizations with multiple background tile providers (Oracle Maps, Esri), automatic geocoding of address columns, support for custom GeoJSON layers, and several map visualization types (point, choropleth, heatmap, flow). Maps work in both Workbooks and Classic Analyses.

---

## Map Visualization Types

| Type | Use Case | Data Required |
|---|---|---|
| **Map (Point)** | Locations of stores, customers, events | Latitude/longitude or geocoded address |
| **Choropleth (Region)** | Color regions by metric (sales by state) | Region attribute (matches map layer) |
| **Heatmap** | Density of points | Lat/lon points |
| **Cluster Map** | Group nearby points | Lat/lon points |
| **Flow Map** | Origin-destination flows | Origin and destination lat/lon |
| **Bubble Map** | Point size by metric | Lat/lon + measure |

---

## Setting Up Maps

### Step 1: Configure Map Service (Admin)

**Console** → **Maps** → **Map Backgrounds**:
- **Oracle Maps Cloud Service** (default, free with OAC)
- **Esri ArcGIS** (requires Esri subscription)
- **Custom WMS/WMTS tile servers**

### Step 2: Geocode Address Columns

If your dataset has addresses (no lat/lon), enrich the dataset:
1. Open Dataset → select address column
2. **Recommendations** panel → "Enrich with Geography"
3. OAC adds Latitude, Longitude, City, State, Country columns

### Step 3: Create Map Visualization

1. Workbook → Add visualization
2. Drag latitude column to **Map Layer Latitude**
3. Drag longitude column to **Map Layer Longitude**
4. Drag a measure to **Color** or **Size**

---

## Map Layers

### Built-In Layers (Oracle Maps)
- World countries
- US states
- US counties
- US ZIP codes
- World cities (major)

### Adding Custom Map Layers (GeoJSON)

For custom geographies (sales territories, store regions, voting districts):

1. Prepare GeoJSON file with:
   - Polygon geometries
   - Property field that matches your data column (e.g., `region_id`)

2. **Console** → **Maps** → **Map Layers** → **Upload Map Layer**
3. Select GeoJSON file
4. Map the property field to a key column

### Example GeoJSON Structure
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": { "region_id": "EMEA-NORTH" },
      "geometry": {
        "type": "Polygon",
        "coordinates": [[[-10, 50], [10, 50], [10, 70], [-10, 70], [-10, 50]]]
      }
    }
  ]
}
```

---

## Map Properties (Grammar Panel)

| Property | Function |
|---|---|
| **Map Background** | Choose tile provider (street, satellite, terrain) |
| **Color** | Measure that drives color (gradient or threshold) |
| **Size** | Measure that drives point size |
| **Layer Type** | Points, Clusters, Heatmap, Choropleth |
| **Tooltip** | Columns to show on hover |
| **Min/Max Zoom** | Control zoom range |
| **Auto Zoom** | Fit map to data bounds |

---

## Choropleth (Filled Region) Maps

Color regions based on a measure:

1. Drag a region attribute (e.g., "Country") to **Category**
2. Drag a measure (e.g., "Revenue") to **Color**
3. OAC auto-matches to a built-in or custom region layer
4. Configure color scale: gradient, divergent, or classed

> 💡 **Tip:** For US state choropleths, ensure your data uses 2-letter state codes (CA, NY, TX). For full names, OAC can match but with lower accuracy.

---

## Multi-Layer Maps

A single map visualization can have multiple layers:
- Layer 1: Choropleth (regions colored by sales)
- Layer 2: Points (store locations)
- Layer 3: Heatmap (customer density)

**Configure**: Map Properties → **Add Layer**

Each layer:
- Independent data binding
- Independent style
- Toggleable on/off in legend

---

## Map Filters & Interactions

### Spatial Filtering
- Click a region → filters dashboard to that region
- Drag a box → filters to that bounding area (via Selection tool)

### Drill-Down
- Configure hierarchical drill: Country → State → City
- Click country → zooms to states within country

### Cross-Visualization Filtering
Map can filter other visualizations on the canvas (and vice versa).

---

## Calculations for Maps

### Distance Calculations
```
-- Haversine distance (in calculated column)
6371 * ACOS(
  COS(RADIANS("Lat1")) * COS(RADIANS("Lat2")) *
  COS(RADIANS("Lon2") - RADIANS("Lon1")) +
  SIN(RADIANS("Lat1")) * SIN(RADIANS("Lat2"))
) AS "Distance (km)"
```

### Geofence
Create a calculated column that flags points inside a region:
```
CASE WHEN "Latitude" BETWEEN 40 AND 45 
     AND "Longitude" BETWEEN -75 AND -70
     THEN 'In Region' ELSE 'Out' END
```

---

## Performance Tips

> 💡 **Tip:** For >10,000 points, use **Cluster** or **Heatmap** layer type instead of individual points — much faster.

> 💡 **Tip:** Limit map zoom range — narrower zoom range loads fewer tiles.

> ⚠️ **Warning:** Large GeoJSON layers (>10MB) can slow rendering. Simplify polygons before uploading using tools like Mapshaper.

---

## Common Use Cases

### Retail / Store Performance
- Choropleth: revenue by state
- Points: store locations sized by revenue
- Heatmap: customer density

### Logistics / Supply Chain
- Flow map: shipments from warehouses to customers
- Choropleth: delivery time by region

### Field Service / IoT
- Points: sensor/device locations
- Color by status (red = alert, green = OK)
- Real-time dashboard via auto-refresh

### Demographics / Marketing
- Choropleth: demographic data by ZIP code
- Overlay: store locations as points

---

## Map Export

- Right-click map → **Export** → PDF/PNG
- Map is rendered server-side at export time (preserves zoom/pan state)

---

## Related
- [[Workbooks & Visualizations]]
- [[Subject Areas & Datasets]]
- [[Administration & Service Console]]
- [[Data Flows & Data Preparation]]
