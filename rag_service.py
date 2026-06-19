from pathlib import Path

def retrieve_context(question: str):
    text = Path("knowledge.txt").read_text()
    return text

