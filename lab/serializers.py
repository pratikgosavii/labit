from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import lab_test, lab, test

# Step 1: Create Serializer
class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = lab_test
        fields = '__all__'  # Include all fields



from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, labbotomist_details

class LabbotomistDetailsSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = labbotomist_details
        fields = ['id', 'only_delivery', 'full_name', 'mobile_no', 'address', 'email', 'password']

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = User.objects.create(
            email=email,
            is_labbotomist=True,
            password=make_password(password)  # Encrypt password
        )

        labbotomist = labbotomist_details.objects.create(user=user, **validated_data)
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


from masters.models import lab

class LabSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = lab
        fields = ['id', 'name', 'lab_name', 'email', 'password']

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')

        user = User.objects.create(
            email=email,
            is_vendor=True,
            password=make_password(password)  # Encrypt password
        )

        lab_instance = lab.objects.create(user=user, **validated_data)
        return lab_instance

    def update(self, instance, validated_data):
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)

        if email:
            instance.user.email = email
        if password:
            instance.user.password = make_password(password)  # Encrypt new password

        instance.user.save()
        return super().update(instance, validated_data)
