from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from books.models import Book
from .cart import Cart


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.add(book=book)
    return redirect('cart:cart_detail')


def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book,  id=book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')


@login_required(login_url='/users/login')
def cart_detail(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart/detail.html', context)