from pydantic import BaseModel, validator
from enum import Enum

class Gender(str, Enum):
    male = "M"
    female = "F"

class HealthData(BaseModel):
    gender: Gender
    age: int
    height: float
    weight: float
    waist: float
    systolic: float
    relaxation: float
    fasting_blood_sugar: float
    cholesterol: float
    triglyceride: float
    hdl: float
    ldl: float
    hemoglobin: float
    serum_creatinine: float
    ast: float
    alt: float
    gtp: float

    # Авторасчёт BMI, если не указан
    bmi: float | None = None  

    @validator('bmi', pre=True, always=True)
    def calc_bmi(cls, v, values):
        if v is None and values.get('height') and values.get('weight'):
            return values['weight'] / (values['height'] / 100) ** 2
        return v

class PredictionResult(BaseModel):
    smokes: bool