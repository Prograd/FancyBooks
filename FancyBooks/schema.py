from graphene_django import DjangoObjectType
import graphene
from graphene_django.debug import DjangoDebug

from products.models import Book as BookModel, Category as CategoryModel


class Category(DjangoObjectType):
    class Meta:
        model = CategoryModel


class Book(DjangoObjectType):
    class Meta:
        model = BookModel


class Query(graphene.ObjectType):
    books = graphene.List(Book)
    categories = graphene.List(Category)
    debug = graphene.Field(DjangoDebug, name='_debug')

    def resolve_books(self, info):
        return BookModel.objects.all()

    def resolve_categories(self, info):
        return CategoryModel.objects.all()


schema = graphene.Schema(query=Query)
