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
    is_labitnow = models.BooleanField(default=False)


class order(models.Model):
    TYPE_CHOICES = [
        ('test', 'Test'),
        ('medicine', 'Medicine'),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("collected_from_customer", "Collected From Customer"),
        ("delivered_to_hub", "Delivered To Hub"),
        ("collected_from_vendor", "Collected From Vendor"),
        ("delivered_to_vendor", "Delivered To Vendor"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)  # Order type (Test/Medicine)
    labbotomist = models.ForeignKey(labbotomist_details, on_delete=models.SET_NULL, null=True, blank=True)  
    pharmacy = models.ForeignKey(pharmacy, on_delete=models.SET_NULL, null=True, blank=True)  
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')], default='pending')
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

class order_item(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE, related_name="items")
    type = models.CharField(max_length=10, choices=[('test', 'Test'), ('medicine', 'Medicine')])
    lab_test = models.ForeignKey(lab_test, on_delete=models.SET_NULL, null=True, blank=True)  # Optional for test orders
    medicine = models.ForeignKey(medicine, on_delete=models.SET_NULL, null=True, blank=True)  # Optional for medicine orders
    quantity = models.PositiveIntegerField(default=1)
    is_labitnow = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)



class hub_to_vendor(models.Model):

    order = models.ForeignKey(order, on_delete=models.CASCADE)
    labbotomist = models.ForeignKey(labbotomist_details, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
