
import joblib

model = joblib.load("diagnosis_model.pkl")

print(model.classes_)