import joblib

files = [
    "risk_model.pkl",
    "diagnosis_model.pkl"
]

for file in files:
    try:
        model = joblib.load(file)
        print(f"{file} loaded successfully")
        print(type(model))
        print("-" * 50)

    except Exception as e:
        print(f"{file} failed")
        print(e)
        print("-" * 50)