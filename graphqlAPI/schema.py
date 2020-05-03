import graphene
from graphene_django.debug import DjangoDebug

from graphqlAPI.mutations.billing_create import BillingCreate
from graphqlAPI.types.book import Book
from graphqlAPI.types.category import Category
from graphqlAPI.types.order import Order
from products.models.book import Book as BookModel
from products.models.category import Category as CategoryModel
from billings.models.order import Order as OrderModel


class Mutation(graphene.ObjectType):
    create_billing = BillingCreate.Field()


class Query(graphene.ObjectType):
    books = graphene.List(Book)
    categories = graphene.List(Category)
    orders = graphene.List(Order)
    debug = graphene.Field(DjangoDebug, name='_debug')

    def resolve_books(self, info):
        return BookModel.objects.all()

    def resolve_categories(self, info):
        return CategoryModel.objects.all()

    def resolve_orders(self, info):
        return OrderModel.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)
