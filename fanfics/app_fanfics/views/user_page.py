from django.shortcuts import render
from django.http import HttpResponse


def publish(request):
    return HttpResponse("Hello!")