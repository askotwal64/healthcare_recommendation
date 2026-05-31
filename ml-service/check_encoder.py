import joblib

encoder = joblib.load("ordinal_encoder.pkl")

print(type(encoder))
print(encoder.categories_)