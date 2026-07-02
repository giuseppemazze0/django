from django.db import models

class Pokemon(models.Model):
    nome = models.CharField(max_length=30)
    numero_pokedex = models.PositiveIntegerField(unique=True)
    altura = models.DecimalField(max_digits=6, decimal_places=2)
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField(max_length=300)
    tipagens = models.ManyToManyField('Tipagem', related_name='pokemons')
    habitats = models.ManyToManyField('Habitat', related_name='pokemons')
    treinador = models.ForeignKey('Treinador', on_delete=models.CASCADE, related_name='pokemons', null=True, blank=True)

    def __str__(self):
        return self.nome



class Tipagem(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome



class Habitat(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField(max_length=300)

    def __str__(self):
        return self.nome



class Treinador(models.Model):
    nome = models.CharField(max_length=20)
    cidade = models.CharField(max_length=30)
    idade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome