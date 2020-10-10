from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from ebook.models import users_inf
from django.views.generic.edit import FormView


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, "login.html")


def registration(request):
    return render(request, "registration.html")
