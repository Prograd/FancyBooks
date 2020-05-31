from django.contrib.auth import get_user_model
from django.test import TestCase

from billings.models.order import Order, OrderBook
from products.models.book import Book


class OrderModelTest(TestCase):

    def setUp(self):
        self.order = Order.objects.create()
        for amount in range(1, 4):
            OrderBook.objects.create(order=self.order, book=Book.objects.create(price=5.5), amount=amount)

    @staticmethod
    def create_test_user():
        user = get_user_model()(
            username='test',
            email='test',
        )
        user.save()
        return user

    def test_all_owned_when_admin(self):
        user = OrderModelTest.create_test_user()
        user.is_superuser = True
        owned_order = list(Order.all_owned(user))
        self.assertEqual(owned_order, [self.order])

    def test_all_owned_when_user_with_models(self):
        user = OrderModelTest.create_test_user()
        self.order.owner = user
        self.order.save()
        owned_order = list(Order.all_owned(user))
        self.assertEqual(owned_order, [self.order])

    def test_all_owned_when_user_without_models(self):
        user = OrderModelTest.create_test_user()
        owned_order = list(Order.all_owned(user))
        self.assertEqual(owned_order, [])
