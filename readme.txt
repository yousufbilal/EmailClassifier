# **PHASES OF THE PROJECT**

## **PHASE 1 — Dataset Creation**

* Create 6–10 emails (Python list of dicts).
* Each dict has: `"text"` and `"label"`.
* Convert to pandas DataFrame.
* Print DataFrame + row count.

---

## **PHASE 2 — Text Preprocessing**

* Load DataFrame from Phase 1.
* Extract email text.
* Convert text → numerical features using TF-IDF.
* Print the feature matrix shape.

---

## **PHASE 3 — Model Training**

* Split features + labels into train/test.
* Train a classifier (Naive Bayes recommended).
* Predict on test set.
* Print accuracy + prediction results.

---

## **PHASE 4 — Prediction Tool**

* Load trained model + vectorizer.
* Accept user input (email text).
* Predict phishing or legit.
* Print the result.

---

## **PHASE 5 — (Optional) Save Model**

* Save model + vectorizer to `/model/`.
* Load them in your prediction script.

---

## **PHASE 6 — (Optional) Extensions**

* Add real phishing datasets
* Try different ML models
* Build a small Flask API
* Add a simple UI
* Add model explainability

---

