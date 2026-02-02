README.txt
LexiScan Auto – Legal Contract Entity Extractor (NER)

PROJECT OVERVIEW
LexiScan Auto is a production-ready NLP system designed for large financial law firms to automatically extract key legal entities from millions of PDF contracts.
The system reduces manual review effort by converting unstructured legal documents into structured, searchable data.

BUSINESS PROBLEM
Manual contract review is slow, expensive, and error-prone.
Law firms need an automated solution to extract critical legal information from both digital and scanned contracts at scale.

ENTITIES EXTRACTED

DATE

Contract start date

Contract end date

Renewal or termination dates

PARTY

Names of organizations or individuals involved in the contract

AMOUNT

Dollar values, fees, penalties, or payments

TERMINATION_CLAUSE

Clauses related to termination conditions and notice periods

SYSTEM ARCHITECTURE

PDF Input
↓
OCR using Tesseract
↓
Text Cleaning and Noise Reduction
↓
Named Entity Recognition (NER Model)
↓
Rule-Based Validation
↓
Structured JSON Output

TECH STACK

OCR : Tesseract OCR
NLP Framework : SpaCy / TensorFlow (BiLSTM)
Embeddings : GloVe / BERT (fine-tuned)
Annotation Tool : Doccano
API Framework : FastAPI
Containerization : Docker
Programming Lang : Python 3.10+

PROJECT STRUCTURE

LexiScan-Auto/
|
|-- data/
| |-- raw_pdfs/
| |-- ocr_text/
| |-- annotated/
|
|-- ocr/
| |-- ocr_engine.py
| |-- text_cleaning.py
|
|-- ner/
| |-- train.py
| |-- model.py
| |-- inference.py
| |-- embeddings.py
|
|-- postprocessing/
| |-- date_validation.py
| |-- amount_validation.py
| |-- clause_rules.py
|
|-- api/
| |-- app.py
|
|-- docker/
| |-- Dockerfile
|
|-- requirements.txt
|-- README.txt

DEVELOPMENT PLAN

WEEK 1 – OCR AND TEXT QUALITY

Handle both digital and scanned PDFs

Integrate Tesseract OCR

Remove OCR noise and artifacts

Normalize extracted text

WEEK 2 – NER MODELING

Annotate legal contracts using Doccano

Train custom NER model using BiLSTM or SpaCy

Fine-tune contextual embeddings (GloVe or BERT)

Optimize F1-score for entity extraction

WEEK 3 – POST-PROCESSING AND VALIDATION

Validate date formats (YYYY-MM-DD)

Ensure amounts contain currency symbols

Handle legal edge cases and OCR noise

Improve reliability for legal professionals

WEEK 4 – DEPLOYMENT

Containerize OCR and NLP pipeline using Docker

Expose REST API using FastAPI

Perform end-to-end testing

Input: PDF document

Output: Structured JSON

API DETAILS

Endpoint:
POST /extract-entities

Input:

PDF file or raw text

Output (Sample JSON):

{
"dates": ["2024-01-01", "2026-12-31"],
"parties": ["ABC Bank", "XYZ Finance Ltd"],
"amounts": ["$1,250,000"],
"termination_clauses": [
"Either party may terminate with 30 days written notice."
]
}

MODEL EVALUATION

Evaluation Metrics:

Precision

Recall

F1-Score (Primary Metric)

Focus Area:

Minimizing false negatives due to legal sensitivity

DOCKER DEPLOYMENT

Build Docker Image:
docker build -t lexiscan-auto .

Run Container:
docker run -p 8000:8000 lexiscan-auto

SECURITY AND COMPLIANCE

No permanent storage of contract data

Stateless REST API

Suitable for on-premise legal deployments

FUTURE ENHANCEMENTS

Legal clause classification (Confidentiality, Arbitration, Indemnity)

Multi-language contract support

Contract similarity search

Legal risk scoring