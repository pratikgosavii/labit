
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *

class pharmachy_serializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = pharmacy
        fields = ['id', 'owner_full_name', 'pharmacy_name', 'mobile_no', 'address', 'email', 'password']

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = User.objects.create(
            email=email,
            username=email,
            is_pharmassist=True,
            password=make_password(password)  # Encrypt password
        )

        labbotomist = pharmacy.objects.create(user=user, **validated_data)
        return labbotomist

    def update(self, instance, validated_data):
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)

        if email:
            instance.user.email = email
        if password:
            instance.user.password = make_password(password)  # Encrypt new password

        instance.user.save()
        return super().update(instance, validated_data)
