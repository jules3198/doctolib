from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
# Create your models here.




class ValidadeDoctor(models.Model):
    department = (
    ('Dentistry', "Dentistry"),
    ('Cardiology', "Cardiology"),
    ('ENT Specialists', "ENT Specialists"),
    ('Astrology', 'Astrology'),
    ('Neuroanatomy', 'Neuroanatomy'),
    ('Blood Screening', 'Blood Screening'),
    ('Eye Care', 'Eye Care'),
    ('Physical Therapy', 'Physical Therapy'),
    )
    praticient =models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(choices=department, max_length=100)
    qualification_name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Appointment(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    praticient = models.ForeignKey(ValidadeDoctor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    status_appointment = models.BooleanField(default=True)




class TakeAppointment(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

