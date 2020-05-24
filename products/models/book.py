from django.db import models

from billings.models.order import Order
from products.models.category import Category


class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    publisher = models.CharField(max_length=50)
    published_date = models.DateField(null=True)
    description = models.CharField(max_length=300)
    page_count = models.IntegerField(null=True)
    thumbnail_url = models.CharField(max_length=300)
    language = models.CharField(max_length=10)
    authors = models.CharField(max_length=300)
    price = models.FloatField(default=0.00)
    categories = models.ManyToManyField(Category)
    orders = models.ForeignKey(Order, on_delete=models.DO_NOTHING, null=True)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.title
