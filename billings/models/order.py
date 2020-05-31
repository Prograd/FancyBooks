from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, F

from products.models.book import Book


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    books = models.ManyToManyField(Book, through='OrderBook')

    @staticmethod
    def all_owned(user):
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(owner=user).all()

    def add_book(self, book, amount=None):
        if amount is None:
            amount = 1
        OrderBook.objects.create(order=self, book=book, amount=amount)

    @property
    def order_price(self):
        return OrderBook.objects.filter(order=self).annotate(
            price=models.ExpressionWrapper((F('book__price') * F('amount')),
                                           output_field=models.FloatField())).aggregate(Sum('price'))['price__sum']


class OrderBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, null=True)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, null=True)
    amount = models.IntegerField(default=1)
