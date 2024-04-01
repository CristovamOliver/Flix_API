from rest_framework import generics, views, response, status
from movies.models import Movie
from movies.serializers import MovieModelSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from django.db.models import Count, Avg
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetrieveUpdateDestrowView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values(
            'genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        avg_stars = Review.objects.aggregate(
            avg_stars=Avg('stars'))['avg_stars']

        return response.Response(
            data={'Total Movies': total_movies,
                  'Movies by Genre': movies_by_genre,
                  'Total Reviews': total_reviews,
                  'Average Stars': round(avg_stars, 1) if avg_stars else 0},
            status=status.HTTP_200_OK
        )
