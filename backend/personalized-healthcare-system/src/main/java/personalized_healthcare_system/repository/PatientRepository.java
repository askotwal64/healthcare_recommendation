package personalized_healthcare_system.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import personalized_healthcare_system.entity.Patient;

public interface PatientRepository extends JpaRepository<Patient, Long > {
}
