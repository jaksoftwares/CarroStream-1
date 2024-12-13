from django.urls import path
from . import views

app_name = 'booking'
urlpatterns = [
    # Define your routes here, e.g.,
  # Route to handle the modal booking from the dashboard
    path('booking/book/<int:service_id>/', views.book_service, name='book_service'),

    # A generic booking view (if needed in other contexts)
    # path('book/', views.booking_view, name='booking_view'),

    # Route for canceling a booking
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
