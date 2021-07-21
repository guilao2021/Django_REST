from django.db import models

class Tratamento(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.FloatField()

    def __str__(self):
        return self.descricao