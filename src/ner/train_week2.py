import spacy
from spacy.training.example import Example
from pathlib import Path
import random

# -----------------------------
# Safe Paths
# -----------------------------
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent.parent
MODEL_PATH = PROJECT_ROOT / "week2_model"

# -----------------------------
# Training Data (Sample Legal Data)
# -----------------------------
TRAIN_DATA = [
    (
        "ABC Bank signed agreement on 2024-01-01 worth $500000.",
        {"entities": [(29, 39, "DATE"), (46, 53, "MONEY"), (0, 8, "PARTY")]}
    ),
    (
        "XYZ Finance Ltd may terminate the contract on 2025-12-31.",
        {"entities": [(0, 16, "PARTY"), (45, 55, "DATE"), (18, 27, "TERMINATION")]}
    )
]

# -----------------------------
# Create Blank Model
# -----------------------------
nlp = spacy.blank("en")

if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")

# Add labels
labels = ["DATE", "PARTY", "MONEY", "TERMINATION"]
for label in labels:
    ner.add_label(label)

# -----------------------------
# Training
# -----------------------------
optimizer = nlp.initialize()

for i in range(30):
    random.shuffle(TRAIN_DATA)
    losses = {}

    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], losses=losses)

    print(f"Iteration {i+1}, Losses: {losses}")

# -----------------------------
# Save Model
# -----------------------------
nlp.to_disk(MODEL_PATH)

print(f"\n✅ MODEL TRAINED SUCCESSFULLY")
print(f"📁 Saved at: {MODEL_PATH}")