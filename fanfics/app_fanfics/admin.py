from django.contrib import admin

# Register your models here.
from .models import Author, Fandom

admin.site.register(Author)
admin.site.register(Fandom)
