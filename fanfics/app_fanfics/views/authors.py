from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404

from ..models import Author


def author_page(request, author_id):

    author = get_object_or_404(Author, pk=author_id)
    return HttpResponse(f"The page of the author {author.nickname}")


def author_list(request):
    context = {
        'authors_list' : Author.objects.order_by('nickname')
    }
    return render(request, 'author_list.html', context)
