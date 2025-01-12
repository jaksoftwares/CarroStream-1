from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if not name or not email or not message:
            messages.error(request, "Please fill in all required fields.")
            return redirect("contact")

        # Save the message to the database
        ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)
        messages.success(request, "Your message has been sent successfully.")
        return redirect("contact")

    return render(request, "contact/contact.html")
