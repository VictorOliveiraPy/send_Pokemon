from rest_framework import serializers

from core.models import Pokemon
from pokemon_api.celery import app


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'


