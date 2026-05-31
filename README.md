# Personalized Healthcare Recommendation System

## Project Overview

The Personalized Healthcare Recommendation System is an AI-powered healthcare application that predicts diseases, assesses health risks, and provides personalized recommendations based on patient health data.

The system integrates:

- Angular Frontend
- Spring Boot Backend
- FastAPI Machine Learning Service
- MySQL Database
- Scikit-Learn Machine Learning Models

---

## Features

### Patient Management
- Add patient records
- View patient information
- Store patient health details in MySQL

### Disease Prediction
Predicts possible conditions such as:

- Diabetes
- Hypertension
- Heart Disease
- Obesity
- Underweight
- Healthy

### Health Risk Assessment

Provides:

- Heart Disease Risk
- Diabetes Risk
- Overall Health Risk

### Personalized Recommendations

Generates:

- Medication Recommendations
- Diet Recommendations
- Exercise Recommendations

---

## Technology Stack

### Frontend
- Angular
- TypeScript
- HTML
- CSS

### Backend
- Spring Boot
- Java
- REST API

### Machine Learning Service
- Python
- FastAPI
- Scikit-Learn
- Joblib
- Pandas
- NumPy

### Database
- MySQL

---

## System Architecture

User

↓

Angular Frontend

↓

Spring Boot Backend

↓

FastAPI ML Service

↓

Machine Learning Models (GradientBoost)

↓

Prediction Results

---

## Project Structure

```text
PersonalizedHealthcareSystem
│
├── backend
├── healthcare-ui
├── ml-service
└── README.md
```

---

## API Endpoints

### Patient APIs

#### Get All Patients

```http
GET /patients
```

#### Add Patient

```http
POST /patients
```

---

### Prediction API

```http
POST /prediction
```

Request Body:

```json
{
  "age": 35,
  "gender": "Male",
  "bmi": 24.5
}
```

---

## Machine Learning Models

The project uses:

- diagnosis_model.pkl
- risk_model.pkl
- healthcare_model.pkl
- recommendation_model.pkl

---

## Future Enhancements

- JWT Authentication
- Doctor Dashboard
- Appointment Booking
- Medical Report Upload
- Real-time Monitoring
- Cloud Deployment

---

## Author

Ashish Singh Kotwal

Karthikadevi



Personalized Healthcare Recommendation System