from django.test import TestCase

from billings.models.order import Order
from products.models.book import Book


class OrderModelTest(TestCase):

    def test_should_sum_price_in_order(self):
        order = Order.objects.create()
        for book in range(3):
            order.book_set.add(Book.objects.create(price=5.25))
        self.assertEqual(order.order_price, 15.75)
