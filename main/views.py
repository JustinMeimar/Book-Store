from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from .models import Book, Author
from .forms import MainForm, AuthorForm
# Create your views here.

def main_view(request):
    books= Book.objects.all()
    
    return render(request, "main/index.html", {
        "books":books
    })

def book_view(request, book_id, *args, **kwargs):
    try:
        book = Book.objects.get(id=book_id)
        return render(request, "main/bookview.html", {
            "content":book.content,
            "title":book.title,
            "author":book.author
        })
    except:
        return HttpResponse("No book found")

def create_book(request):
    author_form = AuthorForm
    form = MainForm()
    if request.method == "POST":
        if "book_form" in request.POST: 
            form = MainForm(request.POST)
            if form.is_valid():
                form.save()        
                form = MainForm()
        if "author_form" in request.POST:
            author_form = AuthorForm(request.POST)
            if author_form.is_valid():
                author_form.save()
                author_form = AuthorForm

    return render(request, "main/createbook.html", {
        "form":form,
        "author_form":author_form
    })

def book_list_view(request, *args, **kwargs):
    qs = Book.objects.all()
    tweet_list = [{"id":i.id, "content":i.content} for i in qs]
    data = {
        "isUser":False,
        "response":tweet_list
    }
    
    return JsonResponse(data)

def book_delete_view(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect(reverse("main"))

