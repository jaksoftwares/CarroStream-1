# views.py
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from services.models import Service
from accounts.models import User
from .models import Appointment, Vehicle
from django.contrib import messages
from .forms import AccountSettingsForm, ContactSupportForm
from accounts.models import UserProfile
from accounts.forms import UserProfileForm
from django.contrib.auth import logout
from services.models import Service 
from django.contrib.auth import get_user_model
from accounts.models import User
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserProfileForm
from contact.models import ContactMessage
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import  BookingForm
from django.views.decorators.csrf import csrf_exempt


@login_required
def user_dashboard(request):
    user = request.user
    profile = user.profile
    User.objects.all()
    

    # Fetch all services for the dropdown in the form
    services = Service.objects.all()

    # Fetch all bookings for the user, ordered by date
    bookings = Booking.objects.filter(user=user).order_by('-created_at')

    # Handle form submission for updating the user profile
    if request.method == "POST":
        # Profile form handling
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if 'profile_form' in request.POST and profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('dashboard:user_dashboard')  # Redirect after saving profile form

    else:
        profile_form = UserProfileForm(instance=profile)

    # Full name for the user (used in the template)
    full_name = f"{user.first_name} {user.last_name}"

    context = {
        'user': user,
        'user_profile': profile,
        'profile_form': profile_form,
        'services': services,
        'bookings': bookings,
        'full_name': full_name,
        'User': user,
    }

    return render(request, 'dashboard/user_dashboard.html', context)


@login_required
def create_booking(request):
    user = request.user
    services = Service.objects.all()

    if request.method == 'POST':
        # Handle booking creation
        service_id = request.POST.get('service')
        date = request.POST.get('date')
        time = request.POST.get('time')
        comments = request.POST.get('comments')

        service = get_object_or_404(Service, id=service_id)

        # Create new booking
        booking = Booking.objects.create(
            user=user,
            service=service,
            date=date,
            time=time,
            comments=comments,
            created_at=timezone.now()
        )
        
        messages.success(request, "Booking successfully made!")
        return redirect('dashboard:user_dashboard')  # Stay in the dashboard after booking

    context = {
        'services': services,
    }
    return render(request, 'dashboard/user_dashboard.html', context)  # Same dashboard template



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
    # Fetch all the data needed for the dashboard
    total_services = Service.objects.count()  # Count of all services
    total_users = get_user_model().objects.count()  # Total users
    pending_bookings = Booking.objects.filter(status='Pending').count()  # Count of pending bookings
    services = Service.objects.all()  # All services
    users = get_user_model().objects.all()  # All users
    contacts = ContactMessage.objects.all()  # Fetch all contact messages
    bookings = Booking.objects.all().select_related('user', 'service')
    bookings = Booking.objects.all()

    # Pass the data to the template
    context = {
        'total_bookings': pending_bookings,
        'pending_bookings': pending_bookings,
        'total_services': total_services,
        'total_users': total_users,
        'services': services,
        'users': users,
        'contacts': contacts,  # Add contacts to context
        'bookings': bookings,
    }

    return render(request, 'dashboard/siteadmin_dashboard.html', context)

@csrf_exempt
def update_booking_status(request, booking_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_status = data.get('status')
            
            booking = Booking.objects.get(id=booking_id)
            booking.status = new_status
            booking.save()

            return JsonResponse({'success': True})
        except Booking.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Booking not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})




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

def custom_logout(request):
    logout(request)
    return redirect('home') 



