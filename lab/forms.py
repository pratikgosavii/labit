



from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime




class labbotomist_details_Form(forms.ModelForm):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
        required=False  # Allow keeping existing password on update
    )

    class Meta:
        model = labbotomist_details
        fields = ['email', 'password', 'only_delivery', 'full_name', 'mobile_no', 'address']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile No'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'rows': 3}),
        }

    def save(self, commit=True):
        # Create User first
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user, created = User.objects.get_or_create(email=email, is_labbotomist = True)
        if password:
            user.set_password(password)
            user.save()

        # Now save the labbotomist with the user
        labbotomist = super().save(commit=False)
        labbotomist.user = user  # Link user to labbotomist

        if commit:
            labbotomist.save()
        return labbotomist
    