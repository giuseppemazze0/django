from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    
    def __str__(self):
        return f'{self.nome} tem {self.idade} {"anos" if self.idade > 1 else "ano"}.'


class Amigo(models.Model):
    nome_grupo = models.CharField(max_length=100)
    pessoas = models.ManyToManyField(Pessoa, related_name="grupos")

    def __str__(self):
        return self.nome_grupo