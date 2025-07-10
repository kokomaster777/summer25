import joblib

model = joblib.load("models/model.pkl")
print("Признаки модели:", model.feature_names_in_)  # Теперь работает!