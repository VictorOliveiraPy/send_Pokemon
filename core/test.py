from django.core import mail
from .tools import EnviarEmail
from unittest.mock import MagicMock, Mock
from django.test import TestCase


# Test de envio fake
class EmailTest(TestCase):
    def test_no_email_sent(self):
        teste_email = EnviarEmail()
        resposta = teste_email.enviar_email('ola', 'victorblog410@gmail.com',
                                            'victor', 'victorblog410@gmail.com')

        self.assertEqual(resposta, 'ok')

    def envio_fake(self):
        enviar_email = Mock(return_value="ok")

        self.assertEqual(enviar_email, 'ok')

    def api_fake(self):
        chama_api = Mock(return_value=200)

        self.assertEqual(chama_api, 200)
