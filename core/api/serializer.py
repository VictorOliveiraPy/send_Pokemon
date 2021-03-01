from rest_framework import serializers

from core.models import Pokemon
from pokemon_api.celery import app


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        app.conf.on = {
            'add-every-30-seconds': {
                'task': 'tasks.test',
                'schedule': 5.0,
                'args': [validated_data]
            },
        }
        return super().create(validated_data)
