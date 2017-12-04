from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BookList.as_view(), name='book_list'),
    url(r'^authors/$', views.AuthorList.as_view(), name='authors')
]