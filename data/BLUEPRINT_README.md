# Zürich Mobility Blueprint Documentation

## System Overview

This blueprint models the Zürich mobility ecosystem as a network of places (`elements`) and movement or integration relationships (`connections`) for direct ingestion into Kumu.

- Primary focus: integration, resilience, and multimodal accessibility.
- Audience: mobility planners, finance partners, academic collaborators.
- Intended use: filtering hotspots, visualizing corridor dependencies, and evaluating first/last-mile readiness.

## File Format

The JSON intentionally includes only:

- `elements`
- `connections`

No Kumu full project export wrappers are included.

## Element Schema

Each element includes:

- `label`, `id`, `type`, `description`
- `district`, `latitude`, `longitude`
- `role`, `primary_modes`
- `daily_users_estimate`, `interchange_capacity`, `accessibility`
- `has_parking`, `has_bikeshare`, `has_carshare`, `first_mile_last_mile`
- `centrality`, `is_regional_gateway`
- `degree_centrality`, `weighted_degree_centrality`, `betweenness_centrality`, `network_influence_score`
- `tags` (array)

## Connection Schema

Each connection includes:

- `from`, `to`, `id`, `type`
- `mode`, `frequency_per_hour`, `direction`
- `estimated_daily_volume`, `capacity_utilization`
- `proximity_weight`
- `avg_travel_time_minutes`, `reliability_score`, `requires_transfer`
- `route_name`, `operator`
- `is_bottleneck`, `is_key_corridor`, `resilience_importance`
- `tags` (array)

## Data Assumptions

Where direct operational values are not integrated from live feeds, calibrated estimates are used:

- S-Bahn: typically 4-6 trains/hour on primary corridors in peak windows.
- Tram: typically 6-10 services/hour on core corridors.
- Bus: typically 4-8 services/hour on backbone links.
- Integration links (walk, bike-share, transfer): lower equivalent frequencies but high strategic relevance.

Volumes, utilization, and reliability are intentionally normalized for comparative visualization rather than timetable-grade simulation.

## Kumu Decoration Hints

Recommended mappings:

- Element size: `daily_users_estimate`
- Element color: `network_influence_score` (or `centrality` for a simpler categorical view)
- Edge thickness: `frequency_per_hour`
- Edge layout pull/visual proximity: `proximity_weight`
- Edge color: `mode`
- Edge style: dashed when `is_bottleneck = true`
- Stress lens: `capacity_utilization >= 0.8`

Suggested mode colors:

- S-Bahn: `#0066CC`
- Tram: `#CC0000`
- Bus: `#FFCC00`
- Bike-Share: `#00AA55`
- Car-Share: `#9933FF`
- Multi-modal: `#FF9933`

## Example Kumu Advanced Editor Rules

```css
.connection[mode="S-Bahn"] { color: #0066CC; }
.connection[mode="Tram"] { color: #CC0000; }
.connection[mode="Bus"] { color: #FFCC00; }
.connection[mode="Multi-modal"] { color: #FF9933; }
.connection[is_bottleneck="true"] { stroke-dasharray: 6 4; color: #D7263D; }
.connection[capacity_utilization>="0.8"] { width: 4; }
```

## Sample Query Ideas

- Peak-hour stress:
  - `capacity_utilization >= 0.8`
- Regional gateway dependency:
  - `is_regional_gateway = true`
- Accessibility gap scan:
  - `accessibility != "Full"`
- High-resilience corridors:
  - `resilience_importance = "Critical"`

## Quality Checks Applied

- Valid JSON parse
- Unique element labels and stable IDs
- Connection endpoints validated against existing elements
- Numeric fields stored as numeric values
- Full schema population for every element and connection
