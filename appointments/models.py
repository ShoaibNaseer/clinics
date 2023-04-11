from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Appointment(models.Model):
    patient_id = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    counsellor_id = models.ForeignKey('counsellors.Counsellor', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def validate_appointment_date(self):
        if self.appointment_date < timezone.now():
            raise ValidationError("Appointment date cannot be in the past.")

    def save(self, *args, **kwargs):
        self.validate_appointment_date()
        super().save(*args, **kwargs)
