package personalized_healthcare_system.service.impl;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import personalized_healthcare_system.dto.PredictionRequest;
import personalized_healthcare_system.dto.PredictionResponse;
import personalized_healthcare_system.service.PredictionService;

@Service
public class PredictionServiceImpl implements PredictionService {

    private final RestTemplate restTemplate;

    public PredictionServiceImpl(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    @Override
    public PredictionResponse predict(PredictionRequest request) {

        String url = "http://localhost:5000/predict";

        ResponseEntity<PredictionResponse> response =
                restTemplate.postForEntity(
                        url,
                        request,
                        PredictionResponse.class
                );

        return response.getBody();
    }
}