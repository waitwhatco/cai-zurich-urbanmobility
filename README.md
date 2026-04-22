# Zürich Urban Mobility System Blueprint

Production-ready Kumu JSON blueprint of the Zürich urban mobility system for network analysis, resilience mapping, and blended finance strategy work.

## What This Repository Contains

- `data/zurich_mobility_system.json` — the full network blueprint (`elements` + `connections`) for Kumu remote JSON ingestion.
- `data/BLUEPRINT_README.md` — schema definitions, assumptions, quality checks, and Kumu decoration guidance.
- `data/GITHUB_SETUP.md` — practical setup flow for publishing and consuming the JSON as a remote source.
- `LICENSE` — MIT license.

## Dataset Snapshot

- Elements (nodes): **54**
- Connections (flows): **100**
- Geographic scope: Zürich city districts 1-12 plus key regional corridors and gateway hubs.
- Modes represented: **S-Bahn, Tram, Bus, Multi-modal integration** with node-level bike-share and car-share attributes.

## Why This Blueprint

This model is designed for:

- multimodal integration analysis (transfer dependencies and first/last-mile quality)
- bottleneck and resilience screening (critical corridors and stress indicators)
- communication with mixed audiences (technical planners and non-technical stakeholders)

## Quick Start

1. Open `data/zurich_mobility_system.json`.
2. Validate locally with:
   - `python3 -m json.tool data/zurich_mobility_system.json > /dev/null`
3. In Kumu, add a **JSON data source** and point to your hosted raw file URL.
4. Style by:
   - node size: `daily_users_estimate`
   - edge thickness: `frequency_per_hour`
   - edge color: `mode`
   - stress view: `capacity_utilization` and `is_bottleneck`

## Data Quality Principles

- Unique labels and stable IDs for all elements.
- Numeric fields remain numeric for direct decoration/filter support.
- Connection endpoints reference existing elements only.
- Realistic operational estimates calibrated to Zürich network patterns where authoritative live feed integration is not used.

## Regenerating the JSON

The dataset is generated from a reproducible script:

- `scripts/generate_blueprint.py`

Run:

- `python3 scripts/generate_blueprint.py`