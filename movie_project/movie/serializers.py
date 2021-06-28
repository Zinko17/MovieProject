from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.Serializer):
    movie_name = serializers.ListField(child=serializers.CharField())


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'