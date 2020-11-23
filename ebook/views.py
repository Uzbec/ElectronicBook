from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.db.models import Q
from .models import book_inf, users_inf, userbook
import os


def index(request):
    books = book_inf.objects.all().order_by('?')
    newbooks = book_inf.objects.all().order_by('-addingDate')
    userbooks = userbook.objects.all()
    return render(request, 'index.html',
                  {'books': books, 'newbooks': newbooks, 'userbooks': userbooks})


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
    books = userbook.objects.filter(user=user, status="True")
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
    book = book_inf.objects.get(id=bookid)
    confirmedbook = userbook.objects.get(user=user, book=book)
    confirmedbook.status = 'True'
    confirmedbook.save()
    # books = userbook.objects.filter(status="False")
    # return render(request, 'managingbookslibr.html', {'books': books})
    return HttpResponseRedirect("/managingbookslibr")


def canceladdbooktouser(request):
    userid = request.GET.get("userid", "")
    bookid = request.GET.get("bookid", "")
    user = User.objects.get(id=userid)
    book = book_inf.objects.get(id=bookid)
    confirmedbook = userbook.objects.get(user=user, book=book)
    confirmedbook.delete()
    return HttpResponseRedirect("/managingbookslibr")


def add_book(request):
    Bookname = request.POST.get("Bookname")
    Bookauthor = request.POST.get("Bookauthor")
    discriptions = request.POST.get("discriptions")
    bookimg = request.FILES["bookimg"]
    # print(bookimg)
    bookfile = request.FILES["bookfile"]
    newbook = book_inf.objects.create(bookname=Bookname)
    newbook.author = Bookauthor
    newbook.discriptions = discriptions
    newbook.bookimage = bookimg
    newbook.bookfile = bookfile
    newbook.save()
    # return render(request, 'libradmin.html')
    return HttpResponseRedirect("/libradmin/")


def delete_book(request):
    bookid = request.POST.get("Bookid")
    print(bookid)
    book = book_inf.objects.get(id=bookid)
    delbook = book_inf.objects.get(bookname=book)
    delbook.delete()
    return HttpResponseRedirect("/libradmin/")


def downloadbook(request):
    bookid = request.GET.get("bookid", "")
    book = book_inf.objects.get(id=bookid)
    ebook = book.bookfile
    print(str(ebook))
    with open(f"media/{ebook}", 'rb') as fh:
        response = HttpResponse(content_type="application/octet-stream")
        response[
            'Content-Disposition'] = 'attachment; filename=' + os.path.basename(
            f"media/{ebook}")
        response.write(fh.read())
    return response


def search_results(request):
    query = request.GET.get("q", "")
    books = book_inf.objects.filter(Q(bookname__icontains=query) | Q(author__icontains=query) | Q(discriptions__icontains=query))
    return render(request, 'search_results.html', {'books': books})


def book(request, bookid):
    book = book_inf.objects.get(id=bookid)
    n = 5
    return render(request, 'book.html', {'book': book, 'rate': int(book.rate), 'kolstars': range(n)})
