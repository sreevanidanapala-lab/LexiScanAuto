import spacy
import json
from pathlib import Path
from spacy.training import Example

# ------------------------------
# Safe absolute paths
# ------------------------------
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent

TRAIN_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "week1_training_data.json"
MODEL_PATH = PROJECT_ROOT / "week1_model"

# ------------------------------
# Check training data
# ------------------------------
if not TRAIN_DATA_PATH.exists():
    raise FileNotFoundError(
        f"Training data not found: {TRAIN_DATA_PATH}\n"
        "👉 Run baseline_dataset.py first."
    )

# ------------------------------
# Load training data
# ------------------------------
with open(TRAIN_DATA_PATH, "r", encoding="utf-8") as f:
    TRAIN_DATA = json.load(f)

# ------------------------------
# Create spaCy pipeline
# ------------------------------
nlp = spacy.blank("en")

if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")

# Add labels
for _, annotations in TRAIN_DATA:
    for start, end, label in annotations["entities"]:
        ner.add_label(label)

# Initialize model
nlp.initialize()

# ------------------------------
# TRAIN LOOP (spaCy 3 compliant)
# ------------------------------
for epoch in range(10):
    losses = {}

    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], losses=losses)

    print(f"Epoch {epoch + 1} | Loss: {losses}")

# ------------------------------
# Save model
# ------------------------------
nlp.to_disk(MODEL_PATH)
print(f"✅ WEEK 1 MODEL SAVED AT: {MODEL_PATH}")