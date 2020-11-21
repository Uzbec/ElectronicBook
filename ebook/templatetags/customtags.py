from django import template
from ebook.models import book_inf, users_inf, userbook
from django.contrib.auth.models import User

register = template.Library()


@register.simple_tag
def if_include(bookid, userid):
    book = book_inf.objects.get(id=bookid)
    user = User.objects.get(id=userid)
    t = userbook.objects.get(user=user, book=book)
    print(t)
