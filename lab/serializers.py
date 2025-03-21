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
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = labbotomist_details
        fields = ['id', 'full_name', 'mobile_no', 'address', 'username', 'password']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        user = User.objects.create(
            username=username,
            is_labbotomist=True,
            password=make_password(password)  # Encrypt password
        )

        labbotomist = labbotomist_details.objects.create(user=user, **validated_data)
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
