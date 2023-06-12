from django.db import models


# Create your models here.
from account.models import User



class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Anime(models.Model):
    name = models.CharField(max_length=30)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type')
    year = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name='genres')
    descriptions = models.TextField(blank=True, max_length=200)
    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
