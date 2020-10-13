from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from ebook.models import users_inf
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import book_inf, users_inf

# import time


def index(request):
    books = book_inf.objects.all()
    return render(request, 'index.html', {'books': books})


def login(request):
    return render(request, "login.html")


def registration(request):
    return render(request, "registration.html")


def reg_user(request):
    if request.method == "POST":
        # loginName = request.POST.get("loginN")
        email = request.POST.get("email")
        password = request.POST.get("password")
        firstName = request.POST.get("first_name")
        lastName = request.POST.get("last_name")
        birthday = request.POST.get("birthday")
        print(birthday)
        # Создайте пользователя и сохраните его в базе данных
        new_user = User.objects.create_user(
            username=email, email=email, password=password)
        # Обновите поля и сохраните их снова
        new_user.first_name = firstName
        new_user.last_name = lastName
        new_user.save()
        user_inf = users_inf.objects.create(user=new_user)
        user_inf.date_of_birth = birthday
        user_inf.save()
    return HttpResponseRedirect("/login/")
