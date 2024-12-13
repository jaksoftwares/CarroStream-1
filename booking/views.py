from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from services.models import Service
from django.shortcuts import redirect, get_object_or_404

# Basic view example
def booking(request):
    return render(request, 'booking/booking.html')


@login_required
def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.full_name = request.user.get_full_name()  # Assuming full name is available in the user model
            booking.save()
            return redirect('dashboard:siteadmin_dashboard')  # Redirect to the dashboard or another page after successful booking
    else:
        form = BookingForm()

    services = Service.objects.all()
    return render(request, 'booking_form.html', {'form': form, 'services': services})

@login_required
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.service = service
            booking.save()
            return redirect('dashboard:user_dashboard')  # Redirect to the dashboard
    else:
        form = BookingForm()

    return render(request, 'dashboard/user_dashboard.html', {'form': form, 'service': service})

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Set the current user automatically
            booking.save()
            return redirect('dashboard')  # Redirect to the dashboard after saving the booking
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'cancelled'
    booking.save()
    return redirect('dashboard:user_dashboard')