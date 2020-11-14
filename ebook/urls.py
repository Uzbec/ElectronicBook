from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('registration', views.registration, name="registration"),
    path('reg_user/', views.reg_user),
    path('userbooks/<int:userid>', views.userbooks, name='userbooks'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('libradmin', views.libradmin, name='libradmin'),
]
