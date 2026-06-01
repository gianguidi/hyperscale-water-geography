\
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "REPRO.md",
    "environment.yml",
    "requirements.txt",
    ".gitignore",
    "notebooks/water_consumption_hyp_clean_updated.ipynb",
    "scripts/config.example.yml",
    "data/raw",
    "data/processed",
    "outputs/figures",
    "outputs/tables",
    "src/hyperscale_water_geography/__init__.py",
]

FORBIDDEN_PATTERNS = [
    "/Users/",
    "C:\\\\Users\\\\",
    "Harvard US-Sites 2025-12-15.csv",
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
    print("  OK: notebook is valid JSON")

    for pattern in FORBIDDEN_PATTERNS:
        if pattern in nb_text:
            raise ValueError(f"Forbidden local/private path pattern found in notebook: {pattern}")
    print("  OK: no obvious local/private path patterns in notebook")

    print("Repository smoke test passed.")

if __name__ == "__main__":
    main()
