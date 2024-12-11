from django.urls import path
from . import views

app_name = 'booking'
urlpatterns = [
    # Define your routes here, e.g.,
path('booking', views.booking, name='booking'),
path('book-service/<int:service_id>/', views.book_service, name='book_service'),
# path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
