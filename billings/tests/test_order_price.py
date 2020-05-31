from django.test import TestCase

from billings.models.order import Order, OrderBook
from products.models.book import Book


class OrderPriceTest(TestCase):

    def test_should_sum_price_in_order(self):
        order = Order.objects.create()
        for amount in range(1, 4):
            OrderBook.objects.create(order=order, book=Book.objects.create(price=5.5), amount=amount)
        self.assertEqual(order.order_price, 33)
