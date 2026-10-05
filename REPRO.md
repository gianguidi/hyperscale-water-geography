# Reproducibility Notes

This repository supports the transferred Nature Water manuscript:

**One footprint, many maps: the hidden geography of U.S. data-centre water use**

Transfer date: **5 October 2026**

## 1. Analytical estimand

The analysis is an annualized current-capacity screening model for a frozen 15 December 2025 Baxtel inventory. The primary model interprets `current_mw` as **facility-input nameplate power**. It does not claim to be an operating census or a facility-metered water inventory.

The two reported operational-water pathways are:

- **on-site water consumption** associated with facility operation and cooling assumptions;
- **electricity-related water consumption** attributed from the annual production mix of the facility-hosting balancing authority.

The analysis excludes construction, servers, semiconductor fabrication, fuels and other value-chain water.

## 2. Required empirical inputs

The canonical empirical run requires lawful access to the restricted facility inventory plus the following public or project-archived inputs:

```text
Baxtel facility snapshot: 15 December 2025
EPA eGRID2023 Revision 2 BA-level generation mix
WattTime/project-archived BA polygons:
  balancing_authorities_polygons/balancing_authorities_EPA.shp
  join field: region_B_1
HydroBASINS level 6, North America v1c
WRI Aqueduct 4.0 annual baseline fields:
  bws_score
  bwd_score
U.S. Census state boundary layer
```

The Aqueduct input must be an **annual baseline** layer containing `bws_score` and `bwd_score`. A monthly Aqueduct file is not a valid substitute for the reported annual indicators.

## 3. Canonical table and validation contracts

Every reported national and regional result must derive from one canonical facility-by-scenario table. A successful figure-generating run must pass all of the following:

| Contract | Pass condition |
|---|---|
| Input identity | Required inputs exist; checksums and configuration hash recorded |
| Inventory uniqueness | One unique facility row after eligibility filtering |
| Spatial assignment | At most one state, BA and hosting basin per facility; required coverage complete |
| Annual Aqueduct schema | Annual BWS/BWD fields; unique basin key; valid 0-5 scores after no-data removal |
| BA mix | Seven non-negative shares; pre-normalization sum within 0.98-1.02 |
| Canonical uniqueness | One row per facility-scenario with expected scenario coverage |
| Non-negativity | Electricity and both water pathways finite and non-negative |
| Additive identity | `W_total = W_onsite + W_electricity` within tolerance |
| Aggregation conservation | State, BA and basin sums reconcile to the relevant national pathway total |
| Subset bound | Every ranked/top-region subset is no greater than its parent national total |
| Scenario isolation | No-hydropower case retains baseline activity/cooling parameters and changes only the hydropower factor |

The earlier regional profile products that violated subset/national conservation were discarded and must not be regenerated or used.

## 4. Transfer-version numerical targets

The released aggregate tables in `outputs/tables/` encode the current manuscript targets.

Baseline/reference:

- 472 provider-defined records;
- 20,041 MW reported current capacity;
- 115.87 TWh/yr facility-input electricity;
- 74.16 GL/yr on site;
- 225.74 GL/yr electricity-related;
- 299.89 GL/yr total;
- electricity-related share 75.27%.

Regional screening:

- 63 positive-burden hosting basins;
- 62 with valid annual Aqueduct context;
- 10 of 63 basins reach >=50% of on-site consumption;
- 24 hosting BAs;
- 3 of 24 BAs reach >=50% of electricity-related consumption;
- BWS score >=3: 25 basins, 15 also at least median on-site burden;
- BWD score >=3: 7 basins, 6 also at least median on-site burden.

Hydropower attribution:

- selected reference hydropower factor: 8.0 L/kWh;
- zero-hydropower sensitivity: 128.35 GL/yr electricity-related and 202.50 GL/yr total;
- zeroing hydropower lowers the displayed baseline electricity pathway by 97.39 GL/yr (43.1%);
- a deterministic comparison using approximately 6.1 L/kWh gives about 202.6 GL/yr electricity-related and 276.8 GL/yr total.

## 5. Spatial interpretation

### On-site pathway

Facilities are assigned to facility-hosting HydroBASINS level-6 polygons. This does **not** establish the water utility's intake basin. Under a common scenario parameter set, on-site basin burden is proportional to summed reported facility capacity and is not a measured cooling-performance map.

### Electricity pathway

Facilities are assigned by point-in-polygon to the project-archived BA layer. The resulting quantity is a **hosting-BA production-mix attribution**. It is not plant-level electricity tracing, a physical source-water map, retail-utility assignment, or formal GHG Protocol location-based/market-based accounting.

## 6. Data availability boundary

The Baxtel source records cannot be redistributed by the authors. Public release should contain only non-restricted materials such as:

- scenario configuration;
- aggregate figure-source tables;
- non-restricted spatial crosswalks;
- validation reports;
- input checksums and configuration hash;
- output manifest;
- synthetic-input workflow.

Independent end-to-end reconstruction of the empirical facility-to-geography joins requires lawful access to the licensed Baxtel file.

## 7. Notebook status

`notebooks/water_consumption_hyp_clean_updated.ipynb` predates the corrected transfer workflow and is retained as a legacy provenance artifact. It should not be cited as the canonical source of the transferred regional figures.

The versioned release corresponding to the accepted manuscript should include the corrected canonical code path, validation outputs, figure-source tables, exact input hashes/configuration hash and output manifest.

## 8. Environment

```bash
conda env create -f environment.yml
conda activate hyperscale-water-geography
python scripts/validate_submission_snapshot.py
python scripts/smoke_test_repository.py
```
