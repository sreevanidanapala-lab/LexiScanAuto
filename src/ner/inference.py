import spacy
from pathlib import Path

MODEL_PATH = Path("ner_model")
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
        elif ent.label_ == "AMOUNT":
            result["amounts"].append(ent.text)
        elif ent.label_ == "TERMINATION_CLAUSE":
            result["termination_clauses"].append(ent.text)

    return result