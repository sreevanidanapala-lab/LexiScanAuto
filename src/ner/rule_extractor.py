import re


# -----------------------------
# PARTY EXTRACTION
# -----------------------------
def extract_parties(text: str):
    """
    Extract company/party names from contract text.
    Looks for:
    - Companies mentioned after 'between'
    - Capitalized organization names
    """

    parties = set()

    # 1️⃣ Extract from "between X and Y"
    between_pattern = re.search(
        r'between\s+(.*?)\s+and\s+(.*?)[\.,\n]',
        text,
        re.IGNORECASE
    )

    if between_pattern:
        party1 = between_pattern.group(1).strip()
        party2 = between_pattern.group(2).strip()
        parties.add(party1)
        parties.add(party2)

    # 2️⃣ Extract company-style names (Ltd, Pvt Ltd, Corp, Solutions etc.)
    company_pattern = re.findall(
        r'\b[A-Z][A-Za-z&,\s]+(?:Pvt Ltd|Private Limited|Ltd|Limited|Corporation|Corp|Solutions|Technologies)\b',
        text
    )

    for match in company_pattern:
        parties.add(match.strip())

    return list(parties)


# -----------------------------
# TERMINATION CLAUSE EXTRACTION
# -----------------------------
def extract_termination_clauses(text: str):
    """
    Extract termination-related clauses.
    Looks for sentences containing keywords like:
    terminate, termination, breach, written notice
    """

    termination_clauses = []

    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    keywords = [
        "terminate",
        "termination",
        "written notice",
        "breach",
        "end this agreement"
    ]

    for sentence in sentences:
        if any(keyword in sentence.lower() for keyword in keywords):
            termination_clauses.append(sentence.strip())

    return termination_clauses