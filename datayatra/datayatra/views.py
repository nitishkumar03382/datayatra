from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate


def home(request):
  return render(request, "home.html")

def signup(request):
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
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})
