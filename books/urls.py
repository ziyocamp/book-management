from django.urls import path

from .views import home_view, books_view, book_detail_view

app_name = "books"

urlpatterns = [
    path('', home_view, name='home_page'),
    path('books/', books_view, name='books_page'),
    path('books/<int:book_id>', book_detail_view, name='deatil'),
]
