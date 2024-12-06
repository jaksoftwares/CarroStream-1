# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Appointment, Vehicle

# Service Booking Form
class BookServiceForm(forms.Form):
    service_choices = [
        ('car_wash', 'Car Wash'),
        ('oil_change', 'Oil Change'),
        ('tire_rotation', 'Tire Rotation'),
        ('brake_repair', 'Brake Repair'),
        ('full_detailing', 'Full Detailing')
    ]
    
    service_type = forms.ChoiceField(choices=service_choices)
    appointment_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

# Account Settings Form
class AccountSettingsForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

# Contact Support Form
class ContactSupportForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Describe your issue here...'}))
