from django.shortcuts import render,HttpResponse
from .models import ToDo
from .models import Book


def homepage(request):
    return render(request,"index.html")


def test (request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def go (request):
    return render(request, "go.html") 

def second (request):
    return HttpResponse("test 2 page")

def three (request):
    book_list = Book.objects.all()
    return render(request, "book.html", {"book_list": book_list})