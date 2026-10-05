# Data directory

Place local empirical inputs under `data/raw/`. Do **not** commit restricted facility-level data, exact coordinates, addresses, vendor-provided identifiers, or other Baxtel-supplied record-level fields unless explicitly cleared for public release.

The corrected transfer workflow requires local equivalents of:

```text
data/raw/facilities.csv
data/raw/BA_egrid.xlsx
data/raw/balancing_authorities_polygons/balancing_authorities_EPA.shp
data/raw/hydrobasins/hybas_lake_na_lev06_v1c.shp
data/raw/aqueduct/Aqueduct40_baseline_annual.csv
```

The Aqueduct file name above is a local convention. The underlying input must provide **Aqueduct 4.0 annual baseline** values for both:

```text
bws_score
bwd_score
```

Do not substitute the earlier monthly Aqueduct file used by the legacy notebook.

The empirical facility snapshot used by the transferred manuscript is a commercially licensed Baxtel file frozen on 15 December 2025. It is not distributable in this repository.
