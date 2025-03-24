from django.db import models

# Create your models here.


from masters.models import *
from users.models import User


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)  # Link to the doctor
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')

    def __str__(self):
        return f"{self.user.email} - {self.doctor.name} ({self.appointment_date})"