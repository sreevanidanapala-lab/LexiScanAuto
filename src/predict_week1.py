import spacy
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
MODEL_PATH = PROJECT_ROOT / "week1_model"

if not MODEL_PATH.exists():
    raise FileNotFoundError("❌ week1_model not found. Run train_week1.py first.")

nlp = spacy.load(MODEL_PATH)

text = "Alpha Corp signed the agreement on January 15, 2022 for $250,000."

doc = nlp(text)

print("🔍 WEEK 1 PREDICTIONS")
for ent in doc.ents:
    print(ent.text, "->", ent.label_)