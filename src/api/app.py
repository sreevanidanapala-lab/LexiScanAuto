from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from ner.inference import extract_entities
from postprocessing.validator import validate_output
from ocr.ocr_engine import extract_text_from_pdf
from ocr.text_cleaning import clean_text
import tempfile

app = FastAPI(title="LexiScan Auto API")

class TextRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "LexiScan Auto Running"}


@app.post("/extract-entities")
async def extract_entities_api(file: UploadFile = File(None), request: TextRequest = None):

    if file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            text = extract_text_from_pdf(tmp.name)
    elif request:
        text = request.text
    else:
        return {"error": "Provide PDF file or raw text"}

    cleaned_text = clean_text(text)
    raw_output = extract_entities(cleaned_text)
    validated = validate_output(raw_output)

    return validated