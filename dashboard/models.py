from django.db import models
from django.conf import settings  # Import settings to access the custom user model
from accounts.models import User
from services.models import Service 
from django.utils import timezone
from datetime import date

class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    service_type = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, default='upcoming')

    def __str__(self):
        return f'{self.service_type} for {self.user.username} on {self.appointment_date}'

class Vehicle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment of {self.amount} by {self.user.username} on {self.date}'

from django.db import models



class Booking(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='dashboard_bookings')
    date = models.DateField(default=date.today)
    time = models.TimeField()  # Make sure this exists
    preferred_date = models.DateField(default='2024-01-01')
    comments = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.full_name} on {self.preferred_date} at {self.preferred_time}"



