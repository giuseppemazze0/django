from django.db import models



class Faculdade(models.Model):
    nome = models.CharField(max_length=100)
    data_inauguracao = models.DateField()
    rua = models.CharField(max_length=100, null=True)
    bairro = models.CharField(max_length=100, null=True)
    cidade = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome



class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    ects = models.PositiveIntegerField()
    descricao = models.TextField()
    objetivo_curso = models.TextField()
    competencias_adquiridas = models.TextField()
    destinatario = models.TextField()
    ligacao_meio_empresarial = models.TextField()
    oportunidade_carreira = models.TextField()
    total_anos = models.PositiveIntegerField()
    faculdade = models.ForeignKey(Faculdade, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome



class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


class Aluno(Pessoa):
    bio = models.CharField(max_length=100, null=True)
    foto_perfil = models.ImageField(upload_to='aluno/foto_perfil/', null=True)
    numero_aluno = models.CharField(max_length=10, unique=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='licenciatura_aluno')



class Professor(Pessoa):
    numero_professor = models.CharField(max_length=10, unique=True)
    licenciaturas = models.ManyToManyField(Licenciatura)



class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='tecnologias/')
    link_website_oficial = models.URLField()

    def __str__(self):
        return self.nome



class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    ano_semestre = models.CharField(max_length=30, null=True)
    descricao = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia)
    link_github = models.URLField()
    link_video = models.URLField(blank=True, null=True)
    uc = models.ForeignKey('UnidadeCurricular', on_delete=models.CASCADE, related_name="projetos", null=True)
    imagem = models.ImageField(upload_to='projetos/')

    def __str__(self):
        return self.nome



class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ects = models.PositiveIntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='ucs/')
    professores = models.ManyToManyField(Professor)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs')

    def __str__(self):
        return self.nome



class TFC(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField('Aluno', related_name="tfcs")
    orientadores = models.ManyToManyField('Professor', related_name="tfcs")
    licenciatura = models.ForeignKey('Licenciatura', on_delete=models.CASCADE, related_name="tfcs", null=True)
    sumario = models.TextField()
    link_pdf = models.URLField(blank=True, null=True)
    imagem = models.URLField(null=True)
    palavras_chave = models.CharField(max_length=300, null=True)
    areas = models.CharField(max_length=300, null=True)
    tecnologias = models.ManyToManyField('Tecnologia', related_name="tfcs")
    rating = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.titulo



# Transformei strings do JSON em relações ManyToMany
# Evitei redundância entre entidades
# Normalizei os dados
class MakingOf(models.Model):
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='makingof/', blank=True, null=True)
    data = models.DateField(auto_now_add=True)