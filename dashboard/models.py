# models.py
from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, default='upcoming')

    def __str__(self):
        return f'{self.service_type} for {self.user.username} on {self.appointment_date}'

class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment of {self.amount} by {self.user.username} on {self.date}'
