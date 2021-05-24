import datetime

from django.shortcuts import render

from ..models import User, Author
from django.contrib.auth import authenticate, login, logout
from django.http import (HttpResponse, HttpResponseForbidden, HttpResponseRedirect)
from django.urls import reverse


def registration_page(request):
    return render(request, 'register.html', {})


def register_view(request):
    if request.method != 'POST':
        return HttpResponseForbidden('Register with POST')
    username = request.POST.get('login')
    email = request.POST.get('email')
    password = request.POST.get('password')
    new_user = User.objects.create_user(username, email, password)
    new_user.save()
    new_author = Author(nickname=username, user=new_user, register_date=datetime.date.today())
    new_author.save()
    return HttpResponseRedirect(reverse('fics:index'))


def authorize_view(request):
    if request.method != 'POST':
        return HttpResponseForbidden('Authorize with POST')

    username = request.POST.get('login')
    password = request.POST.get('password')

    # user = User.objects.get(username=login)
    user = authenticate(request, username=username, password=password)
    if user is None:
        return HttpResponse("No such user registered.")
    login(request, user)
    return HttpResponseRedirect(reverse('fics:index'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('fics:index'))
