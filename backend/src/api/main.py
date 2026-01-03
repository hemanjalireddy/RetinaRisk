from fastapi import FastAPI
from backend.src.schemas.patient import PatientData, AnalysisResponse
from backend.src.services.patient_service import patient_service

app = FastAPI()

@app.get("/")
def health():
    return {"status": "online"}

@app.post("/analyze", response_model=AnalysisResponse)
def analyze(data: PatientData):
    return patient_service.process(data)