from django.contrib import admin

# Register your models here.
from anime.models import Anime, Genre, Type

admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(Type)