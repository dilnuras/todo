from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Book(models.Model):
    title = models.CharField(max_length=100)
    sutitle = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.DateTimeField(auto_now_add = False)
    published_at = models.DateTimeField(auto_now_add = True)
    is_favorite = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
   
