from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login', views.login, name="login"),
    path('', include('django.contrib.auth.urls')),
    path('registration', views.registration, name="registration"),
    path('reg_user/', views.reg_user),
    path('userbooks/<int:userid>', views.userbooks, name='userbooks'),
]
