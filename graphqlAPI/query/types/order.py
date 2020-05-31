import graphene
from graphene_django import DjangoObjectType

from billings.models.order import Order as OrderModel


class Order(DjangoObjectType):
    class Meta:
        model = OrderModel

    order_price = graphene.Field(graphene.Float)

    def resolve_order_price(self, info):
        return self.order_price
