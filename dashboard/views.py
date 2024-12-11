# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from services.models import Service
from .models import Appointment, Vehicle
from django.contrib import messages
from .forms import AccountSettingsForm, ContactSupportForm
from accounts.models import UserProfile
from accounts.forms import UserProfileForm
from django.contrib.auth import logout
from services.models import Service 
from booking.models import Booking
from django.contrib.auth import get_user_model
from accounts.models import User
User.objects.all()


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





@login_required
def admin_dashboard(request):
    # Get data for dashboard overview
    total_bookings = Booking.objects.count()
    pending_bookings = Booking.objects.filter(status='Pending').count()
    total_services = Service.objects.count()
    active_users = get_user_model().objects.filter(is_active=True).count()

    # Get the list of services, bookings, and users
    services = Service.objects.all()
    bookings = Booking.objects.all()
    users = get_user_model().objects.all()

    # Pass the data to the template
    context = {
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'total_services': total_services,
        'active_users': active_users,
        'services': services,
        'bookings': bookings,
        'users': users,
    }

    return render(request, 'dashboard/admin_dashboard.html', context)







def siteadmin_dashboard(request):
    services = Service.objects.all()  # Fetch all services
    return render(request, 'dashboard/siteadmin_dashboard.html', {'services': services})


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



