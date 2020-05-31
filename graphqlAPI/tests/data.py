from django.utils.datetime_safe import datetime

from billings.models.billing import Billing
from billings.models.order import Order
from products.models.book import Book
from products.models.category import Category


def initialize():
    test_category = Category.objects.create(name='test')
    order = Order.objects.create()
    for i in range(3):
        book = Book.objects.create(
            id=i + 1,
            title='test book',
            subtitle='test sub',
            publisher='test',
            published_date=datetime.strptime("2019-12-12", "%Y-%m-%d").date(),
            description='test description',
            page_count=67 * i,
            thumbnail_url='https://test.test',
            language='en-gb',
            authors='test test',
            price=79.23 * i
        )
        order.add_book(book=book)
        test_category.book_set.add(
            book
        )

    Billing.objects.create(
        status="Created",
        order=order
    )
