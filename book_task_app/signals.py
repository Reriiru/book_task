from django.db.models.signals import pre_save
from .models import Book, Author, Genre


def check_genre(sender, instance, **kwargs):
    print(instance.__dict__, sender)
    pass


pre_save.connect(check_genre, sender=Book)
