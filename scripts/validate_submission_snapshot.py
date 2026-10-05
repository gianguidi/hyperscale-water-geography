from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
TOL = 0.03

def read_csv(name: str):
    with (TABLES / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol

def main() -> None:
    rows = read_csv("national_scenarios.csv")
    assert len(rows) == 4, "Expected four public scenario rows"

    for row in rows:
        onsite = float(row["onsite_water_gl_yr"])
        elec = float(row["electricity_related_water_gl_yr"])
        total = float(row["total_water_gl_yr"])
        assert close(onsite + elec, total), (
            f"Additive identity failed for {row['scenario']}: "
            f"{onsite} + {elec} != {total}"
        )
        onsite_share = float(row["onsite_share_pct"])
        elec_share = float(row["electricity_related_share_pct"])
        assert close(onsite_share + elec_share, 100.0, 0.05), (
            f"Shares do not sum to 100 for {row['scenario']}"
        )

    baseline = next(r for r in rows if r["scenario"] == "baseline/reference")
    no_hydro = next(r for r in rows if r["scenario"] == "no-hydropower-attribution")

    assert close(float(baseline["total_water_gl_yr"]), 299.89)
    assert close(float(baseline["onsite_water_gl_yr"]), 74.16)
    assert close(float(baseline["electricity_related_water_gl_yr"]), 225.74)
    assert close(float(no_hydro["electricity_related_water_gl_yr"]), 128.35)
    assert close(float(no_hydro["total_water_gl_yr"]), 202.50)

    drop = float(baseline["electricity_related_water_gl_yr"]) - float(
        no_hydro["electricity_related_water_gl_yr"]
    )
    assert close(drop, 97.39), f"Hydropower sensitivity mismatch: {drop}"

    metrics = {r["metric"]: float(r["value"]) for r in read_csv("screening_summary.csv")}
    assert int(metrics["inventory_records"]) == 472
    assert int(metrics["reported_current_capacity_mw"]) == 20041
    assert int(metrics["positive_burden_hosting_basins"]) == 63
    assert int(metrics["hosting_basins_with_valid_annual_aqueduct_context"]) == 62
    assert int(metrics["basins_to_reach_ge_50pct_onsite"]) == 10
    assert int(metrics["hosting_balancing_authorities"]) == 24
    assert int(metrics["bas_to_reach_ge_50pct_electricity_related"]) == 3
    assert int(metrics["bws_score_ge_3_hosting_basins"]) == 25
    assert int(metrics["bwd_score_ge_3_hosting_basins"]) == 7

    assert metrics["basins_to_reach_ge_50pct_onsite"] <= metrics["positive_burden_hosting_basins"]
    assert metrics["bas_to_reach_ge_50pct_electricity_related"] <= metrics["hosting_balancing_authorities"]

    print("Transfer-version public snapshot validation passed.")

if __name__ == "__main__":
    main()
