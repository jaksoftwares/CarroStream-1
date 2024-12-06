from django.shortcuts import render
from django.http import HttpResponse

# Basic view example
def booking(request):
    return render(request, 'booking/booking.html')
