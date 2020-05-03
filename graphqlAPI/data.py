from django.utils.datetime_safe import datetime

from products.models.book import Book
from products.models.category import Category


def initialize():
    test_category = Category.objects.create(name='test')
    for i in range(3):
        test_category.book_set.add(
            Book.objects.create(
                title='test book',
                subtitle='test sub',
                publisher='test',
                published_date=datetime.now(),
                description='test description',
                page_count=67 * i,
                thumbnail_url='https://test.test',
                language='en-gb',
                authors='test test',
                price=79.23 * i
            )
        )
