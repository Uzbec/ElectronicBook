from django.shortcuts import render
from django.utils import timezone


def index(request):
    return render(request, 'templates/index.html', {})


def login(request):
    return render(request, "templates/login.html")


def registration(request):
    return render(request, "templates/registration.html")
