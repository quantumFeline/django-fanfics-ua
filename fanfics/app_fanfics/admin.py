from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Author, Fandom, User

admin.site.register(Author)
admin.site.register(Fandom)
admin.site.register(User, UserAdmin)