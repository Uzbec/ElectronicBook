from django import template
from ebook.models import book_inf, users_inf, userbook
from django.contrib.auth.models import User

register = template.Library()


@register.simple_tag(name='if_include')
def if_include(bookid, userid):
    book = book_inf.objects.get(id=bookid)
    user = User.objects.get(id=userid)
    try:
        t = userbook.objects.get(user=user, book=book)
        #print(t)
        return True
    except userbook.DoesNotExist:
        # print("None")
        return False
