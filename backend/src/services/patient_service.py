from loguru import logger
from backend.src.schemas.patient import PatientData, AnalysisResponse

class PatientService:
    def process(self, patient: PatientData) -> AnalysisResponse:
        logger.info(f"Processing patient {patient.id}")
        return AnalysisResponse(
            status="success", 
            message=f"Patient {patient.name} received."
        )

# Singleton
patient_service = PatientService()