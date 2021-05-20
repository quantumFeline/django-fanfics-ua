from django.http import (HttpResponse, HttpResponseForbidden, HttpResponseRedirect)
from django.urls import reverse


def authorize(request):

    if request.method != 'POST':
        return HttpResponseForbidden('Authorize with POST')
    login = request.POST.get('login')
    password = request.POST.get('password')

    # XXX Hardcoded

    if login == 'user' and password == 'resu':
        request.session['login'] = 'user'
        request.session['login_type'] = 'local'
        return HttpResponseRedirect(reverse('fics:index'))

    text = 'Login failed. Form value: ' + repr(list(request.POST.items()))

    return HttpResponse(text)


def logout(request):
    request.session.pop('login', None)
    request.session.pop('login_type', None)
    return HttpResponseRedirect(reverse('fics:index'))
