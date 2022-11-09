from django.db import models


class Book(models.Model):
    name = models.CharField(max_length = 255)
    author_name = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)


    def __str__(self):
        return f'Id {self.id}: {self.name} -- {self.author_name}'