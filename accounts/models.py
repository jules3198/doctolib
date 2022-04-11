from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    PATIENT = 'PATIENT'
    PRATICIENT = 'PRATICIENT'
    ROLE_CHOICES = (
        (PATIENT, 'patient'),
        (PRATICIENT, 'praticient')
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name="Role")