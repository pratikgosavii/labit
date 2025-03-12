from django.db import models


from users.models import User
from datetime import datetime, timezone

import pytz
ist = pytz.timezone('Asia/Kolkata')



from users.models import User




class doctor(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True, null = True, blank = True)
    name = models.CharField(max_length=120, unique=False)
    image = models.ImageField(upload_to='doctor_images/')
    address = models.CharField(max_length=120, unique=False)
    mobile_no = models.IntegerField(null = True, blank = True)
    experience = models.IntegerField(null = True, blank = True)
    title = models.CharField(max_length=120, unique=False)
    degree = models.CharField(max_length=120, unique=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null = True, blank = True)
    remark = models.CharField(max_length=120, unique=False, null = True, blank = True)
    is_active = models.BooleanField(default = True)

    
    def __str__(self):
        return self.name
    
    


class lab(models.Model):

    name = models.CharField(max_length=120, unique=False)
    image = models.ImageField(upload_to='doctor_images/')
    rating = models.DecimalField(max_digits=3, decimal_places=1, null = True, blank = True)
    remark = models.CharField(max_length=120, unique=False, null = True, blank = True)
    is_active = models.BooleanField(default = True)

    
    def __str__(self):
        return self.name
    

class test(models.Model):

    name = models.CharField(max_length=120, unique=False)
    image = models.ImageField(upload_to='doctor_images/')
    price = models.IntegerField(null = True, blank = True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null = True, blank = True)
    remark = models.CharField(max_length=120, unique=False, null = True, blank = True)
    is_active = models.BooleanField(default = True)

    
    def __str__(self):
        return self.name
    
    

from django.utils.timezone import now


class coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)  # Unique coupon code
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # e.g., 10%
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Max ₹1000 discount
    min_purchase = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Min cart value required
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Cap on discount
    image = models.ImageField(upload_to='doctor_images/')
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
    
    
from django.db import models

class medicine_category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class medicine(models.Model):
    name = models.CharField(max_length=100, unique=True)
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='medicine_images/')
    
    # Suggested Additional Fields
    stock = models.PositiveIntegerField(default=0)  # Track available stock
    manufacturer = models.CharField(max_length=100, blank=True, null=True)  # Manufacturer details
    description = models.TextField(blank=True, null=True)  # Short description of the medicine
    category = models.ForeignKey(medicine_category, on_delete=models.SET_NULL, null=True, blank=True)
    prescription_required = models.BooleanField(default=False)  # Check if the medicine requires a prescription

    def __str__(self):
        return f"{self.name} - ₹{self.price}"
