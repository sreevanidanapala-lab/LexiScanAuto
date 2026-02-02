import spacy
from pathlib import Path

# ------------------------------
# Safe absolute paths
# ------------------------------
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
MODEL_PATH = PROJECT_ROOT / "week2_model"

# ------------------------------
# Create blank English pipeline
# ------------------------------
nlp = spacy.blank("en")

if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")

# Add labels (production entities)
labels = ["DATE", "PARTY", "MONEY", "TERMINATION"]
for label in labels:
    ner.add_label(label)

# Initialize and save model
nlp.initialize()
nlp.to_disk(MODEL_PATH)

print(f" WEEK 2 MODEL CREATED AT: {MODEL_PATH}")