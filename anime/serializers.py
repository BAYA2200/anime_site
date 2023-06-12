from rest_framework import serializers

from anime.models import Anime, Genre, Comment


class TypedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AnimeSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Anime
        fields = ['name', 'descriptions', 'type', 'year', 'genres']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
