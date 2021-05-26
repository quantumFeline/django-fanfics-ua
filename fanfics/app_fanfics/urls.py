from django.urls import path
from .views import views, logins, oauth, authors, fanfic

app_name = 'fics'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration_page', logins.registration_page, name='registration_page'),

    path('register', logins.register_view, name='register'),
    path('authorize', logins.authorize_view, name='authorize'),
    path('logout', logins.logout_view, name='logout'),
    path('oauth2/callback', oauth.oauth_callback),

    path('api/author/index', authors.author_list_json),
    path('api/fandom/index', views.fandom_list_json),

    path('add_fanfic', fanfic.add_fanfic_page, name='add_fanfic'),
    path('publish', fanfic.publish, name='publish'),
    path('publish_chapter/<int:fanfic_id>', fanfic.publish_chapter, name='publish_chapter'),

    path('fandoms', views.fandom_list, name='fandoms_list'),
    path('authors', authors.author_list, name='authors_list'),
    path('author/<int:author_id>',   authors.author_page,     name='author_page'),
    path('fanfic/<int:fanfic_id>',   fanfic.fanfic_page,     name='fanfic_page'),
    path('chapter/<int:chapter_id>', views.chapter_reading, name='chapter_page'),
]

