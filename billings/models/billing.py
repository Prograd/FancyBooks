from typing import List

from django.db import models

from billings.models.order import Order
from products.models.book import Book
from graphqlAPI.mutation.types.book_input import BookInput


class Billing(models.Model):
    status = models.CharField(max_length=100)
    order = models.OneToOneField(
        Order,
        on_delete=models.DO_NOTHING,
        null=True
    )

    @staticmethod
    def of_input(books: List[BookInput]):
        order = Order.objects.create()
        for book in books:
            order.add_book(Book.objects.get(id=book.id), amount=book.amount)
        order.save()
        return Billing.objects.create(status="created", order_id=order.id)
