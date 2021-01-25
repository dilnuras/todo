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

def add_book(request):
    form = request.POST
    book = form["book_text"]
    title = form["three.title"]
    sutitle = form["three.sutitle"]
    description = form["three.description"]
    price = form["three.price"]
    genre = form["three.genre"]
    author = form["three.author"]
    year = form ["three.year"]
    book = Book(title=title, sutitle=sutitle, description=description, price=price,genre=genre, author=author, year=year)
    book.save()
    return redirect(three)
