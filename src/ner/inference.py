import re
import sys
from pathlib import Path
import spacy

# -------------------------------------------------
# FIX PYTHON PATH (so it works when run directly)
# -------------------------------------------------
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent.parent

# Add src folder to Python path
sys.path.append(str(PROJECT_ROOT / "src"))

# Now import rule extractor safely
try:
    from ner.rule_extractor import extract_parties, extract_termination_clauses
except ImportError:
    # If running directly inside ner folder
    from rule_extractor import extract_parties, extract_termination_clauses


# -------------------------------------------------
# LOAD MODEL
# -------------------------------------------------
MODEL_PATH = PROJECT_ROOT / "week2_model"

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model not found at {MODEL_PATH}. Train model first."
    )

nlp = spacy.load(MODEL_PATH)


# -------------------------------------------------
# MAIN EXTRACTION FUNCTION
# -------------------------------------------------
def extract_entities(text):

    doc = nlp(text)

    output = {
        "dates": [],
        "parties": [],
        "amounts": [],
        "termination_clauses": []
    }

    # SpaCy NER results
    for ent in doc.ents:
        if ent.label_ == "DATE":
            output["dates"].append(ent.text)

        elif ent.label_ == "MONEY":
            output["amounts"].append(ent.text)

    # Rule-based extraction
    output["parties"] = extract_parties(text)
    output["termination_clauses"] = extract_termination_clauses(text)

    return output


# -------------------------------------------------
# RUN DIRECTLY (Testing)
# -------------------------------------------------
if __name__ == "__main__":

    sample_text = """
    Service Agreement entered on 2024-03-15 between Alpha Technologies Pvt Ltd and Beta Retail Solutions.

    Alpha Technologies Pvt Ltd agrees to provide IT consulting services for $300,000.

    This Agreement may be terminated by either party with 60 days written notice.

    In case of material breach, the non-breaching party may terminate immediately.
    """

    result = extract_entities(sample_text)

    print("\n✅ EXTRACTION RESULT\n")
    for key, value in result.items():
        print(f"{key}: {value}")