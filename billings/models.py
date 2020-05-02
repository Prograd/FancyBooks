from django.db import models
from django.db.models import Sum


class Order(models.Model):

    def order_price(self):
        return self.book_set.all().aggregate(Sum('price'))['price__sum']


class Billing(models.Model):
    status = models.CharField(max_length=100)
    order = models.OneToOneField(
        Order,
        on_delete=models.DO_NOTHING,
        null=True
    )
