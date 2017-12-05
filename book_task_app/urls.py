from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^authors/$', views.AuthorList.as_view(), name='authors'),
    url(r'^details/(?P<slug>.+)$', views.BookDetails.as_view(),
        name='book_details'),
    url(r'^$', views.BookList.as_view(), name='book_list'),
]
