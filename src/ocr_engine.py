import pytesseract
from pdf2image import convert_from_path
from pathlib import Path

def extract_text_from_pdf(pdf_path: str) -> str:
    images = convert_from_path(pdf_path)
    full_text = ""

    for image in images:
        text = pytesseract.image_to_string(image)
        full_text += text + "\n"

    return full_text