from django.db import models

# Create your models here.
class Idioma(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"Nome: {self.nome}"

class Pais(models.Model):
    nome_oficial = models.CharField(max_length=150)
    capital = models.CharField(max_length=150, null=True, blank=True)
    regiao = models.CharField(max_length=50)
    subregiao = models.CharField(max_length=150, null=True, blank=True)
    idioma = models.ForeignKey(Idioma, max_length=50, null=True, blank=True, on_delete=models.CASCADE)
    populacao = models.BigIntegerField()
    area = models.FloatField()

    def __str__(self):
        return f"Nome do país: {self.nome_oficial}, Capital: {self.capital}, Região: {self.regiao}, Sub-região: {self.subregiao}, Idioma: {self.idioma}, População: {self.populacao}, Área: {self.area}"
