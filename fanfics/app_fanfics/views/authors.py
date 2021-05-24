import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404

from .login_context import get_login_context
from ..models import Author, Fanfic


def author_page(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = get_login_context(request, {
        'author': author,
        'fanfic_list': Fanfic.objects.filter(author = author_id).order_by('title')
    })
    return render(request, 'author_page.html', context)


def author_list(request):
    context = get_login_context(request, {
        'authors_list': Author.objects.order_by('nickname')
    })

    print("author_list: context={}".format(context))
    return render(request, 'author_list.html', context)


def author_list_json(request):
    content = [author.nickname for author in list((Author.objects.order_by('nickname')))]
    body = json.dumps(content) + '\n'
    return HttpResponse(body, 'application/json')
