from fastapi import FastAPI
from pydantic import BaseModel
from src.ner.inference import extract_entities
from src.postprocessing.validator import validate_entities

app = FastAPI(title="LexiScan Auto API")


class ContractRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "LexiScan Auto Running Successfully"}


@app.post("/extract-entities")
def extract(request: ContractRequest):
    raw_output = extract_entities(request.text)
    validated_output = validate_entities(raw_output)
    return validated_output