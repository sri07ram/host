from django.db import models

class Hospital(models.Model):
    patient_name=models.CharField(max_length=100)
    patient_sick=models.CharField(max_length=100)
    a_time = models.CharField(max_length=100)
    doctor_name=models.CharField(max_length=100)
    patient_loc=models.CharField(max_length=100)
