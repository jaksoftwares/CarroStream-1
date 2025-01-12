from django.shortcuts import render
from services.models import Service
from .models import Testimonial

def home(request):
    testimonials = Testimonial.objects.all()
    context={
        'testimonials': testimonials,
    }
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'about/about.html', {'page_title': 'About Us'})

def services(request):
    return render(request, 'services/services.html', {'page_title': 'Services'})
def services_page(request):
    services = Service.objects.all()  # Fetch all services from the database
    context = {
        'page_title': 'Services', 
        'services': services        }
    return render(request, 'services/services.html', context)

def contact(request):
    return render(request, 'contact/contact.html', {'page_title': 'Contact-us'})

def faq(request):
    return render(request, 'faq/faq.html', {'page_title': 'Frequent Questions'})
def terms(request):
    return render(request, 'home/terms.html')