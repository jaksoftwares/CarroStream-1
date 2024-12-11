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
