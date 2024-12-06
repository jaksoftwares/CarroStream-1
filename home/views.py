from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'about/about.html', {'page_title': 'About Us'})

def services(request):
    return render(request, 'services/services.html', {'page_title': 'Services'})

def contact(request):
    return render(request, 'contact/contact.html', {'page_title': 'Contact-us'})

def faq(request):
    return render(request, 'faq/faq.html', {'page_title': 'Frequent Questions'})
def terms(request):
    return render(request, 'home/terms.html')