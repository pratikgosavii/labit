from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import *

class cartserializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = ['id', 'user', 'type', 'test', 'medicine', 'quantity']


class order_serializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = ['user', 'type', 'test', 'medicine', 'quantity', 'total_price', 'payment_status', 'transaction_id']

    def validate(self, data):
        """Ensure either test or medicine is provided based on order type"""
        type = data.get('type')
        test = data.get('test')
        user = data.get('user')
        medicine = data.get('medicine')

        
        if type == 'test' and not test:
            raise serializers.ValidationError("Test must be provided for test orders.")
        if type == 'medicine' and not medicine:
            raise serializers.ValidationError("Medicine must be provided for medicine orders.")
        
        return data
    
from rest_framework import serializers
from .models import hub_to_vendor

class HubToVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = hub_to_vendor
        fields = ['id', 'order', 'labbotomist', 'created_at']
        read_only_fields = ['id', 'created_at']  # Auto-filled fields
