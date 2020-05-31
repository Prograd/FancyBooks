from graphene import Mutation, List, Field

from graphqlAPI.mutation.types.billing import Billing
from billings.models.billing import Billing as BillingModel
from graphqlAPI.mutation.types.book_input import BookInput


class BillingCreate(Mutation):
    class Arguments:
        books = List(BookInput)

    billing = Field(Billing)

    @staticmethod
    def mutate(self, info, books):
        return BillingCreate(billing=BillingModel.of_input(books=books))
