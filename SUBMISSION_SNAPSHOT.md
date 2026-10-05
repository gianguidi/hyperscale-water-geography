# Nature Water transfer snapshot — 5 October 2026

This file records the aggregate numerical targets and reproducibility boundary for the manuscript transferred to **Nature Water** on 5 October 2026.

## Manuscript

**One footprint, many maps: the hidden geography of U.S. data-centre water use**

Authors: Gianluca Guidi and Francesca Dominici

## Inventory and primary interpretation

- Provider: Baxtel
- Snapshot date: 15 December 2025
- Provider-defined records: 472
- Reported current capacity: 20,041 MW
- Primary interpretation of `current_mw`: facility-input nameplate power
- Baseline/reference utilization: 0.66

## National scenario results

| Scenario | Facility electricity (TWh/yr) | On-site water (GL/yr) | Electricity-related water (GL/yr) | Total water (GL/yr) | On-site share (%) | Electricity-related share (%) |
|---|---:|---:|---:|---:|---:|---:|
| Lower-load/lower-water | 96.56 | 16.79 | 188.11 | 204.91 | 8.20 | 91.80 |
| Baseline/reference | 115.87 | 74.16 | 225.74 | 299.89 | 24.73 | 75.27 |
| Higher-load/water-intensive | 149.22 | 159.88 | 290.72 | 450.60 | 35.48 | 64.52 |
| No hydropower attribution | 115.87 | 74.16 | 128.35 | 202.50 | 36.62 | 63.38 |

## Regional screening results

- Positive-burden hosting basins: 63
- Hosting basins with valid annual Aqueduct context: 62
- Smallest set reaching at least half of modeled on-site consumption: 10 of 63 basins
- Hosting balancing authorities: 24
- Smallest set reaching at least half of modeled electricity-related consumption: 3 of 24 BAs
- BWS score >= 3: 25 hosting basins
- BWS score >= 3 and at-least-median on-site burden: 15 basins
- BWD score >= 3: 7 hosting basins
- BWD score >= 3 and at-least-median on-site burden: 6 basins

## Hydropower sensitivity

Under baseline activity and on-site assumptions:

- Reference electricity-related water: 225.74 GL/yr
- Zero-hydropower electricity-related water: 128.35 GL/yr
- Difference: 97.39 GL/yr
- Difference as share of reference electricity-related pathway: 43.1%
- Zero-hydropower total: 202.50 GL/yr
- Electricity-related share at zero-hydropower endpoint: 63.38%

A second deterministic comparison uses approximately 6.1 L/kWh for hydropower, yielding approximately:

- Electricity-related water: 202.6 GL/yr
- Total water: 276.8 GL/yr

## Mandatory validation contracts

The corrected workflow is required to stop if any of the following fail:

1. Input identity and checksums/configuration hash
2. Inventory uniqueness
3. Required spatial assignment
4. Annual Aqueduct schema
5. BA resource-mix validity and normalization
6. Canonical facility-scenario uniqueness
7. Non-negativity
8. `W_total = W_onsite + W_electricity`
9. State/BA/basin aggregation conservation
10. Ranked/top-region subset bounds
11. No-hydropower scenario isolation

## Important interpretation limits

These outputs are screening estimates. They do not measure facility-level water use, identify utility intake basins, trace electricity to individual generating plants, estimate formal market-based or GHG Protocol location-based corporate portfolios, calculate causal ecological impacts, or estimate feasible engineering savings.
