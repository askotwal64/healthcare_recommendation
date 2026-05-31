package personalized_healthcare_system.dto;

import lombok.Data;

@Data
public class PredictionRequest {

    private Integer age;
    private String gender;
    private Double bmi;
    private String smokingStatus;
    private String alcoholConsumption;
    private String physicalActivityLevel;
    private String dietType;
    private Double glucoseLevel;
    private Double hba1c;

    private Double prsCardiometabolic;
    private Double prsType2Diabetes;

    private Integer apoeE4Carrier;
    private Integer brcaPathogenicVariant;

    private Integer familyHistoryCVD;
    private Integer familyHistoryT2D;

    private Double stressLevel;

    private Integer depressionScore;
    private Integer anxietyScore;
    private Integer socialIsolationIndex;

    private Double sleepHours;
    private String sleepQuality;

    private Integer restingHeartRate;
    private Double hrv;

    private Integer systolicBP;
    private Integer diastolicBP;

    private Double ldl;
    private Double hdl;
    private Double triglycerides;

    private Double crp;
    private Double egfr;

    private Double waistCircumference;
}