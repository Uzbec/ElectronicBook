from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class users_inf(models.Model):
    name = models.CharField("Имя", null=True, max_length=50)
    surname = models.CharField("Фамилия", null=True, max_length=100)
    image = models.ImageField("Фотография профиля", blank=True,
                              upload_to="puples_photo",
                              default="puples_photo/default.png")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                                default='',
                                verbose_name="Связь с таблицей пользователей")
    cal = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class book_inf(models.Model):
    bookname = models.CharField("назвние книги", null=True, max_length=150)
    author = models.CharField("автор", null=True, max_length=100)
    rate = models.PositiveIntegerField("Рейтинг книги", default=0,
                                       validators=[MaxValueValidator(5), ])
    discriptions = models.TextField("описание книги")
    bookimage = models.ImageField("Фотография книги", blank=True,
                              upload_to="puples_photo",
                              default="puples_photo/default.png")

    def __str__(self):
        return self.bookname
