import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import (roc_auc_score, average_precision_score,
                             recall_score, precision_score)
from xgboost import XGBClassifier

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data", "clean_stroke.csv")
MODEL_DIR = os.path.join(BASE, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

df = pd.read_csv(DATA)
X = df.drop(columns=["stroke"])
y = df["stroke"]

Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Imbalance handle: stroke wale cases ko zyada weight
weight = (ytr == 0).sum() / (ytr == 1).sum()

model = XGBClassifier(
    n_estimators=300,
    max_depth=3,
    learning_rate=0.05,
    scale_pos_weight=weight,
    eval_metric="aucpr",
    random_state=42,
    monotone_constraints={
        "age": 1,
        "hypertension": 1,
        "heart_disease": 1,
        "avg_glucose_level": 1,
        "smoking_status_smokes": 1,
        "smoking_status_never smoked": -1,
    },
)
model.fit(Xtr, ytr)

p = model.predict_proba(Xte)[:, 1]

print("Test set size:", len(yte), "| Stroke cases:", int(yte.sum()))
print("AUROC  :", round(roc_auc_score(yte, p), 3))
print("PR-AUC :", round(average_precision_score(yte, p), 3))

for t in [0.3, 0.5, 0.7]:
    pred = (p > t).astype(int)
    print(f"Threshold {t}: Recall={recall_score(yte, pred):.3f}, "
          f"Precision={precision_score(yte, pred, zero_division=0):.3f}")

joblib.dump({"model": model, "columns": list(X.columns)},
            os.path.join(MODEL_DIR, "stroke_xgb.pkl"))
print("Model saved in models/stroke_xgb.pkl")