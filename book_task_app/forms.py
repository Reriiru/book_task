from django.forms import ModelForm
from book_task_app.models import Book
from django.core.exceptions import ValidationError


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'pub_date']

    def clean(self):
        if self._errors:
            return self.cleaned_data

        super(BookForm, self).clean()

        genre_set = set(
            self.cleaned_data.get('genre').values_list('id', flat=True)
            )

        for author in self.cleaned_data.get('author').all():
            author_set = set(author.genre.values_list('id', flat=True))
            
            if author_set != genre_set:
                raise ValidationError("This author can't write this sort of book",
                                      code="wrong_author")

        return self.cleaned_data
