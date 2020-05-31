from unittest.mock import MagicMock

from django.test import TestCase

from billings.models.billing import Billing
from graphqlAPI.mutation.types.book_input import BookInput
from products.models.book import Book


class BillingOfInputTest(TestCase):

    def setUp(self):
        self.books_inputs = []
        for i in range(3):
            book = Book.objects.create()
            book_input = BookInput()
            book_input.id = book.id
            book_input.amount = i
            self.books_inputs.append(book)

    def test_should_create_order_and_billing_from_input(self):
        """
        It's should create order with given books ids
        and connect it with new billing
        """
        billing = Billing.of_input(self.books_inputs)
        books_order_ids = list(map(lambda book: book.id, billing.order.books.all()))
        books_ids = list(map(lambda book_input: book_input.id, self.books_inputs))
        self.assertEqual(books_ids, books_order_ids)
