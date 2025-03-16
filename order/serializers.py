from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import cart

class cartserializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = ['id', 'user', 'type', 'test', 'medicine', 'quantity']
