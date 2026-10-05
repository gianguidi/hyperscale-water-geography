from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "REPRO.md",
    "SUBMISSION_SNAPSHOT.md",
    "environment.yml",
    "requirements.txt",
    ".gitignore",
    "notebooks/water_consumption_hyp_clean_updated.ipynb",
    "scripts/config.example.yml",
    "scripts/validate_submission_snapshot.py",
    "data/raw",
    "data/processed",
    "outputs/figures",
    "outputs/tables/national_scenarios.csv",
    "outputs/tables/screening_summary.csv",
    "outputs/tables/hydropower_sensitivity.csv",
    "src/hyperscale_water_geography/__init__.py",
]

FORBIDDEN_PATTERNS = [
    "/Users/",
    "C:\\Users\\",
    "Harvard US-Sites 2025-12-15.csv",
]

LEGACY_PUBLIC_CONFIG_PATTERNS = [
    "Aqueduct40_baseline_monthly",
    "bws_01_score",
]

def main() -> None:
    print("Smoke testing repository structure...")
    for rel in REQUIRED_PATHS:
        path = ROOT / rel
        if not path.exists():
            raise FileNotFoundError(f"Missing required path: {rel}")
        print(f"  OK: {rel}")

    nb_path = ROOT / "notebooks/water_consumption_hyp_clean_updated.ipynb"
    nb_text = nb_path.read_text(encoding="utf-8")
    json.loads(nb_text)
    print("  OK: legacy notebook is valid JSON")

    for pattern in FORBIDDEN_PATTERNS:
        if pattern in nb_text:
            raise ValueError(
                f"Forbidden local/private path pattern found in notebook: {pattern}"
            )
    print("  OK: no obvious local/private path patterns in notebook")

    config_text = (ROOT / "scripts/config.example.yml").read_text(encoding="utf-8")
    for pattern in LEGACY_PUBLIC_CONFIG_PATTERNS:
        if pattern in config_text:
            raise ValueError(
                f"Legacy transfer-inconsistent pattern remains in public config: {pattern}"
            )
    print("  OK: public example config points to annual Aqueduct fields")

    print("Repository smoke test passed.")
    print("Next run: python scripts/validate_submission_snapshot.py")

if __name__ == "__main__":
    main()
