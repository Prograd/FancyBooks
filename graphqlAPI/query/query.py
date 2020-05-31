import graphene

from graphqlAPI.query.types.book import Book
from graphqlAPI.query.types.category import Category
from graphqlAPI.query.types.order import Order

from products.models.book import Book as BookModel
from products.models.category import Category as CategoryModel

from billings.models.order import Order as OrderModel


class Query(graphene.ObjectType):
    books = graphene.List(Book)
    categories = graphene.List(Category)
    orders = graphene.List(Order)

    def resolve_books(self, info):
        return BookModel.objects.all()

    def resolve_categories(self, info):
        return CategoryModel.objects.all()

    def resolve_orders(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        return OrderModel.objects.all()
