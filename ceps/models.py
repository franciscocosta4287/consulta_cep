# from django.db import models

# Create your models here.
from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    ibge = models.CharField(max_length=7, blank=True, null=True)
    gia = models.CharField(max_length=4, blank=True, null=True)
    ddd = models.CharField(max_length=3, blank=True, null=True)
    siafi = models.CharField(max_length=4, blank=True, null=True)
    numero = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return f"{self.cep} - {self.logradouro}"
