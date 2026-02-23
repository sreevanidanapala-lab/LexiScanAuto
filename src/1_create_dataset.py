import json
from pathlib import Path
from utils import find_entities

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent

RAW_DATA = PROJECT_ROOT / "data" / "raw_contracts" / "sample_contracts.txt"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "ner_training_data.json"

if not RAW_DATA.exists():
    raise FileNotFoundError("Raw contract file missing!")

training_data = []

with open(RAW_DATA, "r", encoding="utf-8") as f:
    contracts = f.read().split("\n\n")

for contract in contracts:
    if contract.strip():
        entities = find_entities(contract)
        training_data.append({
            "text": contract,
            "entities": entities
        })

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(training_data, f, indent=4)

print("✅ WEEK 1 COMPLETE – Dataset Created")
print("Saved at:", OUTPUT_PATH)