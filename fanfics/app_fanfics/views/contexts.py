from .oauth import GOOGLE_URL
from ..models import Author, Fanfic, Chapter
from django.shortcuts import get_object_or_404


def get_login_context(request, base_context: dict = None):

    logged_in = request.user.is_authenticated

    if logged_in:
        username = request.user.username
        author_ids = Author.objects.filter(nickname=username)
        print("AUTHOR IDS:", author_ids)
        author_id = author_ids[0].id if author_ids else None

    else:
        username = None
        author_id = None

    auth_context = {
        'logged_in': request.user.is_authenticated,
        'username': username,
        'author_id': author_id,
        'google_url': GOOGLE_URL}

    if base_context:
        context = base_context
        base_context.update(auth_context)
        return context

    return auth_context


def get_fanfic_context(fanfic_id):
    fanfic = get_object_or_404(Fanfic, pk=fanfic_id)
    return {
        'fanfic': fanfic,
        'chapter_list': Chapter.objects.filter(fanfic=fanfic_id).order_by('chapter_title')
    }