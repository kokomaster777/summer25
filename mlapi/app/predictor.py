import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "models" / "model.pkl"

# Порядок признаков как при обучении!
FEATURE_ORDER = [
    'gender', 'hemoglobin', 'Gtp', 'height(cm)', 'triglyceride',
    'LDL', 'ALT', 'HDL', 'Cholesterol', 'fasting blood sugar',
    'waist(cm)', 'systolic', 'relaxation', 'weight(kg)',
    'age', 'BMI', 'serum creatinine', 'AST'
]

def predict_smoker(data) -> bool:
    """Предсказывает, курит ли человек."""
    try:
        model = joblib.load(MODEL_PATH)
        
        # Подготовка данных
        input_data = [
            1 if data.gender == "M" else 0,  # Кодирование gender
            data.hemoglobin,
            data.gtp,
            data.height,
            data.triglyceride,
            data.ldl,
            data.alt,
            data.hdl,
            data.cholesterol,
            data.fasting_blood_sugar,
            data.waist,
            data.systolic,
            data.relaxation,
            data.weight,
            data.age,
            data.bmi or (data.weight / (data.height / 100) ** 2),
            data.serum_creatinine,
            data.ast
        ]
        
        df = pd.DataFrame([input_data], columns=FEATURE_ORDER)
        return bool(model.predict(df)[0])
        
    except Exception as e:
        raise RuntimeError(f"Ошибка предсказания: {str(e)}")