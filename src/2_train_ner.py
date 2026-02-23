import spacy
import json
from pathlib import Path
from spacy.training import Example

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent

DATA_PATH = PROJECT_ROOT / "data" / "processed" / "ner_training_data.json"
MODEL_PATH = PROJECT_ROOT / "week2_model"

if not DATA_PATH.exists():
    raise FileNotFoundError("❌ Training data missing!")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# -------------------------
# CLEAN DATA FOR SPACY
# -------------------------
training_data = []

for item in raw_data:
    text = item["text"]
    entities = item["entities"]

    # If wrongly nested like {"entities": [...]}
    if isinstance(entities, dict):
        entities = entities.get("entities", [])

    clean_entities = []

    for ent in entities:
        if len(ent) == 3:
            start = int(ent[0])
            end = int(ent[1])
            label = str(ent[2])
            clean_entities.append((start, end, label))

    training_data.append((text, {"entities": clean_entities}))

# -------------------------
# CREATE MODEL
# -------------------------
nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")

# Add labels
for text, annotations in training_data:
    for start, end, label in annotations["entities"]:
        ner.add_label(label)

nlp.initialize()
optimizer = nlp.begin_training()

# -------------------------
# TRAINING LOOP
# -------------------------
for epoch in range(15):
    losses = {}

    for text, annotations in training_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], sgd=optimizer, losses=losses)

    print(f"Epoch {epoch+1} Loss: {losses}")

# -------------------------
# SAVE MODEL
# -------------------------
nlp.to_disk(MODEL_PATH)

print("\n✅ MODEL TRAINED SUCCESSFULLY")
print("📁 Saved at:", MODEL_PATH)