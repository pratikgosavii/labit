from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Medicine or Test
    object_id = models.PositiveIntegerField()  # ID of the related object
    content_object = GenericForeignKey('content_type', 'object_id')  # Generic relation
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.content_object} ({self.quantity})"
