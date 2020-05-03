from graphene import Mutation, List, Int, Field

from billings.models.utils.billing_util import BillingUtil
from graphqlAPI.types.billing import Billing


class BillingCreate(Mutation):
    class Arguments:
        book_ids = List(Int)

    billing = Field(Billing)

    def mutate(self, info, book_ids):
        return BillingCreate(billing=BillingUtil.create_billing(book_ids))
