import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .login_context import get_login_context
from ..models import Fandom, Fanfic, Chapter


def index(request):
    return render(request, 'index.html', get_login_context(request))


def fanfic_page(request, fanfic_id):
    fanfic = get_object_or_404(Fanfic, pk=fanfic_id)
    context = {
        'fanfic': fanfic,
        'chapter_list': Chapter.objects.filter(fanfic=fanfic_id).order_by('chapter_title')
    }
    context.update(get_login_context(request))
    return render(request, 'fanfic.html', context)


def chapter_reading(request, chapter_id):
    return HttpResponse(f"The page of the chapter {chapter_id}")


def fandom_list(request):
    context = {
        'fandoms_list': Fandom.objects.order_by('name')
    }
    context.update(get_login_context(request))
    return render(request, 'fandom_list.html', context)


def fandom_list_json(request):
    content = [fandom.name for fandom in list((Fandom.objects.order_by('name')))]
    body = json.dumps(content) + '\n'
    return HttpResponse(body, 'application/json')


