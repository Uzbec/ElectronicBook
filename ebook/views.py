from django.shortcuts import render
from django.utils import timezone


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, "login.html")


def registration(request):
    return render(request, "registration.html")
