from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')

    stars = models.IntegerField(
        validators=[MinValueValidator(0, 'Zero é a nota mínima !'),
                    MaxValueValidator(5, 'Cinco é a nota máxima !')])

    comment = models.TextField(null=True, blank=True)
