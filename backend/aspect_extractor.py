import spacy

nlp = spacy.load("en_core_web_sm")

def extract_aspects(text):
    doc = nlp(text)
    aspects = []

    for chunk in doc.noun_chunks:
        aspects.append(chunk.text.lower())

    return list(set(aspects))