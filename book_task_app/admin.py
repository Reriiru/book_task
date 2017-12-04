from django.contrib import admin
from .models import Author, Book, Genre
from .forms import BookForm


class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'genre']


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    fields = ['title', 'pub_date', 'author', 'genre']


class GenreAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
