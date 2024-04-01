from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg


class MovieModelSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    def get_rate(self, obj):

        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990 !')
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O resumo não pode exceder 200 caracteres !')
        return value
