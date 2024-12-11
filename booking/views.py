from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Booking, Service
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Basic view example
def booking(request):
    return render(request, 'booking/booking.html')

@login_required
def book_service(request, service_id):
    if request.method == "POST":
        # Get the service object
        service = get_object_or_404(Service, id=service_id)

        # Create a booking for the authenticated user
        try:
            booking = Booking.objects.create(
                service=service,
                user=request.user,
                status="Pending",  # Initial status, can be updated later
            )

            # Fetch all the user's bookings
            bookings = Booking.objects.filter(user=request.user)

            # Return to the dashboard with updated bookings
            return render(request, "dashboard/user_dashboard.html", {
                "bookings": bookings,  # Pass the updated bookings to the template
                "services": Service.objects.all()  # You can pass other necessary context as well
            })
        except Exception as e:
            # Return an error if something goes wrong
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

