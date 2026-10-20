# ElderShield: Predictive Digital Twin for Stroke and Fall Prevention in Geriatric Care

Digital Twin Challenge 2026 | Prototype and Code Submission

ElderShield builds a digital twin for every elderly person. It predicts stroke risk, explains why the risk is high, simulates "what-if" changes, and alerts caregivers when live vitals drift or a fall is detected.

> ElderShield is a decision-support prototype. It is **not** a medical diagnosis tool.

---

## 1. Team Details

**Team name:** The_Glitch

| Name | Role | College |
|---|---|---|
| Deva Pandit | Team Leader | R R P G College |
| Puneet Singh | Member | Noida Institute of Engineering and Technology |

## 2. College / Incubator Information

- Deva Pandit: R R P G College
- Puneet Singh: Noida Institute of Engineering and Technology (NIET)

## 3. Project Title

**ElderShield: Predictive Digital Twin for Stroke and Fall Prevention in Geriatric Care**

## 4. Problem Statement

Elderly people are at high risk of stroke and falls, but help often arrives too late:

- Stroke risk builds quietly through age, blood pressure and lifestyle, and nobody tracks it day to day.
- An elder living alone may lie on the floor for a long time before anyone knows about a fall.
- Families and caregivers usually see only snapshots (check-up numbers), not the trend in between.

## 5. Healthcare Use Case

ElderShield gives each elder a **digital twin**: a virtual profile that is updated from health data and live vitals.

1. **Predict:** stroke risk score with Low, Medium and High bands.
2. **Explain:** SHAP shows the top reasons behind a patient's risk (for example age, hypertension, smoking).
3. **What-if:** shows how the risk score changes if hypertension is controlled or the person quits smoking (model-based estimate).
4. **Monitor:** live vitals (heart rate, systolic BP, SpO2) are tracked against baseline. Status moves from STABLE to WARNING to ALERT.
5. **Alert:** a caregiver alert card is raised on ALERT status or a fall event.

Intended users: family caregivers, home-care nurses and geriatric clinics.

## 6. Technical Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Data and ML | pandas, NumPy, scikit-learn, XGBoost |
| Explainability | SHAP |
| Backend API | FastAPI, Uvicorn, Pydantic |
| Frontend | HTML, CSS, JavaScript (canvas charts) |
| Model storage | joblib |
| Planned hardware | ESP32, MPU6050, MAX30102 |

## 7. AI/ML Model or Framework Details

- **Dataset:** Kaggle "Stroke Prediction Dataset" (fedesoriano), 5,110 rows. After cleaning: 5,109 patients (one "Other" gender row removed, missing BMI filled with median). Only about 4.9% are stroke cases (249).
- **Model:** XGBoost classifier (`n_estimators=300`, `max_depth=3`, `learning_rate=0.05`).
- **Class imbalance:** handled with `scale_pos_weight`.
- **Monotonic constraints:** the model is forced to follow medical common sense. Higher age, hypertension, heart disease or glucose, and smoking, can never lower the risk; "never smoked" can never raise it.
- **Explainability:** SHAP `TreeExplainer` gives per-patient reasons (top 3 shown in the API and dashboard).
- **What-if simulator:** re-scores the same patient with changed inputs (hypertension controlled, smoking stopped).
- **Risk bands:** score below 0.3 = LOW, 0.3 to 0.7 = MEDIUM, 0.7 and above = HIGH. The score is a risk score, not a calibrated probability.

### Results (held-out test set: 1,022 patients, 50 stroke cases)

| Metric | Value |
|---|---|
| AUROC | 0.817 |
| PR-AUC | 0.22 (random baseline is about 0.049) |
| Recall at threshold 0.3 | 0.80 (precision 0.105) |
| Recall at threshold 0.5 | 0.72 (precision 0.135) |
| Recall at threshold 0.7 | 0.50 (precision 0.184) |

Accuracy is not reported because the data is highly imbalanced. The test set has only 50 stroke cases, so numbers may shift slightly.

## 8. Demo Video

**15-20 minute demo (Unlisted YouTube):** `PASTE_YOUR_YOUTUBE_LINK_HERE`

## 9. Open-Source License

Released under the **MIT License**. See the [LICENSE](LICENSE) file.

## 10. Architecture Diagram

See [docs/ElderShield_Architecture.pdf](docs/ElderShield_Architecture.pdf).

Flow: **Data** (Kaggle stroke dataset, simulated vitals) -> **AI engine** (XGBoost + SHAP) -> **FastAPI** (`/predict`, `/whatif`, `/live`, `/fall`) -> **Dashboard** (risk card, live graph, what-if table) -> **Caregiver alert**.

## 11. Presentation

See [docs/ElderShield_TheGlitch.pptx](docs/ElderShield_TheGlitch.pptx) (project details and outcomes).

## 12. Public Accessibility

This repository is public. The demo video is an Unlisted YouTube link that opens without login. All documents are included in the `docs/` folder.

---

## Repository Structure

```
ElderShield/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── src/
│   ├── explore.py          # look at the raw data
│   ├── clean.py            # clean data, write data/clean_stroke.csv
│   ├── train_stroke.py     # train XGBoost, save models/stroke_xgb.pkl
│   ├── explain_stroke.py   # SHAP plots
│   ├── risk_engine.py      # predict_risk(): score, band, top reasons
│   ├── what_if.py          # what-if scenarios (command line)
│   └── api.py              # FastAPI backend
├── dashboard/
│   ├── index.html          # risk card, SHAP reasons, what-if
│   └── live.html           # live vitals, alerts, simulated fall
├── models/
│   └── stroke_xgb.pkl      # trained model
└── docs/
    ├── ElderShield_TheGlitch.pptx
    └── ElderShield_Architecture.pdf
```

## How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
2. **Get the dataset.** Download the Kaggle "Stroke Prediction Dataset" (fedesoriano) and save it as `data/healthcare-dataset-stroke-data.csv`. The dataset is not included in this repository.
3. **Prepare data and train** (from the project folder)
   ```bash
   python src/clean.py
   python src/train_stroke.py
   python src/explain_stroke.py
   ```
   A trained `models/stroke_xgb.pkl` is already included, so you can skip this step and go straight to step 4.
4. **Start the API**
   ```bash
   cd src
   python -m uvicorn api:app --reload
   ```
   Open http://127.0.0.1:8000/docs to try the endpoints.
5. **Open the dashboard.** Double-click `dashboard/index.html` for the risk card, and `dashboard/live.html` for live monitoring. Use "Reset simulation" before a demo, and "Simulate fall" to raise a fall alert.

## API Endpoints

| Endpoint | Purpose |
|---|---|
| `POST /predict` | Risk score, band and top 3 SHAP reasons |
| `POST /whatif` | Current risk plus what-if scenarios |
| `GET /live` | One tick of the simulated patient stream |
| `POST /live/reset` | Restart the simulation |
| `POST /fall` | Raise a simulated fall event |
| `GET /events` | Latest caregiver alerts |
| `POST /events/clear` | Clear alerts |

## Limitations and Honest Notes

- ElderShield is decision support, not a diagnosis.
- The stroke model is trained on a public dataset with only 249 stroke cases. It has not been validated on Indian elderly populations or by clinicians.
- **Live vitals and the fall alert are simulated** (no hardware connected yet). Alert thresholds are simple demo rules, not clinical rules.
- What-if results are model-based estimates and do not prove cause and effect.
- The risk score is not a calibrated probability.

## Future Work

- Real fall detection model (1D-CNN) trained on SisFall or MobiAct accelerometer data.
- Wearable integration: ESP32 with MPU6050 and MAX30102.
- SMS and WhatsApp caregiver alerts.
- Privacy by design: consent, encryption, and compliance with India's DPDP Act 2023.
- Probability calibration and clinical validation.

## Team

**The_Glitch:** Deva Pandit (Team Leader, R R P G College) and Puneet Singh (Noida Institute of Engineering and Technology).
