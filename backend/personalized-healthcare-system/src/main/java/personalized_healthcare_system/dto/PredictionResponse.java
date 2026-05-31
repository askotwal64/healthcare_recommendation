package personalized_healthcare_system.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PredictionResponse {

    private String diagnosis;

    private Double heartRisk;

    private Double diabetesRisk;

    private Double overallRisk;

    private String medication;

    private String dietRecommendation;

    private String exerciseRecommendation;
}