from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('registration', views.registration, name="registration"),
    path('reg_user/', views.reg_user),
    path('userbooks/<int:userid>', views.userbooks, name='userbooks'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('libradmin/', views.libradmin, name='libradmin'),
    path('requestforaddbook', views.requestforaddbook,
         name='requestforaddbook'),
    path('managingbookslibr', views.managingbookslibr,
         name='managingbookslibr'),
    path('confirmaddbooktouser', views.confirmaddbooktouser,
         name='confirmaddbooktouser'),
    path('canceladdbooktouser', views.canceladdbooktouser,
         name='canceladdbooktouser'),
    path('libradmin/add_book/', views.add_book, name='add_book'),
    path('libradmin/delete_book/', views.delete_book, name='delete_book'),
    path('userbooks/downloadbook/', views.downloadbook, name='downloadbook'),
    path('search_results', views.search_results, name='search_results'),
]
