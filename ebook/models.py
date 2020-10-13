from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class users_inf(models.Model):
    image = models.ImageField("Фотография профиля", blank=True,
                              upload_to="puples_photo",
                              default="puples_photo/default.png")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                                default='',
                                verbose_name="Связь с таблицей пользователей")
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class book_inf(models.Model):
    bookname = models.CharField("назвние книги", null=True, max_length=150)
    author = models.CharField("автор", null=True, max_length=100)
    rate = models.PositiveIntegerField("Рейтинг книги", default=0,
                                       validators=[MaxValueValidator(5), ])
    discriptions = models.TextField("описание книги")
    bookimage = models.ImageField("Фотография книги", blank=True,
                              upload_to="books_photo",
                              default="books_photo/default.png")

    def __str__(self):
        return self.bookname
