from fastapi import FastAPI
from pydantic import BaseModel
import spacy
from model import get_sentiment
from aspect_extractor import extract_aspects

# ✅ app must be defined BEFORE decorators
app = FastAPI()

# Load spaCy once
nlp = spacy.load("en_core_web_sm")

class Review(BaseModel):
    text: str


@app.post("/analyze")
def analyze_review(review: Review):
    doc = nlp(review.text)
    results = []

    for sent in doc.sents:
        sentence = sent.text.strip()

        aspects = extract_aspects(sentence)

        if aspects:
            sentiment = get_sentiment(sentence)

            for aspect in aspects:
                results.append({
                    "aspect": aspect,
                    "sentence": sentence,
                    "sentiment": sentiment
                })

    return {"results": results}