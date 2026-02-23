import re

def find_entities(text):
    entities = []

    patterns = {
        "DATE": r"(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}",
        "PARTY": r"(Alpha Corp|Beta Solutions|Global Finance Ltd)",
        "MONEY": r"\$\d{1,3}(?:,\d{3})*(?:\.\d+)?",
        "TERMINATION": r"\b(terminated|termination)\b"
    }

    for label, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            entities.append((match.start(), match.end(), label))

    return entities