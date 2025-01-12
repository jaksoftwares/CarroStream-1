# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('newsletter', views.compose_newsletter, name='newsletter'),
   
]
