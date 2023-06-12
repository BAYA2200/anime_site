from django.urls import path

from anime import views
from .views import AnimeListCreateView

urlpatterns = [
    path('post/', AnimeListCreateView.as_view()),
    path('post/<int:anime_id>/comments/', views.CommentListCreateAPIView.as_view()),

]
