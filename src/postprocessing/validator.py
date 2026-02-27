import re


def validate_entities(data: dict):

    # Validate dates (YYYY-MM-DD)
    valid_dates = []
    for d in data["dates"]:
        if re.match(r"\d{4}-\d{2}-\d{2}", d):
            valid_dates.append(d)

    # Validate amounts ($ symbol required)
    valid_amounts = []
    for amt in data["amounts"]:
        if amt.startswith("$"):
            valid_amounts.append(amt)

    return {
        "dates": valid_dates,
        "parties": data["parties"],
        "amounts": valid_amounts,
        "termination_clauses": data["termination_clauses"]
    }