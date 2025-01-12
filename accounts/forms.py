from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, UserProfile  # Assuming UserProfile is the model where phone_number and address are stored

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=150, required=True)
    phone_number = forms.CharField(
        max_length=15, 
        required=True,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number (e.g., +254700123456 or 0700123456).')]
    )
    address = forms.CharField(
        max_length=255, 
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your address (e.g., 123 Street, Nairobi, Kenya)'
        })
    )
    profile_picture = forms.ImageField(required=False)
    terms = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password1', 'password2', 'profile_picture']

    def save(self, commit=True):
        # Save user
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()

        # Save the additional profile data (phone number, address, profile picture)
        user_profile = UserProfile.objects.create(
            user=user,
            phone_number=self.cleaned_data['phone_number'],
            address=self.cleaned_data['address'],
            profile_picture=self.cleaned_data.get('profile_picture')  # Save profile picture if uploaded
        )

        return user


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username or Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(
        max_length=15, 
        required=True,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number (e.g., +254700123456 or 0700123456).')]
    )
    address = forms.CharField(
        max_length=255, 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your address (e.g., 123 Street, Nairobi, Kenya)'}))

    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'profile_picture']
    
    def save(self, commit=True):
        # Save profile data
        user_profile = super().save(commit=False)
        if commit:
            user_profile.save()
        return user_profile
