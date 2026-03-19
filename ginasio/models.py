from django.db import models

class Ginasio(models.Model):
    nome = models.CharField(max_length=50)
    mensalidade = models.DecimalField(max_digits=6, decimal_places=2)
    cidade = models.CharField(max_length=40)

    def __str__(self):
        return self.nome