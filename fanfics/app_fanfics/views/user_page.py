from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .login_context import get_login_context
from ..models import Fanfic, Fandom, Chapter


def add_fanfic_page(request):
    return render(request, "add_fanfic.html", get_login_context(request))


def publish(request):
    fanfic_title = request.POST['title']
    fanfic_fandom = Fandom.objects.filter(name=request.POST['fandom'])
    fanfic_text = request.POST['text']
    fanfic = Fanfic(title=fanfic_title, fandom=fanfic_fandom.id)
    fanfic.save()
    chapter = Chapter(fanfic=fanfic.id, text=fanfic_text)
    chapter.save()
    return HttpResponseRedirect(reverse('fics:index'))
