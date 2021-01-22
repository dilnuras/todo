from django.shortcuts import render,HttpResponse, redirect
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

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)
