import re

def validate_entities(data):

    validated = {
        "Dates": [],
        "Parties": [],
        "Amounts": [],
        "TerminationClauses": []
    }

    # Date validation
    date_pattern = r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}$"

    # Money validation
    money_pattern = r"^\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?$"

    for d in data.get("Dates", []):
        if re.match(date_pattern, d.strip()):
            validated["Dates"].append(d.strip())

    for m in data.get("Amounts", []):
        if re.match(money_pattern, m.strip()):
            validated["Amounts"].append(m.strip())

    # Remove duplicates
    validated["Parties"] = list(set(data.get("Parties", [])))
    validated["TerminationClauses"] = list(set(data.get("TerminationClauses", [])))

    return validated