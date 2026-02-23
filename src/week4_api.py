from fastapi import FastAPI
from pydantic import BaseModel
import importlib.util
from pathlib import Path
import spacy

# ----------------------------
# Load 3_validator.py
# ----------------------------
CURRENT_DIR = Path(__file__).resolve().parent
validator_path = CURRENT_DIR / "3_validator.py"

spec = importlib.util.spec_from_file_location("validator", validator_path)
validator_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator_module)

validate_entities = validator_module.validate_entities

# ----------------------------
# Load Model
# ----------------------------
PROJECT_ROOT = CURRENT_DIR.parent
MODEL_PATH = PROJECT_ROOT / "week2_model"
nlp = spacy.load(MODEL_PATH)

app = FastAPI(title="LexiScan Auto API")


class ContractInput(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "LexiScan Auto API Running Successfully"}


@app.post("/extract")
def extract(contract: ContractInput):

    doc = nlp(contract.text)

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

    validated = validate_entities(raw)

    return {
        "product": "LexiScan Auto",
        "status": "success",
        "extracted_entities": validated
    }