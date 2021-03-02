from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .tools import EnviarEmail
from .tools import atualizar_envio
from .models import Pokemon
from datetime import date


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def enviar_emial():
    enviar = EnviarEmail()
    data_atual = date.today()
    pokemon = Pokemon.objects.filter(enviar=False, agendamento=data_atual)
    for destinario in pokemon:
        enviar.enviar_email(
            'Treinado Pokemon',
            'pokemon',
            'victorblog410@gmail.com',
            destinario.email

        )
        atualizar_envio(destinario.email)

    return True
