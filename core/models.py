from django.db import models


# Create your models here.
class Pokemon(models.Model):
    email = models.EmailField('E-mail', blank=False)
    email2 = models.EmailField('Segundo E-mail', blank=True)
    data_hora = models.DateTimeField(auto_now_add=False)
