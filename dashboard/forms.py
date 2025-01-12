# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Appointment, Vehicle



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

from django import forms
from dashboard.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'date', 'time', 'comments']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'required': True}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Any additional information...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].empty_label = 'Select Service'


