from django.contrib import admin
from .models import (
    Localizacao, Faculdade, Sala, Licenciatura, Competencia,
    Aluno, Professor, Tecnologia, Projeto,
    UnidadeCurricular, Formacao, TFC, MakingOf
)


# -------------------------
# Pessoa
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone")
    search_fields = ("nome", "email")
    ordering = ("nome",)


# -------------------------
# Faculdade
class FaculdadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "max_capacidade_alunos", "data_inauguracao", "e_publica")
    search_fields = ("nome",)
    list_filter = ("e_publica", "data_inauguracao")
    ordering = ("nome",)


# -------------------------
# Sala
class SalaAdmin(admin.ModelAdmin):
    list_display = ("numero_sala", "tem_computadores", "quantidade_cadeiras", "quantidade_mesas")
    search_fields = ("numero_sala",)
    list_filter = ("tem_computadores",)
    ordering = ("numero_sala",)


# -------------------------
# Licenciatura
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ects", "total_anos", "faculdade")
    search_fields = ("nome", "descricao")
    list_filter = ("faculdade",)
    ordering = ("nome",)


# -------------------------
# Competência
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "habilidade_adquirida")
    search_fields = ("nome", "habilidade_adquirida")
    list_filter = ("tipo",)
    ordering = ("nome",)


# -------------------------
# Aluno
class AlunoAdmin(PessoaAdmin):
    list_display = PessoaAdmin.list_display + ("numero_aluno", "licenciatura")
    search_fields = PessoaAdmin.search_fields + ("numero_aluno",)
    list_filter = ("licenciatura",)


# -------------------------
# Professor
class ProfessorAdmin(PessoaAdmin):
    list_display = PessoaAdmin.list_display + ("numero_professor",)
    search_fields = PessoaAdmin.search_fields + ("numero_professor",)
    list_filter = ("licenciaturas",)


# -------------------------
# Tecnologia
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nivel_interesse")
    search_fields = ("nome",)
    list_filter = ("nivel_interesse",)
    ordering = ("nome",)


# -------------------------
# Projeto
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "nota", "prazo")
    search_fields = ("nome", "descricao")
    list_filter = ("nota", "prazo", "tecnologias")
    ordering = ("prazo",)


# -------------------------
# UC
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "ects", "licenciatura")
    search_fields = ("nome", "descricao")
    list_filter = ("licenciatura",)
    ordering = ("nome",)


# -------------------------
# Formação
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_inicio", "data_fim")
    search_fields = ("nome",)
    ordering = ("-data_inicio",)


# -------------------------
# TFC
class TFCAdmin(admin.ModelAdmin):
    list_display = ("nome", "nota")
    search_fields = ("nome", "descricao")
    ordering = ("-nota",)


# -------------------------
# Making Of
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("data",)
    search_fields = ("descricao",)
    ordering = ("-data",)



admin.site.register(Localizacao)
admin.site.register(Faculdade, FaculdadeAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)
admin.site.register(Formacao, FormacaoAdmin)
admin.site.register(TFC, TFCAdmin)
admin.site.register(MakingOf, MakingOfAdmin)