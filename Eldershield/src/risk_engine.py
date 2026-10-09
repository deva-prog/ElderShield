import os
import joblib
import pandas as pd
import shap

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bundle = joblib.load(os.path.join(BASE, "models", "stroke_xgb.pkl"))
model = bundle["model"]
columns = bundle["columns"]
explainer = shap.TreeExplainer(model)


def get_band(score):
    if score >= 0.7:
        return "HIGH"
    if score >= 0.3:
        return "MEDIUM"
    return "LOW"


def predict_risk(p):
    row = {c: 0 for c in columns}
    row["age"] = p["age"]
    row["hypertension"] = p["hypertension"]
    row["heart_disease"] = p["heart_disease"]
    row["avg_glucose_level"] = p["avg_glucose_level"]
    row["bmi"] = p["bmi"]
    row["gender_Male"] = int(p["gender"] == "Male")
    row["ever_married_Yes"] = int(p.get("married", True))
    row["Residence_type_Urban"] = int(p["residence"] == "Urban")

    work_col = f"work_type_{p['work_type']}"
    if work_col in row:
        row[work_col] = 1
    smoke_col = f"smoking_status_{p['smoking']}"
    if smoke_col in row:
        row[smoke_col] = 1

    X = pd.DataFrame([row], columns=columns)
    score = float(model.predict_proba(X)[0, 1])

    sv = explainer(X)
    pairs = sorted(zip(columns, sv[0].values), key=lambda x: -abs(x[1]))[:3]
    reasons = [
        {"feature": n, "impact": round(float(v), 2),
         "effect": "badhaya" if v > 0 else "ghataya"}
        for n, v in pairs
    ]
    return {"score": round(score, 3), "band": get_band(score), "reasons": reasons}


if __name__ == "__main__":
    patient_a = {"age": 80, "hypertension": 1, "heart_disease": 0,
                 "avg_glucose_level": 120, "bmi": 22, "gender": "Female",
                 "residence": "Rural", "work_type": "Private",
                 "smoking": "never smoked"}

    patient_b = {"age": 35, "hypertension": 0, "heart_disease": 0,
                 "avg_glucose_level": 90, "bmi": 24, "gender": "Male",
                 "residence": "Urban", "work_type": "Private",
                 "smoking": "never smoked"}

    print("Patient A (80 saal):", predict_risk(patient_a))
    print("Patient B (35 saal):", predict_risk(patient_b))