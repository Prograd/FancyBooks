from functools import reduce

from django.test import TestCase

from billings.models.order import Order
from products.models.book import Book


class BillingGetBookIds(TestCase):

    def setUp(self):
        self.book_ids = []
        self.order = Order.objects.create()
        for i in range(3):
            book = Book.objects.create()
            self.order.add_book(book)
            self.book_ids.append(book.id)

    def test_should_return_book_ids_as_string(self):
        books_order_ids = self.order.books_ids()
        books_ids = str(reduce(lambda prev, id: str(prev) + ', ' + str(id), self.book_ids))
        self.assertEqual(books_order_ids, books_ids)

    def test_should_return_empty_sting(self):
        order = Order.objects.create()
        books_order_ids = order.books_ids()
        self.assertEqual(books_order_ids, '')
