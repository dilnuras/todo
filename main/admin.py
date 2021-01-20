from django.contrib import admin
from .models import ToDo


admin.site.register(ToDo)

from .models import Book


admin.site.register(Book)