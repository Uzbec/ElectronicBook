from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
