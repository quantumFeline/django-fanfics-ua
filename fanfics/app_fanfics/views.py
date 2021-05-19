from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Author


def index(request):
    template = loader.get_template('index.html')
    return render(request, 'index.html', {})


def author_page(request, author_id):

    author = get_object_or_404(Author, pk=author_id)
    return HttpResponse(f"The page of the author {author.nickname}")


def fanfic_page(request, fanfic_id):
    return HttpResponse(f"The page of the fanfic {fanfic_id} by {fanfic_id}")


def chapter_reading(request, chapter_id):
    return HttpResponse(f"The page of the chapter {chapter_id}")


def fandom_list(request):
    return HttpResponse("List of fandoms")


def author_list(request):
    context = {
        'authors_list' : Author.objects.order_by('nickname')
    }
    return render(request, 'author_page.html', context)
