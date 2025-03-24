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
        fields = ['type', 'lab_test', 'medicine', 'quantity', 'total_price', 'payment_status', 'transaction_id']

    def validate(self, data):
        """Ensure either test or medicine is provided based on order type"""
        request = self.context.get('request')

        if not request or not request.user:
            raise serializers.ValidationError("User authentication is required.")

        type = data.get('type')
        lab_test = data.get('lab_test')
        medicine = data.get('medicine')

        if type == 'test' and not lab_test:
            raise serializers.ValidationError("Test must be provided for test orders.")
        if type == 'medicine' and not medicine:
            raise serializers.ValidationError("Medicine must be provided for medicine orders.")

        return data

    def create(self, validated_data):
        """Set the user before creating the order"""
        request = self.context.get('request')
        validated_data['user'] = request.user  # Assign user here
        return super().create(validated_data)
    
    
from rest_framework import serializers
from .models import hub_to_vendor

class HubToVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = hub_to_vendor
        fields = ['id', 'order', 'labbotomist', 'created_at']
        read_only_fields = ['id', 'created_at']  # Auto-filled fields
