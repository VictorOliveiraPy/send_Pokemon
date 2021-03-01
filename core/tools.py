from django.core.mail import send_mail
from .models import Pokemon
import requests
from dataclasses import dataclass
from typing import Dict


class EnviarEmail(object):
    def enviar_email(self, titulo, msg, de, para):
        try:
            send_mail(titulo, msg, de, [para], fail_silently=False)
            return 'ok'
        except Exception as e:
            return 'Error'


def atualizar_envio(email):
    atualizar = Pokemon.objects.filter(email1=email).update(enviar=True)

    return True


@dataclass(init=False)
class Poke:
    url_base: str = "https://pokeapi.co/api/v2/pokemon/"
    name: str
    height: float
    weight: float
    abilities: Dict[str, str]
    base_experience: int

    def lista_todos_pokemon(self):
        r = requests.get(self.url_base)
        return r.json()

    def busca_pokemon(self, url):
        r = requests.get(url).json()
        resultado = {}

        if r:
            self.name = r["forms"][0]["name"]
            self.base_experience = float(r["base_experience"])
            self.height = int(r["height"])
            self.weight = float(r["weight"])
            for res in r["abilities"]:
                self.abilities = res["ability"]

            resultado["name"] = self.name
            resultado["height"] = self.height
            resultado["weight"] = self.weight
            resultado["abilities"] = self.abilities
            resultado["base_experience"] = self.base_experience
            return resultado
