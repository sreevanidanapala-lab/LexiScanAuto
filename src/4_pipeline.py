import spacy
import json
from pathlib import Path
import importlib.util

# ----------------------------
# Load 3_validator.py manually
# ----------------------------
CURRENT_DIR = Path(__file__).resolve().parent

validator_path = CURRENT_DIR / "validator.py"

spec = importlib.util.spec_from_file_location("validator", validator_path)
validator_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator_module)

validate_entities = validator_module.validate_entities

# ----------------------------
# Load trained model
# ----------------------------
PROJECT_ROOT = CURRENT_DIR.parent
MODEL_PATH = PROJECT_ROOT / "week2_model"

if not MODEL_PATH.exists():
    raise FileNotFoundError("❌ week2_model not found. Train Week 2 first.")

nlp = spacy.load(MODEL_PATH)


def extract_entities(text):

    doc = nlp(text)

    raw = {
        "Dates": [],
        "Parties": [],
        "Amounts": [],
        "TerminationClauses": []
    }

    for ent in doc.ents:
        if ent.label_ == "DATE":
            raw["Dates"].append(ent.text)
        elif ent.label_ == "PARTY":
            raw["Parties"].append(ent.text)
        elif ent.label_ == "MONEY":
            raw["Amounts"].append(ent.text)
        elif ent.label_ == "TERMINATION":
            raw["TerminationClauses"].append(ent.text)

    return validate_entities(raw)


# ----------------------------
# Test block
# ----------------------------
if __name__ == "__main__":
    test_text = "Beta Solutions signed on December 31, 2025 for $500,000."

    result = extract_entities(test_text)

    print("\n📦 WEEK 3 VALIDATED OUTPUT")
    print(json.dumps(result, indent=4))