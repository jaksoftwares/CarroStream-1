# models.py in content_management app
from django.db import models
from accounts.models import User

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

class AdminLog(models.Model):
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_admin': True})
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
