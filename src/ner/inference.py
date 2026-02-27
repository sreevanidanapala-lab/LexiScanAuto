from ner.rule_extractor import extract_parties, extract_termination_clauses
import re


def extract_dates(text):
    return re.findall(r'\d{4}-\d{2}-\d{2}', text)


def extract_amounts(text):
    return re.findall(r'\$\s?\d+(?:,\d{3})*(?:\.\d{2})?', text)


def extract_entities(text: str):

    return {
        "dates": extract_dates(text),
        "amounts": extract_amounts(text),
        "parties": extract_parties(text),
        "termination_clauses": extract_termination_clauses(text)
    }