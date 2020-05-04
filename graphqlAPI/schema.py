import graphene
import graphql_jwt
from graphene_django.debug import DjangoDebug

from graphqlAPI.mutations.billing_create import BillingCreate
from graphqlAPI.mutations.user_create import CreateUser
from graphqlAPI.types.book import Book
from graphqlAPI.types.category import Category
from graphqlAPI.types.order import Order
from products.models.book import Book as BookModel
from products.models.category import Category as CategoryModel
from billings.models.order import Order as OrderModel


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_billing = BillingCreate.Field()
    create_user = CreateUser.Field()


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
