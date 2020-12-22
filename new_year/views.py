from django.shortcuts import render
from .models import Congratulation


def index(request):
    congratulations = Congratulation.objects.all()
    return render(request, 'new_year/index.html', {'congratulations': congratulations})
