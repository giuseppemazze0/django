from django.db import models



class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class Treinador(Pessoa):
    especialidade = models.CharField(max_length=100, blank=True, null=True)



class Membro(Pessoa):
    data_nascimento = models.DateField(blank=True, null=True)



class SessaoTreino(models.Model):
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE, related_name='sessoes_treinadores')
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='sessoes_membros')
    data = models.DateField()
    hora = models.TimeField()
    ginasio = models.ForeignKey('Ginasio', on_delete=models.CASCADE, related_name='sessoes_ginasios')

    def __str__(self):
        return f"Marcado no dia {self.data} às {self.hora.strftime('%H:%M')}"



class Ginasio(models.Model):
    nome = models.CharField(max_length=100)
    mensalidade = models.DecimalField(max_digits=6, decimal_places=2)
    rua = models.CharField(max_length=100, default="Desconhecido")
    cidade = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome