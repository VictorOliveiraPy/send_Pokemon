from django.core.mail import send_mail
from .models import Pokemon
import requests


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


def pokemon_api():
    r = requests.get('https://pokeapi.co/api/v2/pokemon/')

    return
