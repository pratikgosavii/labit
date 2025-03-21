from django.db import models

# Create your models here.


from django.db import models
from users.models import User
from masters.models import *
from lab.models import *
from pharmacy.models import *
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


class order(models.Model):

    TYPE_CHOICES = [
        ('test', 'Test'),
        ('medicine', 'Medicine'),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("collected", "Collected"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)  # Differentiates Test & Medicine orders
    test = models.ForeignKey(test, on_delete=models.SET_NULL, null=True, blank=True)  # Optional for test orders
    medicine = models.ForeignKey(medicine, on_delete=models.SET_NULL, null=True, blank=True)  # Optional for medicine orders
    labbotomist = models.ForeignKey(labbotomist_details, on_delete=models.SET_NULL, null=True, blank=True)  # Optional for medicine orders
    pharmacy = models.ForeignKey(pharmacy, on_delete=models.SET_NULL, null=True, blank=True)  # Optional for medicine orders
    quantity = models.PositiveIntegerField(default=1)  # Only applicable for medicine orders
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')], default='pending')
    transaction_id = models.CharField(max_length=255, null=True, blank=True)  # Store Payment Gateway transaction ID
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

