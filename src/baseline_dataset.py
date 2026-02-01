import json
import re
from pathlib import Path

# ------------------------------
# Safe paths: always relative to this script
# ------------------------------
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw_contracts" / "sample_contracts.txt"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "week1_training_data.json"

# ------------------------------
# Check file exists
# ------------------------------
if not RAW_DATA_PATH.exists():
    raise FileNotFoundError(f"File not found: {RAW_DATA_PATH}")

# ------------------------------
# Function to extract entities
# ------------------------------
def find_entities(text):
    entities = []
    patterns = {
        "DATE": r"(January|March|December)\s\d{1,2},\s\d{4}",
        "PARTY": r"(Alpha Corp|Beta Solutions|Global Finance Ltd|Orion Tech)",
        "MONEY": r"\$\d{1,3}(?:,\d+)*(?:\.\d+)?",
        "TERMINATION": r"\b(terminated|termination)\b"
    }
    for label, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            entities.append((match.start(), match.end(), label))
    return entities

# ------------------------------
# Read raw contracts
# ------------------------------
with open(RAW_DATA_PATH, encoding="utf-8") as f:
    contracts = f.read().split("\n\n")

training_data = []
for contract in contracts:
    if contract.strip():
        entities = find_entities(contract)
        training_data.append((contract, {"entities": entities}))

# ------------------------------
# Create processed folder if not exist
# ------------------------------
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# ------------------------------
# Save training data
# ------------------------------
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(training_data, f, indent=4)

print("✅ WEEK 1 DATA CREATED")
print(f"Saved at: {OUTPUT_PATH}")