from django.db import models


class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    unidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class Receita(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    tempo_preparo = models.PositiveIntegerField(blank=True, null=True, help_text="Tempo em minutos")
    ingredientes = models.ManyToManyField(Ingrediente,related_name='receitas')
    nacionalidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class Utilizador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    receitas_favoritadas = models.ManyToManyField(Receita ,related_name='utilizadores', blank=True)

    def __str__(self):
        return self.nome