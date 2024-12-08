# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from services.models import Service
from .models import Appointment, Vehicle
from django.contrib import messages
from .forms import BookServiceForm, AccountSettingsForm, ContactSupportForm


def user_dashboard(request):
    return render(request, 'dashboard/user_dashboard.html')

def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')
def siteadmin_dashboard(request):
    services = Service.objects.all()  # Fetch all services
    return render(request, 'dashboard/siteadmin_dashboard.html', {'services': services})
# Dashboard Overview
# @login_required
# def user_dashboard(request):
#     user = request.user
    
#     # Get appointments
#     total_appointments = Appointment.objects.filter(user=user).count()
#     upcoming_appointments = Appointment.objects.filter(user=user, status="upcoming").count()
#     recent_payments = Payment.objects.filter(user=user).count()

#     # Render dashboard with relevant data
#     return render(request, 'dashboard/user_dashboard.html', {
#         'total_appointments': total_appointments,
#         'upcoming_appointments': upcoming_appointments,
#         'recent_payments': recent_payments
#     })

# Book a Service
@login_required
def book_service(request):
    user = request.user
    if request.method == 'POST':
        form = BookServiceForm(request.POST)
        if form.is_valid():
            service_type = form.cleaned_data['service_type']
            appointment_date = form.cleaned_data['appointment_date']
            # Create the appointment
            Appointment.objects.create(user=user, service_type=service_type, appointment_date=appointment_date, status='upcoming')
            messages.success(request, f'{service_type} successfully booked for {appointment_date}!')
            return redirect('user_dashboard')
    else:
        form = BookServiceForm()

    return render(request, 'dashboard/book_service.html', {'form': form})

# View My Appointments
@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'my_appointments.html', {'appointments': appointments})

# Manage Vehicles
@login_required
def my_vehicles(request):
    vehicles = Vehicle.objects.filter(user=request.user)
    return render(request, 'my_vehicles.html', {'vehicles': vehicles})

# Account Settings
@login_required
def account_settings(request):
    if request.method == 'POST':
        form = AccountSettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account settings have been updated successfully!')
            return redirect('user_dashboard')
    else:
        form = AccountSettingsForm(instance=request.user)

    return render(request, 'account_settings.html', {'form': form})

# Help & Support
@login_required
def contact_support(request):
    if request.method == 'POST':
        form = ContactSupportForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            # Here you can add logic to store or send the support message
            messages.success(request, 'Your support request has been submitted!')
            return redirect('user_dashboard')
    else:
        form = ContactSupportForm()

    return render(request, 'contact_support.html', {'form': form})

# Log Out
@login_required
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')
