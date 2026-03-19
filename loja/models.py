from django.db import models

class Loja(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nome