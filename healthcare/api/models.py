from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    medical_history = models.TextField()

    def __str__(self) -> str:
        """String representation of the patient (returns the name)."""
        return self.name

    """
    Represents a patient in the healthcare system.
    Each patient is linked to a Django User account.
    """
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    name: str = models.CharField(max_length=255)
    age: int = models.IntegerField()
    gender: str = models.CharField(max_length=10)
    medical_history: str = models.TextField()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self) -> str:
        """String representation of the doctor (returns the name)."""
        return self.name

    """
    Represents a doctor in the healthcare system.
    Each doctor is linked to a Django User account.
    """
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    name: str = models.CharField(max_length=255)
    specialization: str = models.CharField(max_length=255)
    contact_info: str = models.TextField()


class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assigned_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """String representation of the mapping (patient - doctor)."""
        return f"{self.patient.name} - {self.doctor.name}"

    """
    Maps a patient to a doctor, representing their assignment.
    Includes the timestamp when the mapping was created.
    """
    patient: Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor: Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assigned_on = models.DateTimeField(auto_now_add=True)
