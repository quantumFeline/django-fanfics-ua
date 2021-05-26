import datetime

from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
import django.utils.timezone

from .login_context import get_login_context
from ..models import Fanfic, Fandom, Author


def add_fanfic_page(request):
    return render(request, "add_fanfic.html", get_login_context(request))


def publish(request):
    if request.method != 'POST':
        return HttpResponseForbidden('Register with POST')
    print(request.POST)
    fanfic_title = request.POST.get('title')
    print(request.POST.get('fandom'))
    fanfic_fandoms = Fandom.objects.filter(name=request.POST.get('fandom'))
    print(fanfic_fandoms)
    print(len(fanfic_fandoms))

    if fanfic_fandoms is None or len(fanfic_fandoms) == 0:
        return HttpResponseBadRequest("Невідомий фандом")
    else:
        fanfic_fandom = fanfic_fandoms[0]

    fanfic_annotation = request.POST.get('annotation')
    author = get_object_or_404(Author, pk=get_login_context(request)['author_id'])
    fanfic = Fanfic(title=fanfic_title,
                    author=author,
                    fandom=fanfic_fandom,
                    annotation=fanfic_annotation,
                    publication_date=datetime.date.today())
    fanfic.save()
    return HttpResponseRedirect(reverse('fics:fanfic_page', args=[fanfic.id]))


def publish_chapter(request):
    pass
