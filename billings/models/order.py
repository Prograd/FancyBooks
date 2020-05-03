from django.db import models
from django.db.models import Sum


class Order(models.Model):

    @property
    def order_price(self):
        return self.book_set.all().aggregate(Sum('price'))['price__sum']
