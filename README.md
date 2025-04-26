📜 README.md file
Here’s a simple README you can copy:

markdown
Copy
Edit
# Text Classification API

A simple FastAPI server that classifies a word as "good" or "bad" based on a trained machine learning model.

## Setup

1. Install required Python packages:

```bash
pip install fastapi uvicorn scikit-learn joblib
Train the model:

bash
Copy
Edit
python train_model.py
This will create model.pkl and vectorizer.pkl.

Run the API server:

bash
Copy
Edit
uvicorn api_server:app --reload --port 8000
The API will be available at http://127.0.0.1:8000.

API Usage
POST /predict/

Request Body:

json
Copy
Edit
{
  "word": "yourword"
}
Response:

json
Copy
Edit
{
  "result": "good"  // or "bad"
}
Example
bash
Copy
Edit
curl -X POST "http://127.0.0.1:8000/predict/" -H "Content-Type: application/json" -d "{\"word\":\"fucking\"}"
Response:

json
Copy
Edit
{
  "result": "bad"
}
Notes
Expand train_model.py with more words for better accuracy.

This model is for educational purposes and may not detect all bad words perfectly.

yaml
Copy
Edit

---
---

Would you also like me to show you a version where you **analyze full sentences**, not just single words?  
👉 Like "You are a fucking idiot" = **bad**? (way smarter 👀)  
I can make it for you if you want! 🚀





cd Desktop\jobs\javafx\test_ml\src\main\java\tn\esprit\microservice\test_ml\ml_server
C:\Users\DARK\AppData\Local\Programs\Python\Python39\python.exe train_model.py

uvicorn api_server:app --reload --port 8000
