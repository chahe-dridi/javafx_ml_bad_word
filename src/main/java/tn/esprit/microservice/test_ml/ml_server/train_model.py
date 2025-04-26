from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Example small dataset
texts = [
    "bad", "ugly", "stupid", "hate",
    "good", "beautiful", "smart", "love"
]
labels = [1, 1, 1, 1, 0, 0, 0, 0]  # 1 = bad, 0 = good

# Vectorize words
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train a simple model
model = LogisticRegression()
model.fit(X, labels)

# Save model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model and vectorizer saved!")
