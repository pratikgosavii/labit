from django.db import models

# Create your models here.

from users.models import *

class pharmacy(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owner_full_name = models.CharField(max_length=255)
    pharmacy_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner_full_name