from django.urls import path
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestrowView, MovieStatsView


urlpatterns = [
    path("movies/", MovieCreateListView.as_view()),
    path("movies/<int:pk>", MovieRetrieveUpdateDestrowView.as_view()),
    path('movies/stats/', MovieStatsView.as_view(), name='movie-stats-view'),
]
