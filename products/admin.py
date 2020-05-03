from django.contrib import admin
from products.models.book import Book
from products.models.category import Category

admin.site.register(Category)
admin.site.register(Book)
