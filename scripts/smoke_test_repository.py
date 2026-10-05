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
    "notebooks/Nature_Water_Reviewer_Revision.ipynb",
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

    canonical = ROOT / "notebooks/Nature_Water_Reviewer_Revision.ipynb"
    canonical_text = canonical.read_text(encoding="utf-8")
    canonical_nb = json.loads(canonical_text)
    print("  OK: canonical Nature Water notebook is valid JSON")

    for pattern in FORBIDDEN_PATTERNS:
        if pattern in canonical_text:
            raise ValueError(
                f"Forbidden local/private path pattern found in canonical notebook: {pattern}"
            )

    code_cells = [c for c in canonical_nb.get("cells", []) if c.get("cell_type") == "code"]
    if any(c.get("execution_count") is not None for c in code_cells):
        raise ValueError("Canonical public notebook still contains execution counts.")
    if any(c.get("outputs") for c in code_cells):
        raise ValueError("Canonical public notebook still contains stored outputs.")
    print("  OK: canonical notebook has no stored outputs or execution counts")
    print("  OK: canonical notebook exposes no obvious absolute user paths")

    legacy = ROOT / "notebooks/water_consumption_hyp_clean_updated.ipynb"
    json.loads(legacy.read_text(encoding="utf-8"))
    print("  OK: legacy notebook is valid JSON")

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
