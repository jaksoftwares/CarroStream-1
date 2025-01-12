# models.py in payments app
from django.db import models
from services.models import Booking

class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Payment {self.transaction_id} for {self.booking}"

class Invoice(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to="invoices/")

    def __str__(self):
        return f"Invoice for {self.payment.transaction_id}"
