package personalized_healthcare_system.service.impl;

import org.springframework.stereotype.Service;
import personalized_healthcare_system.entity.Patient;
import personalized_healthcare_system.repository.PatientRepository;
import personalized_healthcare_system.service.PatientService;

import java.util.List;

@Service
public class PatientServiceImpl implements PatientService {

    private final PatientRepository patientRepository;

    public PatientServiceImpl(PatientRepository patientRepository) {
        this.patientRepository = patientRepository;
    }

    @Override
    public Patient savePatient(Patient patient) {
        return patientRepository.save(patient);
    }

    @Override
    public List<Patient> getAllPatients() {
        return patientRepository.findAll();
    }
}