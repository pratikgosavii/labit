from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime




class order_Form(forms.ModelForm):
    class Meta:
        model = order
        fields = '__all__'
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'id': 'user'}),
            'type': forms.Select(attrs={'class': 'form-control', 'id': 'type'}),
            'lab_test': forms.Select(attrs={'class': 'form-control', 'id': 'test'}),
            'medicine': forms.Select(attrs={'class': 'form-control', 'id': 'medicine'}),
            'labbotomist': forms.Select(attrs={'class': 'form-control', 'id': 'labbotomist'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'id': 'quantity'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'total_price', 'step': '0.01'}),
            'payment_status': forms.Select(attrs={'class': 'form-control', 'id': 'payment_status'}),
            'transaction_id': forms.TextInput(attrs={'class': 'form-control', 'id': 'transaction_id'}),
            'status': forms.Select(attrs={'class': 'form-control', 'id': 'sdsds'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control', 'id': 'created_at', 'readonly': 'readonly'}),
        }
