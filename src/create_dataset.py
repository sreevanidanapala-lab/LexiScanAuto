import json
from pathlib import Path
import sys

# ✅ Make src import-safe
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
sys.path.append(str(CURRENT_DIR))

from utils import find_entities

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw_contracts" / "sample_contracts.txt"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "ner_training_data.json"

def create_ner_data():
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"File not found: {RAW_DATA_PATH}")

    training_data = []

    with open(RAW_DATA_PATH, "r", encoding="utf-8") as file:
        contracts = file.read().split("\n\n")

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

    print("✅ NER training data successfully created!")
    print(f"📁 Saved at: {OUTPUT_PATH}")

if __name__ == "__main__":
    create_ner_data()