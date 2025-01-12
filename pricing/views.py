from django.shortcuts import render
from django.http import HttpResponse

# Basic view example
def pricing(request):
    return render(request, 'pricing/pricing.html')
