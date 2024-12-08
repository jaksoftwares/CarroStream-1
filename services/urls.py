# services/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('manage/', views.manage_services, name='manage_services'),
    path('services/get/', views.get_services, name='get_services'),
    path('services/add/', views.add_service, name='add_service'),
    path('edit/<int:pk>/', views.edit_service, name='edit_service'),
    path('delete/<int:pk>/', views.delete_service, name='delete_service'),
    path('services/', views.services_page, name = 'services'),
    
]
