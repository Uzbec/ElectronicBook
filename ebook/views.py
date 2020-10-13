from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from ebook.models import users_inf
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, "login.html")


def registration(request):
    return render(request, "registration.html")


def reg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = UserCreationForm()
        return render(request, 'registration.html', {'form': form})
