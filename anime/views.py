from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView

from account.permissions import BasePermission
from .models import Anime, Comment
from .serializers import AnimeSerializer, CommentSerializer


class AnimeListCreateView(generics.ListCreateAPIView):
    serializer_class = AnimeSerializer

    def get_queryset(self):
        queryset = Anime.objects.all()
        genre_ids = self.request.query_params.getlist('genre')
        type_ids = self.request.query_params.get('type')
        year = self.request.query_params.get('year')

        if genre_ids:
            queryset = queryset.filter(genres__id__in=genre_ids)

        if type_ids:
            queryset = queryset.filter(type__id=type_ids)

        if year:
            queryset = queryset.filter(year=int(year))

        return queryset

class CommentListCreateAPIView(ListCreateAPIView):
    """
    Forum API endpoint to get list of blogs and create forum
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [BasePermission, ]

    def get_queryset(self):
        return self.queryset.filter(anime_id=self.kwargs['anime_id'])

    def perform_create(self, serializer):
        try:
            serializer.save(
                user=self.request.user,
                anime=get_object_or_404(Anime, id=self.kwargs['anime_id'])
            )
        except ValueError:
            serializer.save(
                anime=get_object_or_404(Anime, id=self.kwargs['anime_id'])
            )
