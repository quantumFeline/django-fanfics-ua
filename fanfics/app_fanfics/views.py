from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Author, Fandom


def index(request):
    login = request.session.get('login')
    login_type = request.session.get('login_type')

    context = {
        'logged_in': login is not None,
        'username': f"{login_type}: {login}" if login_type else ''}
    return render(request, 'index.html', context)


def author_page(request, author_id):

    author = get_object_or_404(Author, pk=author_id)
    return HttpResponse(f"The page of the author {author.nickname}")


def fanfic_page(request, fanfic_id):
    return HttpResponse(f"The page of the fanfic {fanfic_id} by {fanfic_id}")


def chapter_reading(request, chapter_id):
    return HttpResponse(f"The page of the chapter {chapter_id}")


def fandom_list(request):
    context = {
        'fandoms_list' : Fandom.objects.order_by('name')
    }
    return render(request, 'fandom_list.html', context)


def author_list(request):
    context = {
        'authors_list' : Author.objects.order_by('nickname')
    }
    return render(request, 'author_list.html', context)
