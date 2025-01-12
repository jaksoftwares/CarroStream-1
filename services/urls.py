# services/urls.py
from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
   path('dashboard', views.dashboard, name='dashboard'),
   
    path('services', views.services_page, name='services'),
    
    # Add and Save  and delete Service
    path('add-service/', views.add_service, name='add_service'),
    path('delete-service/<int:service_id>/', views.delete_service, name='delete_service'),
    path('edit/<int:service_id>/', views.edit_service, name='edit_service'),

    # Team members
    path('add-team-member/', views.add_team_member, name='add_team_member'),
    path('edit-team-member/<int:team_member_id>/', views.edit_team_member, name='edit_team_member'),
    path('delete-team-member/<int:team_member_id>/', views.delete_team_member, name='delete_team_member'),


    # Add and Save Pricing Plan
    path('add-pricing-plan/', views.add_pricing_plan, name='add_pricing_plan'),


    # Add and Save Testimonial
    path('add-testimonial/', views.add_testimonial, name='add_testimonial'),

    # Add and Save FAQ
    path('add-faq/', views.add_faq, name='add_faq'),

    # Add and Save Booking
    path('add-booking/', views.add_booking, name='add_booking'),

    # Add and Save Payment
    path('add-payment/', views.add_payment, name='add_payment'),

    # Add and Save Media File
    path('add-media/', views.add_media, name='add_media'),


]
