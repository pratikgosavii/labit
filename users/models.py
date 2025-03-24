from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_pharmassist = models.BooleanField(default=False)
    is_labbotomist = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    
    username = None  # Remove username field

    USERNAME_FIELD = 'email'  # Set email as the login field
    REQUIRED_FIELDS = [] 