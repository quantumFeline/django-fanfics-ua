from django.db import models


class Fandom(models.Model):
    name = models.CharField(max_length=200)
    fandom_author = models.CharField(max_length=200)


class Author(models.Model):
    nickname= models.CharField(max_length=50)
    register_date = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.nickname


class Fanfic(models.Model):
    title = models.CharField(max_length=500)
    annotation = models.TextField()
    publication_date = models.DateTimeField('Published:')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL)
    beta = models.ForeignKey(Author, on_delete=models.SET_NULL)
    fandom = models.ForeignKey(Fandom, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Chapter(models.Model):
    fanfic = models.ForeignKey(Fanfic, on_delete=models.CASCADE)
    text = models.TextField()
