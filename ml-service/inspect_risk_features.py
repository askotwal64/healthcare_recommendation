import joblib

risk_models = joblib.load("risk_model.pkl")

for name, model in risk_models.items():
    print(f"\n{name} Model Features:")
    print(model.feature_names_in_)