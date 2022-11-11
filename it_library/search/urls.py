from django.urls import path
from .views import *

urlpatterns = [
    path('', show_all_find_books, name='search_page'),
]