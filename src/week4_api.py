from fastapi import FastAPI
from pydantic import BaseModel
import spacy
from pathlib import Path
from src.validator import validate_entities

# ---------------------------
# Load Trained Model
# ---------------------------
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
MODEL_PATH = PROJECT_ROOT / "week2_model"

nlp = spacy.load(MODEL_PATH)

app = FastAPI(title="LexiScan Auto API")

# ---------------------------
# Request Model
# ---------------------------
class ContractRequest(BaseModel):
    text: str


# ---------------------------
# Home Route
# ---------------------------
@app.get("/")
def home():
    return {"message": "LexiScan Auto API Running Successfully"}


# ---------------------------
# Entity Extraction Route
# ---------------------------
@app.post("/extract")
def extract_entities(request: ContractRequest):

    doc = nlp(request.text)

    raw_output = {
        "Dates": [],
        "Parties": [],
        "Amounts": [],
        "TerminationClauses": []
    }

    for ent in doc.ents:
        if ent.label_ == "DATE":
            raw_output["Dates"].append(ent.text)
        elif ent.label_ == "PARTY":
            raw_output["Parties"].append(ent.text)
        elif ent.label_ == "MONEY":
            raw_output["Amounts"].append(ent.text)
        elif ent.label_ == "TERMINATION":
            raw_output["TerminationClauses"].append(ent.text)

    validated_output = validate_entities(raw_output)

    return validated_output