from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @staticmethod
    def all_owned(user):
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(owner=user).all()

    @property
    def order_price(self):
        return self.book_set.all().aggregate(Sum('price'))['price__sum']
