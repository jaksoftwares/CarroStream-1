from django.shortcuts import render
from django.http import HttpResponse

# Basic view example
def blog(request):
    return render(request, 'blog/blog.html')

def news_letter(request):
    return render(request, 'blog/compose-newsletter.html')
