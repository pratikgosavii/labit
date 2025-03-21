from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_Pharmassist = models.BooleanField(default=False)
    is_labbotomist = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
