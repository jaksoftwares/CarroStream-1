# urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'dashboard'
urlpatterns = [
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin/', views.admin_dashboard, name='admin'),
     path('logout/', views.custom_logout, name='logout'),
    path('siteadmin', views.siteadmin_dashboard, name="siteadmin"),
    path('my_appointments/', views.my_appointments, name='my_appointments'),
    path('my_vehicles/', views.my_vehicles, name='my_vehicles'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('contact_support/', views.contact_support, name='contact_support'),
    path('logout/', views.logout_view, name='logout'),
    path('dummy/', views.dummy, name='dummy'),
    path('create/', views.create_booking, name='create_booking'),
    path('update-booking-status/<int:booking_id>/', views.update_booking_status, name='update_booking_status'),
]

