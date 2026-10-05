# Hyperscale Water Geography

Reproducibility materials for the Nature Water transfer of **One footprint, many maps: the hidden geography of U.S. data-centre water use** by Gianluca Guidi and Francesca Dominici.

## Canonical transfer analysis

The canonical notebook used for the revised analysis is `notebooks/Nature_Water_Reviewer_Revision.ipynb`. It reproduces the transferred headline results and implements the corrected canonical facility-by-scenario workflow with accounting and aggregation-conservation checks.

`notebooks/water_consumption_hyp_clean_updated.ipynb` is retained only as legacy provenance from the earlier manuscript version and should not be used to reproduce the transferred regional figures.

## Headline transfer results

| Scenario | Facility electricity (TWh/yr) | On-site water (GL/yr) | Electricity-related water (GL/yr) | Total (GL/yr) |
|---|---:|---:|---:|---:|
| Lower-load/lower-water | 96.56 | 16.79 | 188.11 | 204.91 |
| Baseline/reference | 115.87 | 74.16 | 225.74 | 299.89 |
| Higher-load/water-intensive | 149.22 | 159.88 | 290.72 | 450.60 |
| No hydropower attribution | 115.87 | 74.16 | 128.35 | 202.50 |

Regional screening: 63 positive-burden hosting basins, 62 with valid annual Aqueduct context, 10 basins to reach at least half of on-site consumption, 24 hosting BAs, and 3 BAs to reach at least half of electricity-related consumption. Annual Aqueduct BWS score >=3 flags 25 hosting basins (15 also at least median burden); BWD score >=3 flags 7 (6 also at least median burden).

These are scenario-based screening outputs, not facility-metered water use, ecological impact estimates, or plant-level electricity tracing.

## Reproducibility boundary

The source facility inventory is commercially licensed from Baxtel and cannot be redistributed. Public materials therefore support computational reproduction from non-restricted derived outputs, while full reconstruction of the facility-to-geography joins requires lawful access to the licensed source file.

The corrected workflow requires unique facility-scenario rows, complete required spatial assignments, normalized BA generation shares, non-negative quantities, `W_total = W_onsite + W_electricity`, state/BA/basin conservation, ranked-subset bounds, and scenario isolation for the no-hydropower sensitivity.

See `REPRO.md` and `SUBMISSION_SNAPSHOT.md` for details.

## Environment and checks

```bash
conda env create -f environment.yml
conda activate hyperscale-water-geography
python scripts/validate_submission_snapshot.py
python scripts/smoke_test_repository.py
```
