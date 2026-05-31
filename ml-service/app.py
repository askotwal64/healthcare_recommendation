from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Load models
diagnosis_model = joblib.load("diagnosis_model.pkl")
risk_models = joblib.load("risk_model.pkl")
encoder = joblib.load("ordinal_encoder.pkl")


class PredictionRequest(BaseModel):

    age: int
    gender: str
    bmi: float
    smokingStatus: str
    alcoholConsumption: str
    physicalActivityLevel: str
    dietType: str

    glucoseLevel: float
    hba1c: float

    prsCardiometabolic: float
    prsType2Diabetes: float

    apoeE4Carrier: int
    brcaPathogenicVariant: int

    familyHistoryCVD: int
    familyHistoryT2D: int

    stressLevel: float

    depressionScore: int
    anxietyScore: int
    socialIsolationIndex: int

    sleepHours: float
    sleepQuality: str

    restingHeartRate: int
    hrv: float

    systolicBP: int
    diastolicBP: int

    ldl: float
    hdl: float
    triglycerides: float

    crp: float
    egfr: float

    waistCircumference: float


@app.get("/")
def home():
    return {"message": "Healthcare ML API Running"}


@app.post("/predict")
def predict(request: PredictionRequest):

    try:

        data = pd.DataFrame([{
            "Age": request.age,
            "Gender": request.gender,
            "BMI": request.bmi,
            "Smoking_Status": request.smokingStatus,
            "Alcohol_Consumption": request.alcoholConsumption,
            "Physical_Activity_Level": request.physicalActivityLevel,
            "Diet_Type": request.dietType,
            "Glucose_Level": request.glucoseLevel,
            "HbA1c": request.hba1c,
            "PRS_Cardiometabolic": request.prsCardiometabolic,
            "PRS_Type2Diabetes": request.prsType2Diabetes,
            "APOE_e4_Carrier": request.apoeE4Carrier,
            "BRCA_Pathogenic_Variant": request.brcaPathogenicVariant,
            "Family_History_CVD": request.familyHistoryCVD,
            "Family_History_T2D": request.familyHistoryT2D,
            "Stress_Level": request.stressLevel,
            "Depression_Score": request.depressionScore,
            "Anxiety_Score": request.anxietyScore,
            "Social_Isolation_Index": request.socialIsolationIndex,
            "Sleep_Hours": request.sleepHours,
            "Sleep_Quality": request.sleepQuality,
            "Resting_Heart_Rate": request.restingHeartRate,
            "HRV": request.hrv,
            "Systolic_BP": request.systolicBP,
            "Diastolic_BP": request.diastolicBP,
            "LDL": request.ldl,
            "HDL": request.hdl,
            "Triglycerides": request.triglycerides,
            "CRP": request.crp,
            "eGFR": request.egfr,
            "Waist_Circumference": request.waistCircumference
        }])

        categorical_cols = [
            "Alcohol_Consumption",
            "Sleep_Quality",
            "Physical_Activity_Level",
            "Gender",
            "Smoking_Status",
            "Diet_Type"
        ]

        data[categorical_cols] = encoder.transform(
            data[categorical_cols]
        )

        print(data.head())

        diagnosis = diagnosis_model.predict(data)[0]

        heart_risk = risk_models["Heart"].predict(data)[0]

        diabetes_risk = risk_models["Diabetes"].predict(data)[0]

        overall_risk = risk_models["Overall"].predict(data)[0]

        return {
            "diagnosis": str(diagnosis),
            "heartRisk": float(heart_risk),
            "diabetesRisk": float(diabetes_risk),
            "overallRisk": float(overall_risk)
        }

    except Exception as e:
        import traceback

        traceback.print_exc()

        return {
            "error": str(e)
        }

    data = pd.DataFrame([{
        "Age": request.age,
        "Gender": request.gender,
        "BMI": request.bmi,
        "Smoking_Status": request.smokingStatus,
        "Alcohol_Consumption": request.alcoholConsumption,
        "Physical_Activity_Level": request.physicalActivityLevel,
        "Diet_Type": request.dietType,
        "Glucose_Level": request.glucoseLevel,
        "HbA1c": request.hba1c,
        "PRS_Cardiometabolic": request.prsCardiometabolic,
        "PRS_Type2Diabetes": request.prsType2Diabetes,
        "APOE_e4_Carrier": request.apoeE4Carrier,
        "BRCA_Pathogenic_Variant": request.brcaPathogenicVariant,
        "Family_History_CVD": request.familyHistoryCVD,
        "Family_History_T2D": request.familyHistoryT2D,
        "Stress_Level": request.stressLevel,
        "Depression_Score": request.depressionScore,
        "Anxiety_Score": request.anxietyScore,
        "Social_Isolation_Index": request.socialIsolationIndex,
        "Sleep_Hours": request.sleepHours,
        "Sleep_Quality": request.sleepQuality,
        "Resting_Heart_Rate": request.restingHeartRate,
        "HRV": request.hrv,
        "Systolic_BP": request.systolicBP,
        "Diastolic_BP": request.diastolicBP,
        "LDL": request.ldl,
        "HDL": request.hdl,
        "Triglycerides": request.triglycerides,
        "CRP": request.crp,
        "eGFR": request.egfr,
        "Waist_Circumference": request.waistCircumference
    }])

    categorical_cols = [
        "Alcohol_Consumption",
        "Sleep_Quality",
        "Physical_Activity_Level",
        "Gender",
        "Smoking_Status",
        "Diet_Type"
    ]

    data[categorical_cols] = encoder.transform(
        data[categorical_cols]
    )

    diagnosis = diagnosis_model.predict(data)[0]

    heart_risk = risk_models["Heart"].predict(data)[0]
    diabetes_risk = risk_models["Diabetes"].predict(data)[0]
    overall_risk = risk_models["Overall"].predict(data)[0]

    return {
        "diagnosis": str(diagnosis),
        "heartRisk": float(heart_risk),
        "diabetesRisk": float(diabetes_risk),
        "overallRisk": float(overall_risk)
    }