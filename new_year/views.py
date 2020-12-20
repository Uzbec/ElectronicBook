from django.shortcuts import render


def index(request):
    return render(request, 'new_year/index.html')
