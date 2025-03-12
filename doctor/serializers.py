from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Doctor, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Assign user
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())  # Assign doctor

    class Meta:
        model = Appointment
        fields = '__all__'
