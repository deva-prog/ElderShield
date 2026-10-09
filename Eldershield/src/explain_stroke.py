import os
import joblib
import pandas as pd
import shap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data", "clean_stroke.csv")
MODEL = os.path.join(BASE, "models", "stroke_xgb.pkl")
OUT = os.path.join(BASE, "models")

model = joblib.load(MODEL)["model"]

df = pd.read_csv(DATA)
X = df.drop(columns=["stroke"])
y = df["stroke"]

# Wahi split jo training mein tha
Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

explainer = shap.TreeExplainer(model)
sv = explainer(Xte)

# 1. Global: kaun se features sabse zyada matter karte hain
plt.figure()
shap.plots.beeswarm(sv, show=False)
plt.tight_layout()
plt.savefig(os.path.join(OUT, "shap_summary.png"), dpi=150, bbox_inches="tight")
plt.close()

# 2. Ek patient: sabse zyada risk wala patient
probs = model.predict_proba(Xte)[:, 1]
idx = int(probs.argmax())
print("Sabse high-risk patient ka risk score:", round(float(probs[idx]), 3))
print("Patient ki details:")
print(Xte.iloc[idx].to_string())

plt.figure()
shap.plots.waterfall(sv[idx], show=False)
plt.tight_layout()
plt.savefig(os.path.join(OUT, "shap_patient.png"), dpi=150, bbox_inches="tight")
plt.close()

print("\nTop 5 reasons (is patient ka risk kyun zyada):")
pairs = sorted(zip(X.columns, sv[idx].values), key=lambda x: -abs(x[1]))[:5]
for name, val in pairs:
    direction = "risk badhaya" if val > 0 else "risk ghataya"
    print(f"  {name}: {val:+.2f} ({direction})")

print("\nSaved: models/shap_summary.png aur models/shap_patient.png")