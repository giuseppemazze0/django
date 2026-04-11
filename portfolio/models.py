from django.db import models


class Localizacao(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.rua}, {self.cidade}"


class Faculdade(models.Model):
    nome = models.CharField(max_length=100)
    max_capacidade_alunos = models.PositiveIntegerField()
    quantidade_salas = models.PositiveIntegerField()
    data_inauguracao = models.DateField()
    e_publica = models.BooleanField()
    localizacao = models.OneToOneField(Localizacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Sala(models.Model):
    numero_sala = models.CharField(max_length=5)
    tem_computadores = models.BooleanField()
    quantidade_cadeiras = models.PositiveIntegerField()
    quantidade_mesas = models.PositiveIntegerField()

    def __str__(self):
        return self.numero_sala


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    ects = models.PositiveIntegerField()
    descricao = models.TextField()
    obejetivo_curso = models.TextField()
    competencias_adquiridas = models.TextField()
    destinatario = models.TextField()
    ligacao_meio_empresarial = models.TextField()
    oportunidade_carreira = models.TextField()
    total_anos = models.PositiveIntegerField()
    faculdade = models.ForeignKey(Faculdade, on_delete=models.CASCADE)
    tfc = models.OneToOneField('TFC', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    OPCOES = [
        ('1', 'soft_skill'),
        ('2', 'hard_skill'),
    ]

    nome = models.CharField(max_length=100)
    habilidade_adquirida = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=1,
        choices=OPCOES,
        default='1',
    )

    def __str__(self):
        return self.nome


class Aluno(Pessoa):
    numero_aluno = models.CharField(max_length=10, unique=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE)
    competencias = models.ManyToManyField(Competencia)


class Professor(Pessoa):
    numero_professor = models.CharField(max_length=10, unique=True)
    licenciaturas = models.ManyToManyField(Licenciatura)  # corrigido


class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='tecnologias/')
    link_website_oficial = models.URLField()
    nivel_interesse = models.IntegerField()

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    nota = models.IntegerField()
    prazo = models.DateField()
    tecnologias = models.ManyToManyField(Tecnologia)  # corrigido
    link_github = models.URLField()
    link_video = models.URLField(blank=True, null=True)
    imagem = models.ImageField(upload_to='projetos/')

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ects = models.PositiveIntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='ucs/')
    professores = models.ManyToManyField(Professor)  # corrigido
    projetos = models.ManyToManyField(Projeto)  # corrigido

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    certificado = models.ImageField(upload_to='certificados/')


class TFC(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    nota = models.IntegerField()


class MakingOf(models.Model):
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='makingof/', blank=True, null=True)
    data = models.DateField(auto_now_add=True)