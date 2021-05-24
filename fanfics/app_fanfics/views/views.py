import json
from django.shortcuts import render
from django.http import HttpResponse

from .oauth import GOOGLE_URL
from ..models import Fandom


def index(request):
    print(dir(request.user))

    context = {
        'logged_in': request.user.is_authenticated,
        'username': request.user.username,
        # 'author': Author.objects.filter(autho) if login_type else '',
        'google_url': GOOGLE_URL}
    return render(request, 'index.html', context)


def fanfic_page(request, fanfic_id):
    return HttpResponse(f"The page of the fanfic {fanfic_id} by {fanfic_id}")


def chapter_reading(request, chapter_id):
    return HttpResponse(f"The page of the chapter {chapter_id}")


def fandom_list(request):
    context = {
        'fandoms_list' : Fandom.objects.order_by('name')
    }
    return render(request, 'fandom_list.html', context)


def fandom_list_json(request):
    content = [fandom.name for fandom in list((Fandom.objects.order_by('name')))]
    body = json.dumps(content) + '\n'
    return HttpResponse(body, 'application/json')