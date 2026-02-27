import spacy
from spacy.training.example import Example
from pathlib import Path

MODEL_PATH = Path("ner_model")

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")

labels = ["DATE", "PARTY", "AMOUNT", "TERMINATION_CLAUSE"]
for label in labels:
    ner.add_label(label)

training_data = [
    ("ABC Bank signed agreement on 2024-01-01 for $1,250,000.",
     {"entities": [(0, 8, "PARTY"),
                   (28, 38, "DATE"),
                   (43, 53, "AMOUNT")]})
]

optimizer = nlp.initialize()

for i in range(20):
    losses = {}
    for text, annotations in training_data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], losses=losses)
    print(f"Iteration {i+1} Loss: {losses}")

nlp.to_disk(MODEL_PATH)
print("✅ NER Model Trained Successfully")