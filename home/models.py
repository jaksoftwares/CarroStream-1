# models.py in support app
from django.db import models
from accounts.models import User

class SupportTicket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
class Testimonial(models.Model):
    testimonial_text = models.TextField()  # Stores the testimonial text
    author_name = models.CharField(max_length=100)  # Stores the name of the author
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # Stores the rating (e.g., 4.8)
    
    def __str__(self):
        return f"Testimonial by {self.author_name} - {self.rating} stars"
