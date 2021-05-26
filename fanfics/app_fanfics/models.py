import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Fandom(models.Model):
    name = models.CharField(max_length=200)
    fandom_author = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    nickname = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    register_date = models.DateField()

    def __str__(self):
        return self.nickname


class Fanfic(models.Model):
    title = models.CharField(max_length=500)
    annotation = models.TextField()
    publication_date = models.DateTimeField('Published:', default=datetime.date.today())
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    # TODO
    # beta = models.ForeignKey(Author, on_delete=models.SET_NULL)
    fandom = models.ForeignKey(Fandom, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Chapter(models.Model):
    fanfic = models.ForeignKey(Fanfic, on_delete=models.CASCADE)
    chapter_number = models.IntegerField(default=1)
    chapter_title = models.CharField(max_length=500, default="Глава " + str(chapter_number))
    publication_date = models.DateTimeField('Published:', default=datetime.date.today())
    text = models.FileField()
