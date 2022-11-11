from django.urls import path
from .views import *

urlpatterns = [
    path('', show_all_books_view, name='show_all_books'),
    path('detail/<int:book_pk>/', show_book_detail_view, name='show_book_detail'),
    path('category/<int:category_pk>/', get_all_books_from_category_view, name='get_all_category'),
    path('author/<int:author_pk>/', get_author_detail_view, name='get_author_detail'),
]
