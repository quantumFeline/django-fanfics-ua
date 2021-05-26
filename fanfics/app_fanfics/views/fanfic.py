import datetime
import os.path

from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.core.files.base import ContentFile, File
import django.utils.timezone

from .contexts import get_login_context, get_fanfic_context
from ..models import Fanfic, Fandom, Author, Chapter

FILE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")


def add_fanfic_page(request):
    return render(request, "add_fanfic.html", get_login_context(request))


def fanfic_page(request, fanfic_id):
    context = get_fanfic_context(fanfic_id)
    context.update(get_login_context(request))
    context.update({
        'is_owner': context.get('fanfic').author.nickname == context['username']
    })
    return render(request, 'fanfic.html', context)


def publish(request):
    if request.method != 'POST':
        return HttpResponseForbidden('Publish with POST')
    title = request.POST.get('title')
    annotation = request.POST.get('annotation')
    author = get_object_or_404(Author, pk=get_login_context(request)['author_id'])

    fandoms = Fandom.objects.filter(name=request.POST.get('fandom'))
    if not fandoms:
        return HttpResponseBadRequest("Невідомий фандом")
    else:
        fandom = fandoms[0]

    fanfic = Fanfic(title=title,
                    author=author,
                    fandom=fandom,
                    annotation=annotation,
                    publication_date=datetime.date.today())
    fanfic.save()
    return HttpResponseRedirect(reverse('fics:fanfic_page', args=[fanfic.id]))


def publish_chapter(request, fanfic_id):
    if request.method != 'POST':
        return HttpResponseForbidden("Publish with POST")

    context = get_fanfic_context(fanfic_id)

    existing_chapters = context.get('chapter_list')
    if not existing_chapters:
        num = 1
    else:
        last = len(existing_chapters) - 1
        num = existing_chapters[last].chapter_number + 1

    title = request.POST.get('title')

    fic = context.get('fanfic')
    input_type = request.POST.get('input_type')
    if input_type == "file":
        file = request.FILES.get('chapter_file')

    elif input_type == "text":
        text = request.POST.get('chapter_text')
        # file_path = os.path.join(FILE_DIR, fic.title + "_" + str(num))
        file = File(text)
        # file_path = fic.title + "_" + str(num)
        # file_path, ContentFile(text)
    else:
        print("INPUT TYPE:", input_type)
        return HttpResponseBadRequest("Невідомий тип input")

    chapter = Chapter(fanfic=fic,
                      chapter_number=num,
                      chapter_title=title,
                      publication_date=datetime.date.today(),
                      text=file)
    chapter.save()

    return HttpResponseRedirect(reverse('fics:fanfic_page', args=[fic.id]))
