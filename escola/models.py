from django.db import models


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    ano_letivo = models.CharField(max_length=9)
    escola = models.ForeignKey('Escola', on_delete=models.CASCADE, related_name='turmas')

    def __str__(self):
        return f"Turma {self.ano_letivo}º{self.nome}"



class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    numero_escola = models.PositiveIntegerField(unique=True)
    data_nascimento = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome



class Professor(Pessoa):
    leciona = models.CharField(max_length=100, blank=True, null=True)
    turma = models.OneToOneField(Turma, on_delete=models.CASCADE, related_name='professor')



class Aluno(Pessoa):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos')



class Escola(models.Model):
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=100, default="Desconhecido")
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome