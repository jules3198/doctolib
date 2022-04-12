from django import forms
from .models import ValidadeDoctor



class ValidadeDoctorForm(forms.Form):
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
    qualification_name = forms.CharField(max_length=63,label="qualification name")
    department = forms.ChoiceField(choices=department, label="department")
    hospital_name = forms.CharField(max_length=63,label="hospital_name")
    location = forms.CharField(max_length=63,label="location")