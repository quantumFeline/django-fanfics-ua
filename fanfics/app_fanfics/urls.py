from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fandoms',   views.fandom_list,     name='fandoms_list'),
    path('authors',   views.author_list,     name='authors_list'),
    path('author/<int:author_id>',   views.author_page,     name='author_page'),
    path('fanfic/<int:fanfic_id>',   views.fanfic_page,     name='fanfic_page'),
    path('chapter/<int:chapter_id>', views.chapter_reading, name='chapter_page'),
]

