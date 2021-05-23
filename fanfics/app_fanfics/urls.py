from django.urls import path
from .views import views, logins, oauth, authors, user_page

app_name = 'fics'
urlpatterns = [
    path('', views.index, name='index'),

    path('register', logins.register, name='register'),
    path('authorize', logins.authorize, name='authorize'),
    path('logout', logins.logout, name='logout'),
    path('oauth2/callback', oauth.oauth_callback),

    path('fandoms',   views.fandom_list,     name='fandoms_list'),
    path('api/author/index', authors.author_list_json),
    path('authors',   authors.author_list,     name='authors_list'),
    path('publish', user_page.publish, name='publish'),
    path('author/<int:author_id>',   authors.author_page,     name='author_page'),
    path('fanfic/<int:fanfic_id>',   views.fanfic_page,     name='fanfic_page'),
    path('chapter/<int:chapter_id>', views.chapter_reading, name='chapter_page'),
]

