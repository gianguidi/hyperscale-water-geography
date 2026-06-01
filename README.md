# Hyperscale Water Geography

Reproducibility materials for the manuscript:

**The hidden water geography of U.S. hyperscale data centers in the AI era**

This repository contains the analysis notebook, environment file, repository checks, and placeholders for non-public input data. The workflow estimates operational water consumption for U.S. hyperscale data centers by separating:

1. **Direct cooling water consumption** linked to hydrologic basins.
2. **Electricity-related water consumption** linked to electricity balancing authorities.

## Repository structure

```text
notebooks/
  water_consumption_hyp_clean_updated.ipynb

scripts/
  config.example.yml
  smoke_test_repository.py
  clear_notebook_outputs.py

data/
  raw/          # place local/raw inputs here; not publicly distributed
  processed/    # optional processed/synthetic/anonymized inputs

outputs/
  figures/      # generated manuscript figures
  tables/       # generated manuscript tables

src/
  hyperscale_water_geography/
```

## Data availability and restrictions

The underlying facility-level dataset may contain commercially sensitive information. Do **not** commit raw facility identifiers, addresses, exact coordinates, or vendor-provided files unless they are cleared for public release. Public versions of this repository should include only synthetic, anonymized, or aggregated data products.

Expected local input paths used by the notebook are listed in `scripts/config.example.yml`.

## Environment

Create the conda environment:

```bash
conda env create -f environment.yml
conda activate hyperscale-water-geography
```

Or install the Python dependencies with pip:

```bash
pip install -r requirements.txt
```

## Smoke test

Run this before pushing to GitHub:

```bash
python scripts/smoke_test_repository.py
```

The smoke test checks the repository structure, validates the notebook JSON, and scans for common local hard-coded paths.

## Running the analysis

Open and run:

```text
notebooks/water_consumption_hyp_clean_updated.ipynb
```

The notebook writes outputs to:

```text
outputs/
```

## Suggested Git workflow

```bash
git status
python scripts/smoke_test_repository.py
git add README.md REPRO.md environment.yml requirements.txt .gitignore scripts notebooks src data/raw/.gitkeep data/processed/.gitkeep outputs/figures/.gitkeep outputs/tables/.gitkeep
git commit -m "Initialize reproducibility repository for water manuscript"
git push -u origin main
```
