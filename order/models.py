from django.db import models

# Create your models here.


from django.db import models
from users.models import User
from masters.models import *
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TYPE_CHOICES = (
        ('test', 'Test'),
        ('medicine', 'Medicine'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    test = models.ForeignKey(test, on_delete=models.CASCADE, null=True, blank=True)
    medicine = models.ForeignKey(medicine, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)
