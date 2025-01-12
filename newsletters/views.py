# views.py
from django.shortcuts import render

def compose_newsletter(request):
    return render(request, 'newsletters/newsletter.html')
