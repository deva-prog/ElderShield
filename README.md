# ElderShield: Predictive Digital Twin for Stroke and Fall Prevention in Geriatric Care

## 👥 Team Details & Institutional Information
* **Team Name:** The_Glitch
* **Team Members:** 
  * Deva Pandit (Team Leader)
  * Puneet Singh (Member)

---

## 📌 Problem Statement & Healthcare Use Case
Elderly individuals living alone often face critical health risks that go unnoticed until it is too late. Baseline health factors like age and hypertension build stroke risks quietly without daily monitoring, while accidental falls left undetected can lead to prolonged, life-threatening delays in emergency care.

**ElderShield** establishes a personalized **Digital Twin** (virtual patient model) for each elder. It successfully demonstrates multi-stream data fusion by ingesting historical clinical records alongside simulated real-time wearable telemetry to offer predictive risk stratification and immediate caregiver alert management.

---

## 🛠️ Technical Stack & AI/ML Architecture
* **Data Sources:** Kaggle Stroke Dataset (**5,109 patients** used for static baseline training) fused with simulated time-series vital streams (Heart Rate, SpO2, and Systolic Blood Pressure updating every 2 seconds).
* **AI/ML Engine:** **XGBoost Classifier** optimized with class-imbalance weighting and monotonic medical constraints.
* **Explainability:** **SHAP** (Shapley Additive exPlanations) for personalized feature attribution and dynamic What-if clinical scenario testing.
* **Backend Framework:** **FastAPI & Uvicorn REST API** featuring lightweight local endpoints (`/predict`, `/whatif`, `/live`).
* **Frontend Dashboard:** Responsive **HTML5, CSS3, and JavaScript** with interactive real-time vital tracking charts.

---

## 📈 Model Performance & Validation
Evaluated on a held-out test set of 1,022 patients (including 50 stroke cases), the predictive engine demonstrates exceptional clinical utility:
* **AUROC:** **0.817** (Highly capable of separating high-risk and low-risk individuals)
* **PR-AUC:** **0.22** (4.5x better than a random baseline predictor of 0.049)
* **Recall:** **0.80** (Successfully catches 40 out of 50 actual stroke cases at a risk threshold of 0.340)

---

## 📂 Repository Directory Structure
Following a professional, modular development pattern, the project files are organized as follows:
```text
Eldershield/
├── dashboard/                  # Frontend UI Assets
│   ├── index.html              # Static risk predictor & What-If panel
│   └── live.html               # Real-time health monitoring stream
├── data/                       # Clinical & Anonymized Datasets
│   ├── clean_stroke.csv        # Processed feature set
│   └── healthcare-dataset-stroke-data.csv # Raw Kaggle dataset
├── models/                     # Serialized AI model artifacts
├── src/                        # Core Python Application Source
│   ├── api.py                  # FastAPI REST routes and server configuration
│   ├── clean.py                # Data cleaning pipeline
│   ├── explain_stroke.py       # SHAP explanation calculations
│   ├── explore.py              # Exploratory data analysis scripts
│   ├── risk_engine.py          # Logic for combining static history and live telemetry
│   ├── train_stroke.py         # XGBoost model training and evaluation code
│   └── what_if.py              # Hypothetical treatment adjustment scoring
├── architecture_diagram.pdf   # Complete pipeline design blueprint
├── presentation.pdf           # Project showcase and evaluation deck
├── requirements.txt           # Required Python packages
└── README.md                  # Project homepage documentation
```

---

## 🚀 Installation & How to Run Locally

### 1. Prerequisites
Ensure you have **Python 3.9+** installed on your system.

### 2. Clone the Repository
```bash
git clone [Paste your public GitHub repository link here]
cd Eldershield
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Application Server
Run the FastAPI backend server using PyCharm terminal or your command prompt:
```bash
uvicorn src.api:app --reload
```
Once started, open your web browser and navigate to `http://127.0.0.1:8000` to interact with the **ElderShield Dashboard**.

---

## 🎥 Prototype Demonstration Video
[![ElderShield Prototype Demo](https://shields.io)]([Insert your unlisted YouTube video link here])
*Note: This link hosts our comprehensive video demonstrating the backend API lifecycle, ML validation script walkthrough, and live dashboard alerts simulation.*

---

## 📄 Project Artifacts & Public Accessibility
* **Architecture Diagram:** [architecture_diagram.pdf](architecture_diagram.pdf)
* **Project Presentation Deck:** [presentation.pdf](presentation.pdf)
* **Open-Source License:** This project is open-source and licensed under the **MIT License**.

*All files, documentation, and asset links in this repository are set to **Public** and are fully accessible to the Happiest Health evaluation panel without requiring additional permissions.*
