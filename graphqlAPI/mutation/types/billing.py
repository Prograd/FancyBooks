from graphene_django import DjangoObjectType
from billings.models.billing import Billing as BillingModel


class Billing(DjangoObjectType):
    class Meta:
        model = BillingModel
