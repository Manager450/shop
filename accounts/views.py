from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_backends
from .forms import SignupForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Explicitly set authentication backend
            backend = get_backends()[0]  # Get the first backend
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
            
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # The login field may be email or username, depending on your setup
            login_identifier = form.cleaned_data.get("login")
            password = form.cleaned_data.get("password")
            # Authenticate the user
            user = authenticate(request, username=login_identifier, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Adjust redirect as needed
            else:
                form.add_error(None, "Invalid credentials. Please try again.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})