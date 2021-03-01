from rest_framework.response import Response
from rest_framework.views import APIView
from core.tools import Poke
from rest_framework import status


class ListaPokemonAPIView(APIView):
    def get(self, request, format=None):
        pokemon = Poke()

        data = pokemon.lista_todos_pokemon()

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        pokemon = Poke()
        url = request.POST.get('url', None)
        data = pokemon.busca_pokemon(url)
        return Response(data, status=status.HTTP_200_OK)
