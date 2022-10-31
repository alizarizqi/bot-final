import re


def detect(text):
    regex = r"(?!\w.\w.)(?![A-Z][a-z]\.)(?<=\.|\?)\s"
    matches = re.split(regex, text)
    return matches[0]
