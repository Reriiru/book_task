from django.contrib import admin
from .models import Author, Book, Genre


class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'genre']


class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'pub_date', 'authors', 'genre']


class GenreAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
