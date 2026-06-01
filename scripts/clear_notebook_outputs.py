\
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
NB = ROOT / "notebooks" / "water_consumption_hyp_clean_updated.ipynb"

nb = json.loads(NB.read_text(encoding="utf-8"))
for cell in nb.get("cells", []):
    if cell.get("cell_type") == "code":
        cell["outputs"] = []
        cell["execution_count"] = None

NB.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"Cleared outputs: {NB}")
