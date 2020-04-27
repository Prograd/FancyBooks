from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    publisher = models.CharField(max_length=50)
    published_date = models.DateField()
    description = models.CharField(max_length=300)
    page_count = models.IntegerField()
    thumbnail_url = models.CharField(max_length=300)
    language = models.CharField(max_length=10)
    authors = models.CharField(max_length=300)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
