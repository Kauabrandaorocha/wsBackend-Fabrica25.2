from django.db import models

# Create your models here.
class Idioma(models.Model):
    nome = models.CharField(max_length=50)

class Pais(models.Model):
    nome_oficial = models.CharField(max_length=150)
    capital = models.CharField(max_length=150, null=True, blank=True)
    regiao = models.CharField(max_length=50)
    subregiao = models.CharField(max_length=150, null=True, blank=True)
    idioma = models.ForeignKey(Idioma, max_length=50, null=True, blank=True, on_delete=models.CASCADE)
    populacao = models.BigIntegerField()
    area = models.FloatField()
