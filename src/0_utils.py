import re

def find_entities(text):
    entities = []

    patterns = {
        "DATE": r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}\b",
        "MONEY": r"\$\d{1,3}(?:,\d{3})*(?:\.\d+)?",
        "ORG": r"\b[A-Z][a-zA-Z]+(?:\s[A-Z][a-zA-Z]+)*\b",
        "TERMINATION_CLAUSE": r"(terminated|termination|terminate).*?\."
    }

    for label, pattern in patterns.items():
        for match in re.finditer(pattern, text, re.IGNORECASE):
            entities.append({
                "start": match.start(),
                "end": match.end(),
                "label": label,
                "text": match.group()
            })

    return entities