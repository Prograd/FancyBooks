from billings.models.billing import Billing
from billings.models.order import Order
from products.models.book import Book


class BillingUtil:

    @staticmethod
    def create_billing(books_ids):
        order = Order.objects.create()
        for book_id in books_ids:
            order.book_set.add(Book.objects.get(id=book_id))
        order.save()
        return Billing.objects.create(status="created", order_id=order.id)
