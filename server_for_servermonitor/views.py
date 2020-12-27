from django.shortcuts import render
from django.http import JsonResponse
import psutil


def index(request):
    responseData = {
        'cpu': psutil.cpu_percent(interval=1),
        'ram': psutil.virtual_memory().percent,
        'hdd': psutil.disk_usage('/').percent,
    }
    return JsonResponse(responseData, status=200)
