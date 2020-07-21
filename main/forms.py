from django.forms import ModelForm
from .models import Book, Author

class MainForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "content",
            "title",
            "author",
            "picture"
            ]

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            "first_name",
            "last_name"
        ]