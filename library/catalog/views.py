from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    genre = Genre.objects.all()
    catalog = Catalog.objects.all()
    output = {
        "books": books,
        "authors": authors,
        "publishers": publishers,
        "genres": genre,
        "catalog": catalog
    }
    return render(request, "catalog/index.html", output)
