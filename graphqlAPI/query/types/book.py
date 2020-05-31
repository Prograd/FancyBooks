from graphene_django import DjangoObjectType

from products.models.book import Book as BookModel


class Book(DjangoObjectType):
    class Meta:
        model = BookModel
