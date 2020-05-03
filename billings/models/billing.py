from django.db import models

from billings.models.order import Order


class Billing(models.Model):
    status = models.CharField(max_length=100)
    order = models.OneToOneField(
        Order,
        on_delete=models.DO_NOTHING,
        null=True
    )
