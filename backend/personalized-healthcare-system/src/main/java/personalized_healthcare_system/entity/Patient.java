package personalized_healthcare_system.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "patients")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Patient {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Integer age;

    private String gender;

    private Double bmi;

    private String smoking;

    private String alcohol;

    private String physicalActivity;

    private String dietType;

    private String bloodPressure;

    private Integer cholesterol;

    private Integer glucose;

    private Integer heartRate;

    private Double sleepHours;

    private String familyHistory;

    private String stressLevel;
}
