from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def add_fanfic_page(request):
    return render(request, "add_fanfic.html", {})


def publish(request):
    fanfic_title = request.POST['title']
    fanfic_fandom = request.POST['fandom']
    fanfic_text = request.POST['text']
    return HttpResponse("Hello!")