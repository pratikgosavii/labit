from django.db import models

# Create your models here.





# test title, description, mrp, vendor b2b min max, 

# vendor select box processing time, price b2b ka.

from masters.models import *

class lab_test(models.Model):

    lab = models.ForeignKey(lab, on_delete=models.CASCADE)  # Link to the user
    test = models.ForeignKey(test, on_delete=models.CASCADE)  # Link to the doctor
    address = models.TextField()
    processing_time = models.IntegerField()
    b2b_price = models.IntegerField()
    description = models.CharField(max_length=120, unique=False, null = True, blank = True)




class labbotomist_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="labbotomist_details")
    full_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    only_delivery = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name