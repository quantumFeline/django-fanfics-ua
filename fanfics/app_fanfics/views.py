from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")


def author_page(request, author_id):
    return HttpResponse(f"The page of the author {author_id}")


def fanfic_page(request, fanfic_id):
    return HttpResponse(f"The page of the fanfic {fanfic_id} by {fanfic_id}")


def chapter_reading(request, chapter_id):
    return HttpResponse(f"The page of the chapter {chapter_id}")


def fandom_list(request):
    return HttpResponse("List of fandoms")


def author_list(request):
    return HttpResponse("List of authors")
