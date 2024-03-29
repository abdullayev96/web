from django.shortcuts import render, redirect
from .models import Author, Category, Book
from .forms import AuthorForm, CategoryForm, BookForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required





def login_required_decorator(func):
    return login_required(func, login_url='login_page')

def login_page(request):
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request, 'login.html')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')

@login_required_decorator
def home_page(request):
    return render(request, "index.html")

@login_required_decorator
def author_create(request):
    model = Author()
    form = AuthorForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("author_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "author/form.html", ctx)

@login_required_decorator
def author_list(request):
    authors = Author.objects.all()
    ctx = {
        "authors": authors
    }
    return render(request, "author/list.html", ctx)

@login_required_decorator
def author_edit(request, pk):
    model = Author.objects.get(pk=pk)
    form = AuthorForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("author_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "author/form.html", ctx)

@login_required_decorator
def author_delete(request, pk):
    model = Author.objects.get(pk=pk)
    model.delete()
    return redirect("author_list")


@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("category_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "category/form.html", ctx)

@login_required_decorator
def category_list(request):
    categories = Category.objects.all()
    ctx = {
        "categories": categories
    }
    return render(request, "category/list.html", ctx)

@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("category_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "category/form.html", ctx)

@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect("category_list")


@login_required_decorator
def book_create(request):
    model = Book()
    form = BookForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('book_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "book/form.html", ctx)

@login_required_decorator
def book_list(request):
    books = Book.objects.all()
    ctx = {
        "books": books
    }
    return render(request, "book/list.html", ctx)

@login_required_decorator
def book_edit(request, pk):
    model = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("book_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "book/form.html", ctx)

@login_required_decorator
def book_delete(request, pk):
    model = Book.objects.get(pk=pk)
    model.delete()
    return redirect("book_list")