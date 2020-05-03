from django.test import TestCase

from billings.models.utils.billing_util import BillingUtil
from products.models.book import Book


class BillingUtilTest(TestCase):

    def setUp(self):
        self.books_ids = []
        for i in range(3):
            self.books_ids.append(Book.objects.create().id)

    def test_should_create_order_and_billing(self):
        """
        It's should create order with given books ids
        and connect it with new billing
        """
        billing = BillingUtil.create_billing(self.books_ids)
        books_ids = list(map(lambda book: book.id, billing.order.book_set.all()))
        self.assertEqual(self.books_ids, books_ids)
