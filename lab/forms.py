



from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime




class labbotomist_details_Form(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
        required=False  # Allow keeping existing password on update
    )

    class Meta:
        model = labbotomist_details
        fields = ['username', 'password', 'full_name', 'mobile_no', 'address']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile No'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'rows': 3}),
        }

    def save(self, commit=True):
        # Create User first
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user, created = User.objects.get_or_create(username=username)
        if password:
            user.set_password(password)
            user.save()

        # Now save the labbotomist with the user
        labbotomist = super().save(commit=False)
        labbotomist.user = user  # Link user to labbotomist

        if commit:
            labbotomist.save()
        return labbotomist
    