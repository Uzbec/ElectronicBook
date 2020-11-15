from django.contrib import admin
from .models import book_inf, users_inf, userbook

admin.site.register(book_inf)
admin.site.register(users_inf)
admin.site.register(userbook)

