from django.http import HttpResponse
from rest_framework import generics
from core.api.serializer import PokemonSerializer
from core.models import Pokemon


class poke_info(generics.CreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


