from django.db import models


class Language(models.Model):
    language = models.CharField(max_length=100)


class Catalog(models.Model):
    item = models.CharField(max_length=100)


class Genre(models.Model):
    genre = models.CharField(max_length=150)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)


class Author(models.Model):
    family = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    patronymic = models.CharField(max_length=100, null=True)


class Publisher(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.TextField()
    authors = models.ManyToManyField('Author', blank=True, related_name='AuthorsOfBook')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    year = models.IntegerField()
    description = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    paperback = models.IntegerField()
    article = models.CharField(max_length=20)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    image = models.FileField()
