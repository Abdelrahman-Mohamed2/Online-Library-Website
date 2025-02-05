from django.db import models
from adm.models import Book

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=100)
    isadmin  = models.BooleanField()
    borrowed_books = models.ManyToManyField('adm.Book', related_name='borrowers', blank=True)
    def __str__(self):
        return self.username
