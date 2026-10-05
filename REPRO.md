# Reproducibility Notes

This repository supports the Nature Water transfer of **One footprint, many maps: the hidden geography of U.S. data-centre water use** (5 October 2026).

## Canonical notebook

The revised empirical analysis was run from `notebooks/Nature_Water_Reviewer_Revision.ipynb`. The notebook builds one canonical facility-by-scenario table, validates the accounting and geography assignments before aggregation, and generates the transfer-version national and regional outputs from that run.

The older `notebooks/water_consumption_hyp_clean_updated.ipynb` is legacy provenance only.

## Analytical estimand

The analysis is an annualized current-capacity screening model for a frozen 15 December 2025 Baxtel inventory. The primary model interprets `current_mw` as facility-input nameplate power. It does not claim to be an operating census or a facility-metered water inventory.

The reported pathways are on-site operational water consumption and electricity-related operational water consumption attributed from the annual production mix of the facility-hosting balancing authority.

## Required empirical inputs

- Baxtel facility snapshot: 15 December 2025
- EPA eGRID2023 Revision 2 BA-level generation mix
- project-archived WattTime BA polygons, joined on `region_B_1`
- HydroBASINS level 6, North America v1c
- WRI Aqueduct 4.0 annual `bws_score` and `bwd_score`
- U.S. Census state boundaries

A monthly Aqueduct field must not be substituted for the reported annual BWS/BWD indicators.

## Mandatory validation contracts

| Contract | Pass condition |
|---|---|
| Input identity | Required inputs exist and run identity is recorded |
| Inventory uniqueness | One unique facility row after eligibility filtering |
| Spatial assignment | Required state, BA and hosting-basin assignments are valid |
| Aqueduct schema | Annual BWS/BWD fields with valid scores |
| BA mix | Non-negative shares and valid normalization |
| Canonical uniqueness | One row per facility-scenario |
| Non-negativity | Electricity and water quantities are finite and non-negative |
| Additive identity | `W_total = W_onsite + W_electricity` |
| Aggregation conservation | State, BA and basin sums reconcile to national pathway totals |
| Subset bound | Ranked/top-region subsets do not exceed parent totals |
| Scenario isolation | No-hydropower case changes only the hydropower factor |

## Transfer-version targets

Baseline/reference: 472 records, 20,041 MW, 115.87 TWh/yr facility-input electricity, 74.16 GL/yr on site, 225.74 GL/yr electricity-related, 299.89 GL/yr total.

Regional screening: 63 positive-burden hosting basins; 62 with valid annual Aqueduct context; 10 basins to reach >=50% of on-site consumption; 24 hosting BAs; 3 BAs to reach >=50% of electricity-related consumption. BWS score >=3 flags 25 hosting basins, 15 also at least median burden; BWD score >=3 flags 7, 6 also at least median burden.

Hydropower sensitivity: zero attribution gives 128.35 GL/yr electricity-related and 202.50 GL/yr total; the reduction from the reference electricity pathway is 97.39 GL/yr (43.1%).

## Interpretation boundary

Hosting HydroBASINS polygons are not verified utility intake basins. Hosting-BA attribution is not plant-level tracing, a physical source-water map, retail-utility assignment, or formal market-based corporate accounting.

The Baxtel source records cannot be redistributed. The public release therefore includes non-restricted documentation, aggregate tables, validation material, code, and the canonical notebook, while end-to-end reconstruction of the empirical joins requires lawful access to the licensed facility file.
