# Reproducibility Notes

This repository supports the manuscript:

**The hidden water geography of U.S. hyperscale data centers in the AI era**

## Main workflow

The main workflow is documented in:

```text
notebooks/water_consumption_hyp_clean_updated.ipynb
```

## Required inputs

The notebook expects the following local files or equivalents:

```text
data/raw/facilities.csv
data/raw/BA_egrid.xlsx
data/raw/balancing_authorities_polygons/balancing_authorities_EPA.shp
data/raw/hydrobasins/hybas_lake_na_lev06_v1c.shp
data/raw/aqueduct/Aqueduct40_baseline_monthly_y2023m07d05.csv
```

The U.S. state boundary layer is loaded from the Census URL specified in the notebook.

## Minimum facility table schema

The facility table should contain, at minimum:

```text
latitude
longitude
current_mw
company_name
company_type
```

If already available, the following columns are used by the notebook:

```text
subregion_id
pfaf_id
bws_01_score
s1_m3_mid
s2_m3_mid
total_m3_mid
mwh_fac_A_mid
```

## Data restrictions

Do not commit restricted raw data. In particular, do not commit:

- vendor-provided raw files;
- exact facility addresses;
- exact facility coordinates if restricted;
- identifiable facility names if restricted by agreement;
- confidential operator-level infrastructure information.

For public release, use synthetic, anonymized, or aggregated data products.

## Outputs

Generated outputs are written to:

```text
outputs/figures/
outputs/tables/
```

## Environment

```bash
conda env create -f environment.yml
conda activate hyperscale-water-geography
python scripts/smoke_test_repository.py
```
