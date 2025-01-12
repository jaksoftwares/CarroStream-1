from django import forms
from .models import Service, PricingPlan, TeamMember, Testimonial, FAQ, Booking, Payment, MediaFile

# Service Model Form
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'price', 'description', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),  # Optional restriction for images
        }

# Pricing Plan Model Form
class PricingPlanForm(forms.ModelForm):
    class Meta:
        model = PricingPlan
        fields = ['plan_name', 'features', 'price']

# Team Member Model Form
class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'role']

# Testimonial Model Form
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['user', 'feedback']

# FAQ Model Form
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']

# Booking Model Form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'service', 'date', 'status']

# Payment Model Form
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['user', 'amount', 'date']

# Media File Model Form (Single file upload)
class MediaFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'accept': 'image/*'}),  # Restricting to image files (optional)
        }
