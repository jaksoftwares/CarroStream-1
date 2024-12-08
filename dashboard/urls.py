# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin/', views.admin_dashboard, name='admin'),
    path('siteadmin', views.siteadmin_dashboard, name="siteadmin"),
    path('book_service/', views.book_service, name='book_service'),
    path('my_appointments/', views.my_appointments, name='my_appointments'),
    path('my_vehicles/', views.my_vehicles, name='my_vehicles'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('contact_support/', views.contact_support, name='contact_support'),
    path('logout/', views.logout_view, name='logout'),
]
