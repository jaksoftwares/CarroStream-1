from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Service
from .forms import ServiceForm
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Service, PricingPlan, TeamMember, Testimonial, FAQ, Booking, Payment, MediaFile
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .forms import ServiceForm, PricingPlanForm, TeamMemberForm, TestimonialForm, FAQForm, BookingForm, PaymentForm, MediaFileForm

def services_page(request):
    services = Service.objects.all() 
    return render(request, 'services/services.html', {'page_title': 'Services'}, {'services': services} )



# Dashboard View
def dashboard(request):
    # Fetch all the objects for the dashboard sections
    services = Service.objects.all()
    pricing_plans = PricingPlan.objects.all()
    team_members = TeamMember.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()
    bookings = Booking.objects.all()
    payments = Payment.objects.all()
    media_files = MediaFile.objects.all()
    
    context = {
        'services': services,
        'pricing_plans': pricing_plans,
        'team_members': team_members,
        'testimonials': testimonials,
        'faqs': faqs,
        'bookings': bookings,
        'payments': payments,
        'media_files': media_files,
    }
    
    return render(request, 'dashboard/siteadmin_dashboard.html', context)


# Add and Save Service
def add_service(request):
    if request.method == 'POST':
        # Initialize the form with POST data and the uploaded image
        form = ServiceForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect back to the dashboard (or to another URL)
            return redirect('services:dashboard')  # Ensure this points to your dashboard URL name
    else:
        form = ServiceForm()  # Create a blank form for GET requests

    # Fetch services to display them in the table
    services = Service.objects.all()

    # Pass the form and the list of services to the template
    return render(request, 'dashboard/siteadmin_dashboard.html', {'form': form, 'services': services})


# View for editing an existing service
def edit_service(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    
    if request.method == 'POST':
        # Update the service with the new data
        service.title = request.POST.get('title')
        service.price = request.POST.get('price')
        service.description = request.POST.get('description')
        service.image = request.FILES.get('image', service.image)
        service.save()

        # After saving, redirect back to the dashboard page
        return redirect('/dashboard/siteadmin')  # Redirect to the dashboard page after edit
    
    # Optionally, if you need to prepopulate the form with the current service data, 
    # you can pass the service instance to the template
    return render(request, 'dashboard/siteadmin', {'service': service})

def delete_service(request, service_id):
    try:
        if request.method == 'POST':
            service = get_object_or_404(Service, id=service_id)
            service.delete()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Invalid method'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


# Add Team Member
def add_team_member(request):
    if request.method == 'POST':
        # Handle form submission to add a new team member
        name = request.POST.get('name')
        role = request.POST.get('role')
        TeamMember.objects.create(name=name, role=role)
        return redirect('dashboard:siteadmin')  # Redirect to the dashboard page
    
    return render(request, 'dashboard/siteadmin_dashboard.html')

# Edit Team Member
def edit_team_member(request, team_member_id):
    team_member = get_object_or_404(TeamMember, pk=team_member_id)
    
    if request.method == 'POST':
        team_member.name = request.POST.get('name')
        team_member.role = request.POST.get('role')
        team_member.save()
        return redirect('dashboard:siteadmin')  # Redirect after saving

    return render(request, 'dashboard/siteadmin_dashboard.html', {'team_member': team_member})

# Delete Team Member
def delete_team_member(request, team_member_id):
    try:
        if request.method == 'POST':
            team_member = get_object_or_404(TeamMember, pk=team_member_id)
            team_member.delete()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Invalid method'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


























# Add and Save Pricing Plan
def add_pricing_plan(request):
    if request.method == 'POST':
        form = PricingPlanForm(request.POST)
        if form.is_valid():
            form.save()
            pricing_plans = PricingPlan.objects.all()
            html = render_to_string('dashboard/siteadmin_dashboard.html', {'pricing_plans': pricing_plans})
            return JsonResponse({'success': True, 'html': html})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = PricingPlanForm()
    return render(request, 'dashboard/siteadmin_dashboard.html', {'form': form})


# Add and Save Team Member
def add_team_member(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            team_members = TeamMember.objects.all()
            html = render_to_string('dashboard/siteadmin_dashboard.html', {'team_members': team_members})
            return JsonResponse({'success': True, 'html': html})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = TeamMemberForm()
    return render(request, 'dashboard/siteadmin_dashboard.html', {'form': form})


# Add and Save Testimonial
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            testimonials = Testimonial.objects.all()
            html = render_to_string('dashboard/siteadmin_dashboard.html', {'testimonials': testimonials})
            return JsonResponse({'success': True, 'html': html})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = TestimonialForm()
    return render(request, 'dashboard/siteadmin_dashboard.html', {'form': form})


# Add and Save FAQ
def add_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            faqs = FAQ.objects.all()
            html = render_to_string('dashboard/siteadmin_dashboard.html', {'faqs': faqs})
            return JsonResponse({'success': True, 'html': html})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = FAQForm()
    return render(request, 'dashboard/siteadmin_dashboard.html', {'form': form})


# Add and Save Booking
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            bookings = Booking.objects.all()
            html = render_to_string('dashboard/siteadmin_dashboard.html', {'bookings': bookings})
            return JsonResponse({'success': True, 'html': html})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = BookingForm()
    return render(request, 'dashboard/siteadmin_dashboard.html', {'form': form})


# Add and Save Payment
def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            payments = Payment.objects.all()
            html = render_to_string('dashboard/siteadmin_dashboard.html', {'payments': payments})
            return JsonResponse({'success': True, 'html': html})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = PaymentForm()
    return render(request, 'dashboard/siteadmin_dashboard.html', {'form': form})


# Add and Save Media File
def add_media(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            media_files = MediaFile.objects.all()
            html = render_to_string('dashboard/siteadmin_dashboard.html', {'media_files': media_files})
            return JsonResponse({'success': True, 'html': html})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = MediaFileForm()
    return render(request, 'dashboard/siteadmin_dashboard.html', {'form': form})

