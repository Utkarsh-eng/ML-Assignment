
from flask import Flask, request, jsonify
import re
import pickle
import numpy as np
from scipy.sparse import hstack, csr_matrix

tfidf = pickle.load(open("tfidf.pkl", "rb"))
best_model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

def predict(sample):
    code = sample.get("code", "")
    cwe = sample.get("cwe_id", "")
  
    code = str(code).lower()
    code = re.sub(r'//.*|/\*.*?\*/|#.*', '', code)
    code = re.sub(r'\s+', ' ', code).strip()
    
    numbers = re.findall(r'\d+', str(cwe))
    if len(numbers) > 0:
        cwe_clean = int(numbers[0])
    else:
        cwe_clean = 0
    
    code_vec = tfidf.transform([code])
    
    cwe_array = csr_matrix([[cwe_clean]])
    X = hstack([code_vec, cwe_array])   
  
    prob = best_model.predict_proba(X)[0][1]
    
    threshold = 0.3
    label = 1 if prob > threshold else 0
    
    return float(prob), int(label)

@app.route("/")
def home():
    return "API is running "

@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.get_json()
    
    prob, label = predict(data)
    
    return jsonify({
        "probability": prob,
        "label": label
    })

if __name__ == "__main__":
    app.run(debug=True)