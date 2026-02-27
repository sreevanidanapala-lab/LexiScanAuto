import re
from datetime import datetime

def validate_output(data):

    clean = {
        "dates": [],
        "parties": data["parties"],
        "amounts": [],
        "termination_clauses": data["termination_clauses"]
    }

    # Date Validation
    for date in data["dates"]:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            clean["dates"].append(date)
        except:
            pass

    # Amount Validation
    for amt in data["amounts"]:
        if re.search(r"\$", amt):
            clean["amounts"].append(amt)

    return clean