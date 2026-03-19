from django.db import models

class AplicacaoDoQuizz(models.Model):
    nome = models.CharField(max_length=40)
    quantPerguntas = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome