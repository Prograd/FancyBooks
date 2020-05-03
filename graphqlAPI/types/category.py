from graphene_django import DjangoObjectType

from products.models.category import Category as CategoryModel


class Category(DjangoObjectType):
    class Meta:
        model = CategoryModel
