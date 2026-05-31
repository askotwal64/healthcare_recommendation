import joblib

diagnosis_model = joblib.load("diagnosis_model.pkl")

print("Diagnosis Features:")
print(diagnosis_model.feature_names_in_)