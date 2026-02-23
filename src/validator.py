import re

def validate_entities(data):

    validated = {
        "Dates": [],
        "Parties": [],
        "Amounts": [],
        "TerminationClauses": []
    }

    # Validate DATE (simple format check)
    for date in data.get("Dates", []):
        if re.search(r"\d{4}", date):
            validated["Dates"].append(date)

    # Validate MONEY (must contain $)
    for amount in data.get("Amounts", []):
        if "$" in amount:
            validated["Amounts"].append(amount)

    # Parties (basic check)
    for party in data.get("Parties", []):
        if len(party) > 2:
            validated["Parties"].append(party)

    # Termination words
    for term in data.get("TerminationClauses", []):
        validated["TerminationClauses"].append(term)

    return validated