from django.shortcuts import render
from django.db.models import Count

from .services import *
from .models import Book, Category, Author
from cart.cart import Cart


def show_all_books_view(request):
    all_books = get_all_objects_from_db_service(Book).prefetch_related('categories', 'authors')
    count_books = get_all_objects_from_db_service(Book).count
    page_obj = get_pagination_service(request, all_books, 10)
    count_books_in_categories = annotate_models_service(Category, Count, 'book').order_by('-book__count')
    context = {'books': all_books, 'count_books': count_books, 'page_obj': page_obj,
               'count_books_in_categories': count_books_in_categories}
    return render(request, 'books/show_all_books.html', context)


def show_book_detail_view(request, book_pk):
    book = get_objects_from_model_by_filter_service(Book, 'pk', book_pk)
    cart = Cart(request)
    book_in_cart = cart.check_book_in_cart(book)
    context = {'book': book, 'book_in_cart': book_in_cart}
    return render(request, 'books/show_book_detail.html', context)


def get_all_books_from_category_view(request, category_pk):
    category = get_objects_from_model_by_filter_service(Category, 'pk', category_pk)
    all_books_from_category = filter_objects_from_db_service \
        (Book, 'categories__pk', category_pk).prefetch_related('categories', 'authors')

    context = {'category': category, 'all_books_from_category': all_books_from_category,
               'title': f'Категорія - {category.title}'}
    return render(request, 'books/get_all_books_from_category.html', context)


def get_author_detail_view(request, author_pk):
    author = get_objects_from_model_by_filter_service(Author, 'pk', author_pk)
    all_author_books = filter_objects_from_db_service(Book, 'authors__pk', author_pk). \
        prefetch_related('categories')
    context = {'title': f'Автор - {author.fullname}', 'author': author,
               'all_author_books': all_author_books}
    return render(request, 'books/get_author_detail.html', context)
