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

def book (request):
    book_list = Book.objects.all()
    return render(request, "book.html", {"book_list": book_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    title = form["book_text"]
    subtitle = form["subtitle"]
    description = form["description"]
    price = form["price"]
    genre = form["genre"]
    author = form["author"]
    year = form ["year"]
    todo = Book(title=title, sutitle=subtitle, description=description, price=price,genre=genre, author=author, year=year)
    todo.save()
    return redirect(book)

def delete_book(request, id):
    books = Book.objects.get(id=id)
    books.delete()
    return redirect(book)
    
def mark_book(request, id):
    books = Book.objects.get(id=id)
    books.is_favorite = not books.is_favorite
    books.save()
    return redirect(book)

def close_book(request, id):
    books =  Book.objects.get(id=id)
    books.is_closed = not books.is_closed
    books.save()
    return redirect(book)

