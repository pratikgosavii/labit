from django.http import JsonResponse
from rest_framework import serializers
from .models import home_banner  # Import your model

# Step 1: Create a serializer
class HomeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = home_banner
        fields = '__all__' 