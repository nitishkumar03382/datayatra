from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def home(request):
  return render(request, "home.html")
def custom_logout(request):
    print("Logging out user")
    logout(request)
    return redirect('home')  # redirect to home page after logout
def signup(request):
    if request.user.is_authenticated:
        print("User is already authenticated, redirecting to home")
        return redirect('home')
    if request.method == "POST":
        print("Received POST request for signup")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid, saving user")
            user = form.save()
            # form.save()
            login(request, user)
            return redirect('home')  # redirect to home page after signup
        else:
            print("Form is invalid. Errors:", form.errors)
            messages.error(request, form.errors.as_text())
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})
