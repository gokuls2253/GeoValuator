from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from .models import Profile

def landing(request):
    return render(request, 'landing/landing.html')

def home(request):
    return render(request, 'landing/home.html')

def services(request):
    return render(request, 'landing/services.html')

def contact(request):
    return render(request, 'landing/contact.html')

def profile(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        context = {
            'username': request.user.username,
            'email': request.user.email,
            'phone_number': profile.phone_number,
            'bio': profile.bio,
            'location': profile.location,
        }
        return render(request, 'landing/profile.html', context)
    else:
        # Redirect to login or show both login and register options
        return render(request, 'landing/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Profile creation is handled by the signal
            login(request, user)  # Log the user in after registration
            messages.success(request, f'Account created successfully!')
            return redirect('profile')  # Redirect to the profile page
    else:
        form = UserRegisterForm()
    return render(request, 'landing/register.html', {'form': form})
