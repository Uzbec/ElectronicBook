from django.db import models


class Congratulation(models.Model):
    name = models.CharField("Имя", max_length=150)
    description = models.CharField("Поздравление", max_length=600)

    def __str__(self):
        return 'Поздравление от {}'.format(self.name)
