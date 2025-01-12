from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=False, default="Default Full Name")
    email = models.EmailField(unique=True, blank=False)
    profile_picture = models.ImageField(upload_to='accounts/userprofile_pictures/', blank=True, null=True)  # Profile picture is optional
    

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='accounts/userprofile_pictures/', blank=True, null=True)  # Optional profile picture

    def __str__(self):
        return f"{self.user.username}'s profile"
