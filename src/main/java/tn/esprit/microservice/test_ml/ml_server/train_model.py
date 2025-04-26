from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

texts = [
    # Bad
    "bad", "ugly", "stupid", "hate", "fucking", "slut", "idiot", "bastard", "dumb", "trash",
    "moron", "jerk", "loser", "scumbag", "douchebag", "asshole", "ignorant", "rude",
    # Good
    "good", "beautiful", "smart", "love", "awesome", "great", "amazing", "kind", "friendly", "nice",
    "fantastic", "brilliant", "genius", "polite", "respectful", "charming", "pleasant", "wonderful"
]
labels = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
]

vectorizer = CountVectorizer(ngram_range=(1,2))
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("✅ Model and vectorizer saved successfully!")
