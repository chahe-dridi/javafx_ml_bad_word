from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Create FastAPI app
app = FastAPI()

# Load your trained model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

class WordRequest(BaseModel):
    word: str

@app.post("/predict/")
def predict_word(request: WordRequest):
    word = request.word.lower().strip()  # clean
    if word not in vectorizer.vocabulary_:
        return {"result": "unknown"}  # or guess bad if you want

    X = vectorizer.transform([word])
    prediction = model.predict(X)
    return {"result": "bad" if prediction[0] == 1 else "good"}
