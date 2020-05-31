from django.test import TestCase

from billings.models.order import Order, OrderBook
from products.models.book import Book


class OrderAddBookTest(TestCase):

    def test_should_add_book_with_certain_amount(self):
        order = Order.objects.create()
        book = Book.objects.create(price=5.25)
        amount = 2
        order.add_book(book=book, amount=amount)
        order_book = OrderBook.objects.get(book=book, order=order)
        self.assertEqual(order_book.amount, amount)

    def test_should_add_book_with_without_amount(self):
        order = Order.objects.create()
        book = Book.objects.create(price=5.25)
        order.add_book(book=book)
        order_book = OrderBook.objects.get(book=book, order=order)
        self.assertEqual(order_book.amount, 1)
