from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .models import book_inf, users_inf, userbook


# import time
# TODO:кнопка добавить
# TODO:В libradmin add_book/
# TODO:В libradmin delete_book/
# TODO:В managingbookslibr confirmaddbooktouser?bookid={{bookItem.id}}&userid={{user.id}}
# TODO:В managingbookslibr canceladdbooktouser?bookid={{bookItem.id}}
# TODO:В userbooks downloadbook?bookid={{bookItem.id}}


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


def userbooks(request, userid):
    user = User.objects.get(id=userid)
    books = userbook.objects.filter(user=user)
    return render(request, 'userbooks.html', {'books': books, 'user': user})


def userprofile(request):
    return render(request, 'userprofile.html')


def libradmin(request):
    books = book_inf.objects.all()
    return render(request, 'libradmin.html', {'books': books})


def requestforaddbook(request):
    userid = request.GET.get("userid", "")
    bookid = request.GET.get("bookid", "")
    user = User.objects.get(id=userid)
    book = book_inf.objects.get(id=bookid)
    new_book = userbook.objects.create(user=user)
    new_book.book = book
    new_book.save()
    print("sucscess add")
    print(request.GET.get("bookid", ""))
    print(request.GET.get("userid", ""))
    # return render(request, 'index.html')
    return HttpResponseRedirect("/")


def managingbookslibr(request):
    books = userbook.objects.filter(status="False")
    return render(request, 'managingbookslibr.html', {'books': books})


def confirmaddbooktouser(request):
    userid = request.GET.get("userid", "")
    bookid = request.GET.get("bookid", "")
    user = User.objects.get(id=userid)
    confirmedbook = userbook(user=user, booksid=bookid, status="True")
    confirmedbook.save()
    books = userbook.objects.filter(status="False")
    # return render(request, 'managingbookslibr.html', {'books': books})
    return HttpResponseRedirect("/managingbookslibr/")


def canceladdbooktouser(request):
    userid = request.GET.get("userid", "")
    bookid = request.GET.get("bookid", "")
    user = User.objects.get(id=userid)
    confirmedbook = userbook(user=user, booksid=bookid, status="Refused")
    confirmedbook.save()
    books = userbook.objects.filter(status="False")
    # return render(request, 'managingbookslibr.html', {'books': books})
    return HttpResponseRedirect("/managingbookslibr/")


def add_book(request):
    Bookname = request.POST.get("Bookname")
    Bookauthor = request.POST.get("Bookauthor")
    discriptions = request.POST.get("discriptions")
    bookimg = request.FILES["bookimg"]
    bookfile = request.POST.get("bookfile")
    newbook = book_inf.objects.create(bookname=Bookname)
    newbook.author = Bookauthor
    newbook.discriptions = discriptions
    newbook.bookimage = bookimg
    newbook.bookfile = bookfile
    newbook.save()
    # return render(request, 'libradmin.html')
    return HttpResponseRedirect("/libradmin/")


def delete_book(request):
    pass