# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from services.models import Service
from .models import Appointment, Vehicle
from django.contrib import messages
from .forms import BookServiceForm, AccountSettingsForm, ContactSupportForm
from accounts.models import UserProfile
from accounts.forms import UserProfileForm
from django.contrib.auth import logout
from services.models import Service 



@login_required
def user_dashboard(request):
    user = request.user
    profile = user.profile

    # Fetch services from the Service model
    services = Service.objects.all()  # Get all available services from the database

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect back to the dashboard after saving
    else:
        form = UserProfileForm(instance=profile)

    # Add the services to the context to be passed to the template
    context = {
        'user': user,
        'user_profile': profile,
        'form': form,  # Pass the form to the template for rendering
        'services': services,  # Pass the services to the template
    }

    return render(request, 'dashboard/user_dashboard.html', context)


def custom_logout(request):
    logout(request)
    return redirect('home') 

def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')
def siteadmin_dashboard(request):
    services = Service.objects.all()  # Fetch all services
    return render(request, 'dashboard/siteadmin_dashboard.html', {'services': services})

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

def dummy(request):
    return render(request, 'dashboard/dummy.html')

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



