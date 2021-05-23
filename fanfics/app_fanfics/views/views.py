from django.shortcuts import render
from django.http import HttpResponse

from .oauth import GOOGLE_URL
from ..models import Fandom


def index(request):
    login = request.session.get('login')
    login_type = request.session.get('login_type')

    context = {
        'logged_in': login is not None,
        'username': f"{login_type}: {login}" if login_type else '',
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
