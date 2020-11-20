from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
import datetime
from django.utils import timezone


class users_inf(models.Model):
    STATUS_CHOICES = (
        ('ST', 'Ученик'),
        ('SADM', 'Администратор'),
        ('LIBR', 'Библиотекарь')
    )

    image = models.ImageField("Фотография профиля", blank=True,
                              upload_to="puples_photo",
                              default="puples_photo/default.png")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                                default='',
                                verbose_name="Связь с таблицей пользователей")
    date_of_birth = models.DateField(blank=True, null=True)
    status = models.CharField("Статуc", choices=STATUS_CHOICES, default='ST',
                              max_length=30)
    grade = models.IntegerField("Класс", default="-1")
    gardesymbol = models.CharField("Символ класса", max_length=1, default="-")

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
    addingDate = models.DateField("Дата добавления",
                                  default=timezone.now)
    bookfile = models.FileField(upload_to='books', blank=False,
                                default="puples_photo/default.png")

    def __str__(self):
        return self.bookname


class userbook(models.Model):
    CHOICES = (
        ('True', 'Подтверждено библиотекарем'),
        ('False', 'В обработке'),
        ('Refused', 'Отказано')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                default='',
                                verbose_name="Связь с таблицей пользователей")
    # booksid = models.CharField("id книги", max_length=30, default='')
    book = models.ForeignKey(book_inf, on_delete=models.CASCADE, null=True,
                                default='',
                                verbose_name="Связь с таблицей книг")
    status = models.CharField("Статуc", choices=CHOICES, default='False',
                              max_length=30)
    reqestdate = models.DateField("Дата добавления", default=timezone.now)
    getdate = models.DateField(default=timezone.now)
    enddate = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Book {} for user {}'.format(self.book.id, self.user.username)
