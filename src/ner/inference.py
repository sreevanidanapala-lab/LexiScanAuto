import spacy
from pathlib import Path

# Safe path handling
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent.parent
MODEL_PATH = PROJECT_ROOT / "week2_model"

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model not found at {MODEL_PATH}. Train model first."
    )

nlp = spacy.load(MODEL_PATH)


def extract_entities(text: str):
    doc = nlp(text)

    result = {
        "dates": [],
        "parties": [],
        "amounts": [],
        "termination_clauses": []
    }

    for ent in doc.ents:
        if ent.label_ == "DATE":
            result["dates"].append(ent.text)
        elif ent.label_ == "PARTY":
            result["parties"].append(ent.text)
        elif ent.label_ == "MONEY":
            result["amounts"].append(ent.text)
        elif ent.label_ == "TERMINATION":
            result["termination_clauses"].append(ent.text)

    return result