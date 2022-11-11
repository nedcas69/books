from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length = 255)
    author_name = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True )

    def __str__(self):
        return f'Id {self.id}: {self.name} -- {self.author_name}'