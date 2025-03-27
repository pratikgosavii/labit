from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import *

class cartserializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = ['id', 'user', 'type', 'test', 'medicine', 'quantity', 'is_labitnow']


class order_serializer(serializers.ModelSerializer):
    items = serializers.ListField(write_only=True)  # Expect a list of items in the request

    class Meta:
        model = order
        fields = ['type', 'total_price', 'payment_status', 'transaction_id', 'items']

    def create(self, validated_data):
        """Creates an order and associated items"""
        request = self.context.get('request')
        items_data = validated_data.pop('items', [])

        order_instance = order.objects.create(user=request.user, **validated_data)

        order_items = []
        for item in items_data:
            lab_test_id = item.get('lab_test')
            medicine_id = item.get('medicine')
            quantity = item.get('quantity', 1)
            is_labitnow = item.get('is_labitnow', False)
            price = item.get('price')

            if not price:
                raise serializers.ValidationError("Price is required for each item.")

            if not (lab_test_id or medicine_id):
                raise serializers.ValidationError("Each item must have either a lab test or medicine.")

            order_items.append(order_item(
                order=order_instance,
                lab_test_id=lab_test_id if lab_test_id else None,
                medicine_id=medicine_id if medicine_id else None,
                quantity=quantity,
                is_labitnow=is_labitnow,
                price=price
            ))

        order_item.objects.bulk_create(order_items)  # Insert all items in bulk
        return order_instance
    

from rest_framework import serializers
from .models import hub_to_vendor

class HubToVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = hub_to_vendor
        fields = ['id', 'order', 'labbotomist', 'created_at']
        read_only_fields = ['id', 'created_at']  # Auto-filled fields


    def create(self, validated_data):
        """Set the user before creating the order"""
        request = self.context.get('request')
        labbotomist_instance = labbotomist_details.objects.get(user = request.user)

        validated_data['labbotomist'] = labbotomist_instance  # Assign user here
        return super().create(validated_data)