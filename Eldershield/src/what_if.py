from risk_engine import predict_risk

patient = {"age": 72, "hypertension": 1, "heart_disease": 0,
           "avg_glucose_level": 110, "bmi": 31, "gender": "Male",
           "residence": "Urban", "work_type": "Private",
           "smoking": "smokes"}

scenarios = {
    "Hypertension control ho jaye": {"hypertension": 0},
    "Smoking chhod de": {"smoking": "never smoked"},
    "BMI 31 se 25 ho jaye": {"bmi": 25},
    "Teeno improvement saath": {"hypertension": 0,
                                "smoking": "never smoked", "bmi": 25},
}

base = predict_risk(patient)
print(f"CURRENT: score={base['score']}, band={base['band']}\n")

for name, change in scenarios.items():
    new_p = {**patient, **change}
    r = predict_risk(new_p)
    diff = r["score"] - base["score"]
    print(f"{name}:")
    print(f"   score={r['score']}, band={r['band']}, change={diff:+.3f}")