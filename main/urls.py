from django.urls import path,include, reverse
from . import views

urlpatterns = [
    path("", views.main_view, name="main"),
    path("book-create", views.create_book, name="form"),
    path("book/<int:book_id>", views.book_view, name="book_view"),
    path("book-delete/<int:book_id>", views.book_delete_view, name="book_delete"),
    path("book-list", views.book_list_view, name="book_list_view"),
]