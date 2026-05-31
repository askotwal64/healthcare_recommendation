package personalized_healthcare_system.service;

import personalized_healthcare_system.dto.PredictionRequest;
import personalized_healthcare_system.dto.PredictionResponse;

public interface PredictionService {

    PredictionResponse predict(PredictionRequest request);

}