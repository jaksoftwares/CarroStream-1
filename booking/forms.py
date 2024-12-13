from django import forms
from services.models import Service
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'booking_date', 'booking_time', 'comments']

    service = forms.ModelChoiceField(queryset=Service.objects.all())
    booking_date = forms.DateField(widget=forms.SelectDateWidget())
    booking_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))