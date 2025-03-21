
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *

class pharmachy_serializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = pharmacy
        fields = ['id', 'owner_full_name', 'pharmacy_name', 'mobile_no', 'address', 'username', 'password']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        user = User.objects.create(
            username=username,
            is_labbotomist=True,
            password=make_password(password)  # Encrypt password
        )

        labbotomist = pharmacy.objects.create(user=user, **validated_data)
        return labbotomist

    def update(self, instance, validated_data):
        username = validated_data.pop('username', None)
        password = validated_data.pop('password', None)

        if username:
            instance.user.username = username
        if password:
            instance.user.password = make_password(password)  # Encrypt new password

        instance.user.save()
        return super().update(instance, validated_data)
