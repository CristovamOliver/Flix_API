from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestoryView


urlpatterns = [
    path("genres/", GenreCreateListView.as_view(), name='genre-create-list'),
    path("genres/<int:pk>", GenreRetrieveUpdateDestoryView.as_view(),
         name='genre-detail-view'),
]
