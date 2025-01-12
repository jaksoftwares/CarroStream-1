from django.db import models
from django.utils.text import slugify

# Service Model

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/')
    
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when a service is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update when the service is modified

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate the slug based on the title

            # Ensure the slug is unique
            original_slug = self.slug
            counter = 1
            while Service.objects.filter(slug=self.slug).exists():  # Check if slug already exists
                self.slug = f'{original_slug}-{counter}'  # Append a counter if slug is not unique
                counter += 1
        
        super().save(*args, **kwargs)

# Pricing Plan Model
class PricingPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    features = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.plan_name


# Team Member Model
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


# Testimonial Model
class Testimonial(models.Model):
    user = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return f"Testimonial by {self.user}"


# FAQ Model
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


# Booking Model
class Booking(models.Model):
    user = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services_bookings')
    date = models.DateField()
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ], default='Pending')

    def __str__(self):
        return f"Booking by {self.user} for {self.service}"


# Payment Model
class Payment(models.Model):
    user = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Payment of {self.amount} by {self.user}"


# Media Manager Model
class MediaFile(models.Model):
    file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Media file uploaded at {self.uploaded_at}"
