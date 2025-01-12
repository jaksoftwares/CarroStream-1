from django.shortcuts import render
from django.http import HttpResponse

# Basic view example
def index(request):
    return HttpResponse('Welcome to the feedback page!')
