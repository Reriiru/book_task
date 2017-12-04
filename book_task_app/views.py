from django.views.generic import ListView
from book_task_app.models import Book, Author


class BookList(ListView):
    model = Book
    context_object_name = 'books'