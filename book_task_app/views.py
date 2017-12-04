from django.views.generic import ListView
from book_task_app.models import Book, Author
from django.utils.datastructures import MultiValueDictKeyError


class AuthorList(ListView):
    model = Author
    context_object_name = 'authors'
    paginate_by = 10


class BookList(ListView):
    model = Book
    context_object_name = 'books'
    ordering = ['-genre']
    paginate_by = 10

    def get_books_by_genre(self):
        genre = self.request.GET['genre']

        books_by_genre = Book.objects.filter(genre__name=genre)
        print(books_by_genre)

        return books_by_genre

    def get_books_by_author(self):
        author = self.request.GET['author']

        books_by_author = Book.objects.filter(author__name=author)
        print(books_by_author)

        return books_by_author

    def get_queryset(self):
        try:
            genre = self.request.GET['genre']
            author = self.request.GET['author']
        except MultiValueDictKeyError:
            return super(BookList, self).get_queryset()

        if genre == '':
            books_by_author = self.get_books_by_author()
            if books_by_author:
                return books_by_author
            else:
                return super(BookList, self).get_queryset()

        if author == '':
            books_by_genre = self.get_books_by_genre()
            if books_by_genre:
                return books_by_genre
            else:
                return super(BookList, self).get_queryset()

        queryset = self.get_books_by_author() & self.get_books_by_genre()
        return queryset
