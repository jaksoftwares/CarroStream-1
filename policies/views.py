from django.shortcuts import render
from django.http import HttpResponse

# Basic view example
def policies(request):
    return render(request, 'policies/policies.html')
