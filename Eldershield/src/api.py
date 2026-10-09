import random
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from risk_engine import predict_risk

app = FastAPI(title="ElderShield API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Patient(BaseModel):
    age: float
    hypertension: int
    heart_disease: int
    avg_glucose_level: float
    bmi: float
    gender: str = "Male"
    residence: str = "Urban"
    work_type: str = "Private"
    smoking: str = "never smoked"


@app.get("/")
def home():
    return {"status": "ElderShield API chal rahi hai"}


@app.post("/predict")
def predict(p: Patient):
    return predict_risk(p.model_dump())


@app.post("/whatif")
def whatif(p: Patient):
    base_p = p.model_dump()
    base = predict_risk(base_p)
    scenarios = {
        "Hypertension control": {"hypertension": 0},
        "Smoking chhod de": {"smoking": "never smoked"},
    }
    out = []
    for name, change in scenarios.items():
        r = predict_risk({**base_p, **change})
        out.append({"scenario": name, "score": r["score"], "band": r["band"],
                    "change": round(r["score"] - base["score"], 3)})
    return {"current": base, "scenarios": out,
            "note": "Model-based estimate, clinical validation baaki hai"}


# ---------- Live patient simulator ----------
state = {"tick": 0}


@app.get("/live")
def live():
    state["tick"] += 1
    t = state["tick"]

    # Shuru mein stable, 15 tick ke baad vitals bigadne lagte hain (25 par cap)
    stress = min(max(0, t - 15), 25)

    heart_rate = 74 + stress * 1.5 + random.uniform(-2, 2)
    systolic_bp = 130 + stress * 2.0 + random.uniform(-3, 3)
    spo2 = 97 - stress * 0.15 + random.uniform(-0.5, 0.5)

    hypertension = 1 if systolic_bp >= 140 else 0
    glucose = 105 + stress * 1.0

    risk = predict_risk({
        "age": 72, "hypertension": hypertension, "heart_disease": 0,
        "avg_glucose_level": glucose, "bmi": 28, "gender": "Male",
        "residence": "Urban", "work_type": "Private", "smoking": "never smoked",
    })

    if systolic_bp >= 160 or spo2 < 92 or heart_rate > 110:
        status = "ALERT"
        alert = "ALERT: caregiver ko notify karo, vitals bigad rahe hain"
    elif systolic_bp >= 140 or spo2 < 94 or heart_rate > 95:
        status = "WARNING"
        alert = None
    else:
        status = "STABLE"
        alert = None

    return {
        "tick": t,
        "heart_rate": round(heart_rate),
        "systolic_bp": round(systolic_bp),
        "spo2": round(spo2, 1),
        "score": risk["score"],
        "band": risk["band"],
        "status": status,
        "alert": alert,
    }


@app.post("/live/reset")
def live_reset():
    state["tick"] = 0
    return {"status": "reset"}


# ---------- Fall event (simulated) ----------
events = []


@app.post("/fall")
def fall():
    ev = {
        "type": "FALL_DETECTED",
        "patient": "Ramesh Kumar (72)",
        "time": datetime.now().strftime("%H:%M:%S"),
        "message": "Ramesh Kumar ke ghar mein girne ka signal mila. Turant check karein.",
    }
    events.insert(0, ev)
    return ev


@app.get("/events")
def get_events():
    return events[:5]


@app.post("/events/clear")
def clear_events():
    events.clear()
    return {"status": "cleared"}