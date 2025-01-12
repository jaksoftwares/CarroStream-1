from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.encoding import force_bytes
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile  # Import the UserProfile model

User = get_user_model()


class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'  # Specify your custom template
    email_template_name = 'accounts/password_reset_email.html'  # Custom email template (optional)
    subject_template_name = 'accounts/password_reset_subject.txt'  # Custom subject for the email (optional)
    success_url = reverse_lazy('password_reset_done')  # Where to redirect after successful password reset request

def get_image_dimensions(image_file):
    """Function to get image dimensions (width, height)"""
    try:
        # Open the image using Pillow
        with Image.open(image_file) as img:
            return img.size  # Returns a tuple (width, height)
    except Exception as e:
        raise ValueError("Unable to retrieve image dimensions") from e
# login logic
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        # Debugging to see if user was authenticated
        if user is not None:
            print("User authenticated successfully")
            login(request, user)
            return redirect(reverse('dashboard:user_dashboard'))
        else:
            print("Authentication failed")
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login') 

    return render(request, 'accounts/login.html')


# def dashboard(request):
#     return render(request, 'dashboard/dashboard.html')


#signup logic
def signup_view(request):
    if request.method == 'POST':
        # Collect data from form
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        profile_picture = request.FILES.get('profile_picture')

        # Check if passwords match
        if password != password_confirm:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('signup')

        try:
            # Create the user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                full_name=full_name
            )

            # Success message
            messages.success(request, 'Account created successfully!')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('signup')

    return render(request, 'accounts/signup.html')



def activate_account(request, uidb64, token):
    try:
        # Decode the user ID from the URL
        uid = urlsafe_base64_decode(uidb64).decode('utf-8')
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    # Validate the token
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True  # Activate the user's account
        user.save()
        messages.success(request, 'Your account has been activated successfully. You can now log in.')
        return redirect('login')  # Redirect to login page
    else:
        messages.error(request, 'The activation link is invalid or has expired.')
        return redirect('signup')  # Redirect to signup page

def forgot_password(request):
    return render(request, 'accounts/password_reset.html')



def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            users = User.objects.filter(email=email)
            
            if not users.exists():
                # Add error message if email does not exist in the system
                messages.error(request, "The email address you entered is not associated with any account.")
                return redirect('password_reset')

            for user in users:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                # Get the current site domain
                site = get_current_site(request)
                domain = site.domain

                # Generate password reset URL
                reset_link = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
                reset_url = f"http://{domain}{reset_link}"

                # Send password reset email
                subject = "Password Reset Request"
                message = render_to_string('accounts/password_reset_email.html', {
                    'user': user,
                    'reset_url': reset_url,
                })
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
            
            return redirect('password_reset_done')

    else:
        form = PasswordResetForm()

    return render(request, 'accounts/password_reset.html', {'form': form})


def password_reset_done(request):
    return render(request, 'accounts/password_reset_done.html')


