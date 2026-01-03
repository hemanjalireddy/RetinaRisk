from pydantic import BaseModel

class PatientData(BaseModel):
    id: str
    age: int
    name: str

class AnalysisResponse(BaseModel):
    status: str
    message: str