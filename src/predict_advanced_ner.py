import spacy
import json
from pathlib import Path

# ------------------------------
# Safe absolute paths
# ------------------------------
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
MODEL_PATH = PROJECT_ROOT / "week2_model"

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        "❌ week2_model not found.\n"
        "👉 Run train_advanced_ner.py first."
    )

nlp = spacy.load(MODEL_PATH)

text = "Beta Solutions entered a contract on December 31, 2025 worth $250,000."

doc = nlp(text)

output = {
    "Dates": [],
    "Parties": [],
    "Amounts": [],
    "TerminationClauses": []
}

for ent in doc.ents:
    if ent.label_ == "DATE":
        output["Dates"].append(ent.text)
    elif ent.label_ in ["PARTY", "ORG"]:
        output["Parties"].append(ent.text)
    elif ent.label_ == "MONEY":
        output["Amounts"].append(ent.text)
    elif ent.label_ == "TERMINATION":
        output["TerminationClauses"].append(ent.text)

print("📦 WEEK 2 STRUCTURED OUTPUT")
print(json.dumps(output, indent=4))