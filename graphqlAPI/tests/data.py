from django.utils.datetime_safe import datetime

from billings.models.utils.billing_util import BillingUtil
from products.models.book import Book
from products.models.category import Category


def initialize():
    test_category = Category.objects.create(name='test')
    books_ids = []
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
        books_ids.append(book.id)
        test_category.book_set.add(
            book
        )
    BillingUtil.create_billing(books_ids)
