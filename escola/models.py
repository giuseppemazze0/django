from django.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=50)
    nivelEnsino = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15, blank=True)
    cidade = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nome