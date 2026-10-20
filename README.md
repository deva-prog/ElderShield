# 🛡️ ElderShield — Predictive Digital Twin for Elderly Care

**Team:** The_Glitch  
**Project Domain:** AI | Healthcare | Data Science | Digital Health

ElderShield is an AI-powered healthcare decision-support system designed to help caregivers monitor elderly individuals by predicting stroke risk, explaining the factors behind predictions, exploring what-if scenarios, and generating alerts for simulated abnormal vital signs and fall events.

## 🎥 Demo Video

▶️ **Watch the Project Demo:** https://youtu.be/53F9bdwPkBk?si=vQytbcwNVvaz4ffH

> Replace `YOUR_DEMO_VIDEO_URL` with your actual demo video URL from YouTube, Google Drive, or another video hosting platform.

## 🚨 Problem Statement

Elderly individuals may face serious health risks that go unnoticed between medical check-ups.

- **Unnoticed stroke risk:** Age and hypertension can contribute to stroke risk over time.
- **Undetected falls:** Elderly individuals living alone may not receive immediate assistance after a fall.
- **Limited continuous monitoring:** Caregivers often have access to periodic health snapshots rather than ongoing trends.

ElderShield aims to address these challenges through predictive analytics, explainable AI, and caregiver alerts.

## 💡 Our Solution

ElderShield creates a digital-twin-inspired risk monitoring experience with four core capabilities:

- **Predict:** Estimate stroke risk and classify it into Low, Medium, or High bands.
- **Explain:** Use SHAP to identify important factors influencing a patient's prediction.
- **What-if Analysis:** Recalculate estimated risk when selected inputs, such as smoking or hypertension, are changed.
- **Monitor:** Display simulated vital signs and generate alerts for warning conditions and fall events.

**Important:** ElderShield is a decision-support prototype, not a medical diagnostic system. Its predictions are model-based estimates and require clinical validation.

## ⚙️ How It Works

1. **Data Input:** Uses a Kaggle stroke dataset and simulated vital-sign data.
2. **AI Engine:** An XGBoost model estimates stroke risk.
3. **Explainable AI:** SHAP provides patient-specific explanations.
4. **Backend API:** FastAPI exposes prediction, what-if, live monitoring, and fall-event endpoints.
5. **Dashboard:** An HTML/JavaScript interface displays risk scores, live charts, and what-if comparisons.
6. **Caregiver Alerts:** Alert cards are generated when monitoring conditions or simulated fall events trigger them.

The prototype runs locally, allowing the demonstration without an internet connection.

## 🧠 AI & Machine Learning

- XGBoost for stroke-risk prediction.
- Class-imbalance weighting to address the unequal distribution of stroke and non-stroke cases.
- Monotonic constraints to encourage medically sensible relationships between selected risk factors and predictions.
- SHAP for explainable, patient-level predictions.
- What-if analysis for comparing model scores under changed inputs.
- Low, Medium, and High risk categories for easier interpretation.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas |
| Machine Learning | XGBoost, Scikit-learn |
| Explainable AI | SHAP |
| Backend | FastAPI, Uvicorn |
| Frontend | HTML, JavaScript |
| Visualization | Live charts |
| Dataset | Kaggle Stroke Dataset |
| Monitoring | Simulated vital-sign stream |

The presentation identifies a dataset containing **5,109 patient records**. Integration with ESP32-based wearable monitoring is planned for future development.

## 📊 Model Performance

The following results are reported in the project presentation for held-out test data.

| Metric | Result |
|---|---:|
| AUROC | 0.817 |
| PR-AUC | 0.22 |
| Recall at threshold 0.3 | 0.80 |
| Test set size | 1,022 patients |
| Stroke cases in test set | 50 |

The reported recall means the model identified 40 out of 50 stroke cases at the specified threshold.

Because the dataset is imbalanced, recall and PR-AUC are emphasized instead of accuracy alone. Lowering the decision threshold may help detect more stroke cases, but it can also increase false alarms.

*These are reported prototype evaluation results, not evidence of clinical effectiveness.*

## 🔍 Explainable AI & What-if Analysis

For an example patient, the presentation demonstrates a risk score of **0.76 (High Risk)**, with age, hypertension, and smoking among the factors influencing the prediction.

Example what-if changes reported in the presentation:

- Controlling hypertension: risk score change of approximately -0.049.
- Quitting smoking: risk score change of approximately -0.055.

These values represent model-based estimates. They do not establish that changing a single factor will cause a specific reduction in an individual's real-world stroke risk.

## 🚨 Live Monitoring & Fall Alerts

The monitoring demonstration includes:

- Blood pressure, heart rate, and SpO₂ monitoring using simulated values.
- Vital-sign updates every two seconds.
- STABLE, WARNING, and ALERT states.
- A simulated fall event that generates a caregiver alert card with the person's name and time.

**Note:** Vital-sign streaming and fall alerts are simulated in the current prototype. A validated real-world fall-detection model and wearable integration are future enhancements.

## ⚠️ Limitations

- ElderShield is not a substitute for medical advice, diagnosis, or treatment.
- The dataset contains only 249 stroke cases, limiting the available positive examples.
- Validation and calibration for elderly populations in India are still required.
- Vital-sign monitoring and fall-event generation are simulated.
- What-if predictions are model estimates, not causal or guaranteed outcomes.
- Clinical review and real-world testing are necessary before practical deployment.

## 🚀 Future Enhancements

- Integrate a real fall-detection model using the SisFall dataset and a 1D-CNN.
- Explore wearable integration using ESP32, MPU6050, and MAX30102 sensors.
- Add SMS and WhatsApp caregiver notifications.
- Improve model validation and calibration with clinical experts.
- Implement consent-based data collection and privacy safeguards aligned with India's Digital Personal Data Protection Act, 2023.

## 👥 Team The_Glitch

**Deva Pandit — Team Leader**  
R R P G College

**Puneet Singh — Team Member**  
Noida Institute of Engineering and Technology

## 🎯 Project Goal

Our goal is to explore how predictive AI, explainability, and continuous monitoring can support earlier awareness of health risks and improve communication between elderly individuals and their caregivers.

**ElderShield — Predict the risk. Explain the why. Support timely care.**

---

*Developed as an AI and healthcare prototype by Team The_Glitch.*
