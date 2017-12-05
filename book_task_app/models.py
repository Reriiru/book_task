from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.SlugField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
