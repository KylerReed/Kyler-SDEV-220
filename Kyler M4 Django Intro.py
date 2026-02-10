INSTALLED_APPS= [
    ...
    "library",
]

from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name
    

from django.contrib import admin
from .models import Book

admin.site.register(Book)
