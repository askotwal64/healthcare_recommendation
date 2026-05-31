package personalized_healthcare_system.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import personalized_healthcare_system.dto.PredictionRequest;
import personalized_healthcare_system.dto.PredictionResponse;
import personalized_healthcare_system.service.PredictionService;

@RestController
@RequestMapping("/prediction")
@CrossOrigin(origins = "*")
public class PredictionController {

    private final PredictionService predictionService;

    public PredictionController(PredictionService predictionService) {
        this.predictionService = predictionService;
    }
    @PostMapping
    public PredictionResponse predict(
            @RequestBody PredictionRequest request) {

        return predictionService.predict(request);
    }
}