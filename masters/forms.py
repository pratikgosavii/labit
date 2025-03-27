from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


class doctor_Form(forms.ModelForm):
    class Meta:
        model = doctor
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
           
            'lab_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'lab_name'
            }),
           
            'degree': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'degree'
            }),

            'title': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'title'
            }),

            'address': forms.Textarea(attrs={'class': 'form-control', 'id': 'address', 'rows': 3}), 

            'mobile_no': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'mobile_no'
            }),

            'experience': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'experience'
            }),
            
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            
            'remark': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'remark'
            }),
            
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
            
        }



    def save(self, commit=True):
        # Create a new User instance
        doctor_instance = super().save(commit=False)  # Get the doctor instance without saving it yet

        if not doctor_instance.user:  
            # If the doctor doesn't have a user, create a new one
            user = User.objects.create(email=self.cleaned_data['name'], is_doctor=True)
            user.set_password("defaultpassword")  # Hash the password
            user.save()
            doctor_instance.user = user  
        else:
            # If user already exists, update username
            doctor_instance.user.email = self.cleaned_data['name']
            doctor_instance.user.save()

        if commit:
            doctor_instance.save()

        return doctor_instance



class testimonials_Form(forms.ModelForm):
    class Meta:
        model = testimonials
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
          
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'price'
            }),

        }

class test_Form(forms.ModelForm):
    class Meta:
        model = test
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),

            'category': forms.Select(attrs={
                'class': 'form-control', 'id': 'category'
            }),
          

            'b2b_min_price': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'b2b_min_price'
            }),

            'b2b_max_price': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'b2b_max_price'
            }),

            'mrp': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'mrp'
            }),

            
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
            
        }



class lab_Form(forms.ModelForm):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
        required=False  # Allow keeping the existing password on update
    )

    class Meta:
        model = lab
        fields = ['email', 'password', 'name', 'image', 'lab_name', 'rating', 'remark', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'lab_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'lab_name'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'remark': forms.TextInput(attrs={'class': 'form-control', 'id': 'remark'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'rows': 3}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
        }

    def save(self, commit=True):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user, created = User.objects.get_or_create(email=email, defaults={'email': email, 'is_vendor': True})
        if password:
            user.set_password(password)
            user.save()

        # Now save the lab entry with the linked user
        lab_entry = super().save(commit=False)
        lab_entry.user = user  # Ensure email is saved in lab model

        if commit:
            lab_entry.save()
        return lab_entry
    
    


class coupon_Form(forms.ModelForm):
    class Meta:
        model = coupon
        fields = '__all__'  # Include all fields
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Coupon Code'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Coupon Code'}),
            'discount_percentage': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'discount_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'min_purchase': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'max_discount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }



class test_category_Form(forms.ModelForm):
    class Meta:
        model = test_category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
        }


class medicine_category_Form(forms.ModelForm):
    class Meta:
        model = medicine_category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
        }

class medicine_Form(forms.ModelForm):
    class Meta:
        model = medicine
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'expiry_date': forms.DateInput(attrs={
                'class': 'form-control', 'id': 'expiry_date', 'type': 'date'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'price', 'step': '0.01'
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'stock'
            }),
            'manufacturer': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'manufacturer'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'id': 'description', 'rows': 3
            }),
            'category': forms.Select(attrs={
                'class': 'form-control', 'id': 'category'
            }),
            'prescription_required': forms.CheckboxInput(attrs={
                'class': 'form-check-input', 'id': 'prescription_required'
            }),
        }






class home_banner_Form(forms.ModelForm):
    class Meta:
        model = home_banner
        fields = '__all__'
        widgets = {
           
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'title'
            }),
          
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'price'
            }),

            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }

