📄 README.md
markdown
 
# Text Classification API (FastAPI + Machine Learning)

A simple API that classifies words as **"good"**, **"bad"**, or **"unknown"** based on a trained machine learning model.

---

## 📁 Project Structure

src/main/java/tn/esprit/microservice/test_ml/ml_server/ ├── pycache/ ├── api_server.py # (Optional extra server script if needed) ├── app.py # Main FastAPI server ├── train_model.py # Script to train the ML model ├── model.pkl # Trained logistic regression model ├── vectorizer.pkl # Trained vectorizer

r
 

---

## 🛠 Installation

1. Open a terminal.
2. Navigate to your project directory:

```bash
cd Desktop\jobs\javafx\test_ml\src\main\java\tn\esprit\microservice\test_ml\ml_server
Install the required Python packages:

bash
 
pip install fastapi uvicorn scikit-learn joblib
⚙️ Training the Machine Learning Model
To retrain or train the model if needed:

bash
 
python train_model.py
This will generate (or update) the files:

model.pkl

vectorizer.pkl

🚀 Running the API Server
Start the FastAPI server by running:

bash
 
uvicorn app:app --reload --port 8000
Access the API documentation at:
👉 http://127.0.0.1:8000/docs

📬 API Usage
➔ Endpoint
POST /predict/

➔ Request Body (JSON)
json
 
{
  "word": "yourword"
}
➔ Example Request
bash
 
curl -X POST "http://127.0.0.1:8000/predict/" ^
  -H "Content-Type: application/json" ^
  -d "{\"word\":\"fucking\"}"
➔ Example Response
json
 
{
  "result": "bad"
}
🧠 Notes
Expand train_model.py with more examples for better accuracy!

Currently the model predicts based only on single words.

This is a simple educational project and might not catch all "bad" words.

Unknown words (words the model wasn't trained on) will return "unknown".

✨ Bonus
Later, you can upgrade this API to:

Predict full sentences ("You're awesome" → good / "You're a stupid idiot" → bad).

Or add a small web page (HTML+JavaScript) to use it easily.

📢 Important Commands Summary

Command	Action
cd Desktop\jobs\javafx\test_ml\src\main\java\tn\esprit\microservice\test_ml\ml_server	Go to project
pip install fastapi uvicorn scikit-learn joblib	Install packages
python train_model.py	Train the model
uvicorn app:app --reload --port 8000	Run the FastAPI server
yaml
 

---

# 📢 Quick explanation:
- `train_model.py` → training.
- `app.py` → serving (FastAPI server).
- `model.pkl` and `vectorizer.pkl` → saved model files.
- Everything ready for calling `/predict/`.

 




