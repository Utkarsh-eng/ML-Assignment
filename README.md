# 🔍 Vulnerability Detection in Code using Machine Learning

## 📌 Overview

This project focuses on identifying whether a given code snippet represents a **real vulnerability** or a **false positive** using machine learning.

The main idea was to build a practical system where the model prioritizes **detecting real vulnerabilities**, even if it means allowing some false alarms.

---

## ⚙️ Approach

### 🧹 Data Preprocessing

* Cleaned code snippets by removing comments and extra spaces using regular expressions
* Created a separate `clean_code` column to preserve original data
* Extracted numeric values from CWE identifiers (e.g., `CWE-79 → 79`)

---

### 🔢 Feature Engineering

* Used **TF-IDF vectorization** to convert code into numerical features
* Limited features to top 5000 tokens for efficiency
* Combined TF-IDF features with the processed CWE feature

---

### 🤖 Models Used

* Logistic Regression (baseline)
* Random Forest (ensemble method)
* XGBoost (final model)

---

## 📊 Evaluation Strategy

Accuracy was not used as the primary metric because:

> In security, missing a real vulnerability is much more critical than raising a false alarm.

So, the focus was on:

* **Recall (primary metric)**
* Precision and F1-score (secondary metrics)

XGBoost achieved the best recall and was selected as the final model.

---

## 🎯 Threshold Tuning

* Default threshold (0.5) was reduced to **0.3**
* This improved recall and helped detect more real vulnerabilities

---

## 🧪 Example Output

```text
Probability: 0.87  
Prediction: Real Vulnerability
```

---

## 🛠️ Tech Stack

* Python
* scikit-learn
* XGBoost
* Pandas, NumPy, SciPy

---

## 📁 Project Structure

```
├── notebook.ipynb       # Model development
├── app.py               # Flask API (optional)
├── tfidf.pkl            # Saved TF-IDF vectorizer
├── model.pkl            # Trained model
└── README.md
```

---

## 🚀 Key Learnings

* Choosing the right metric is more important than accuracy
* TF-IDF works surprisingly well for code-based problems
* Threshold tuning significantly impacts model performance

---

## 🔮 Future Improvements

* Use transformer-based models for code understanding
* Add more contextual features (file structure, dependencies)
* Perform hyperparameter tuning

---

## 👤 Author

**Utkarsh Kumar Yadav**

