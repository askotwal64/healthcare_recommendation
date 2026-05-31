import joblib

risk_models = joblib.load("risk_model.pkl")

print(type(risk_models))
print("\nKeys:")

for key in risk_models.keys():
    print(key)
    print(type(risk_models[key]))
    print("-" * 50)