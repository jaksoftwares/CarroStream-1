from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Define login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to homepage or dashboard
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'accounts/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)  # Automatically log the user in after signup
            return redirect('home')  # Redirect to the homepage or dashboard
        except:
            messages.error(request, 'Error creating the account, please try again.')
            return redirect('signup')

    return render(request, 'accounts/signup.html')


