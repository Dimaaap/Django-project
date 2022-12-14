from decimal import Decimal
from django.conf import settings
from books.models import Book


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        books_ids = self.cart.keys()
        books = Book.objects.filter(id__in=books_ids)

        cart = self.cart.copy()
        for book in books:
            cart[str(book.id)]['book'] = book

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']
            yield item

    def __len__(self):
        return len(self.cart.values())

    def add(self, book):
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'price': str(book.price)}
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, book):
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def total_count(self):
        return len([item for item in self.cart])

    def check_book_in_cart(self, book):
        book_id = str(book.id)
        return book_id in self.cart
