package personalized_healthcare_system.service;

import personalized_healthcare_system.entity.Patient;

import java.util.List;

public interface PatientService {

    Patient savePatient(Patient patient);

    List<Patient> getAllPatients();
}