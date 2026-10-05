# Hyperscale Water Geography

Reproducibility materials for the manuscript:

**One footprint, many maps: the hidden geography of U.S. data-centre water use**

Authors: Gianluca Guidi and Francesca Dominici

This repository is being updated to match the substantially revised manuscript transferred to **Nature Water** on 5 October 2026. The transfer version replaces the earlier regional reporting path that produced internally inconsistent regional totals.

## Transfer-version headline results

The current manuscript uses a 15 December 2025 Baxtel snapshot containing 472 provider-defined U.S. hyperscale records and 20,041 MW of reported current capacity, interpreted in the primary model as facility-input nameplate power.

| Scenario | Facility electricity (TWh/yr) | On-site water (GL/yr) | Electricity-related water (GL/yr) | Total (GL/yr) |
|---|---:|---:|---:|---:|
| Lower-load/lower-water | 96.56 | 16.79 | 188.11 | 204.91 |
| Baseline/reference | 115.87 | 74.16 | 225.74 | 299.89 |
| Higher-load/water-intensive | 149.22 | 159.88 | 290.72 | 450.60 |
| No hydropower attribution | 115.87 | 74.16 | 128.35 | 202.50 |

Additional transfer-version screening results:

- 63 positive-burden facility-hosting HydroBASINS level-6 basins;
- 62 of those basins have valid annual Aqueduct context;
- 10 of 63 hosting basins reach at least 50% of modeled on-site consumption;
- 24 facility-hosting balancing authorities (BAs);
- 3 of 24 hosting BAs reach at least 50% of modeled electricity-related consumption;
- annual Aqueduct baseline water stress (BWS) score >= 3 flags 25 hosting basins, 15 of which also have at-least-median on-site burden;
- annual baseline water depletion (BWD) score >= 3 flags 7 hosting basins, 6 of which also have at-least-median on-site burden.

These are scenario-based screening outputs, not facility-metered water use, ecological impact estimates, or plant-level electricity tracing.

## Current analytical framing

The revised workflow separates two operational pathways:

1. **On-site water consumption**, screened in the facility-hosting HydroBASINS level-6 basin.
2. **Electricity-related water consumption**, attributed using the annual production mix of the facility-hosting BA.

The two spatial partitions are not physically commensurate. Concentration results are therefore interpreted within each partition rather than as a scale-free test that one pathway is intrinsically more clustered.

## Repository status

The public repository is being aligned with the Nature Water transfer in two layers:

- **Current transfer-facing aggregate outputs and documentation** are provided under `outputs/tables/`, `SUBMISSION_SNAPSHOT.md`, and `REPRO.md`.
- `notebooks/water_consumption_hyp_clean_updated.ipynb` is retained for provenance from the earlier manuscript version and **must not be treated as the canonical source of the transferred regional figures**. The corrected canonical analysis package should replace or supersede it in the versioned release corresponding to the accepted manuscript.

This distinction is intentional: the licensed facility-level Baxtel records cannot be redistributed, and the revised manuscript explicitly separates reproduction of released aggregate outputs from full reconstruction of the proprietary facility-to-geography joins.

## Reproducibility boundary

The corrected workflow is defined around one immutable facility-by-scenario table and mandatory validation contracts covering:

- unique facility-scenario rows;
- required spatial assignments;
- normalized BA generation shares;
- non-negative electricity and water quantities;
- additive identity `W_total = W_onsite + W_electricity`;
- state, BA and basin aggregation conservation;
- ranked-subset totals no greater than the corresponding national total;
- scenario isolation for the no-hydropower sensitivity.

See `REPRO.md` for the full boundary and input vintages.

## Data restrictions

The source facility inventory was supplied under a commercial third-party licence by **Baxtel**. Do not commit provider-supplied identifiers, exact coordinates, addresses, or other restricted record-level fields. Independent reconstruction of the source inventory requires lawful access obtained directly from Baxtel under its applicable terms.

Public inputs used by the analysis include EPA eGRID2023 Revision 2, WRI Aqueduct 4.0, HydroBASINS level 6, a project-archived WattTime BA boundary layer, and U.S. Census boundaries.

## Environment

```bash
conda env create -f environment.yml
conda activate hyperscale-water-geography
```

or:

```bash
pip install -r requirements.txt
```

## Public snapshot validation

```bash
python scripts/validate_submission_snapshot.py
python scripts/smoke_test_repository.py
```

The first command checks the arithmetic and key invariants in the public transfer-version aggregate tables. It does **not** substitute for rerunning the licensed facility-level analysis.
