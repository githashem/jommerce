from django.shortcuts import render, redirect
from django.conf import settings
from .forms import LoginForm, SignupForm
from .models import User


def login(request):
    if hasattr(request, "user") and request.user.is_authenticated:
        return redirect(settings.AUTH_LOGIN_REDIRECT_URL)
    if request.method == "POST":
        return redirect(settings.AUTH_LOGIN_REDIRECT_URL)
    return render(request, "auth/login.html", context={"form": LoginForm()})


def logout(request):
    if hasattr(request, "user"):
        if settings.AUTH_LOGOUT_REDIRECT_URL:
            return redirect(settings.AUTH_LOGOUT_REDIRECT_URL)
    if request.method == "POST":
        return redirect(settings.AUTH_LOGOUT_REDIRECT_URL)
    return render(request, "auth/logout.html")


def signup(request):
    if hasattr(request, "user") and request.user.is_authenticated:
        return redirect(settings.AUTH_SIGNUP_REDIRECT_URL)
    if request.method == "POST":
        User.objects.create(email=request.POST["email"], password=request.POST["password"])
        return redirect(settings.AUTH_SIGNUP_REDIRECT_URL)
    return render(request, "auth/signup.html", context={"form": SignupForm()})
