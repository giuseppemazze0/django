from django.contrib import admin
from .models import *


# -------------------------
# Pessoa (base para Aluno e Professor)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone")
    search_fields = ("nome", "email")
    ordering = ("nome",)


# -------------------------
# Faculdade
class FaculdadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "data_inauguracao")
    search_fields = ("nome", "cidade")
    ordering = ("nome",)


# -------------------------
# Licenciatura
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ects", "total_anos", "faculdade")
    search_fields = ("nome", "descricao")
    list_filter = ("faculdade",)
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
    filter_horizontal = ("licenciaturas",)


# -------------------------
# Tecnologia
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "link_website_oficial")
    search_fields = ("nome",)
    ordering = ("nome",)


# -------------------------
# Projeto
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano_semestre", "uc")
    search_fields = ("nome", "descricao")
    list_filter = ("ano_semestre", "tecnologias")
    filter_horizontal = ("tecnologias",)
    ordering = ("ano_semestre",)


# -------------------------
# Unidade Curricular
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "ects", "licenciatura")
    search_fields = ("nome", "descricao")
    list_filter = ("licenciatura",)
    filter_horizontal = ("professores",)
    ordering = ("nome",)


# -------------------------
# TFC
class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "licenciatura", "rating")
    search_fields = ("titulo", "sumario")
    list_filter = ("licenciatura", "rating")
    filter_horizontal = ("autores", "orientadores", "tecnologias")
    ordering = ("-rating",)


# -------------------------
# Competencia
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nivel")
    search_fields = ("nome", "descricao")
    list_filter = ("nivel",)
    ordering = ("nome",)


# -------------------------
# Competencia
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "instituicao", "data_inicio", "data_fim")
    search_fields = ("nome", "instituicao", "descricao")
    list_filter = ("instituicao",)
    filter_horizontal = ("competencias",)
    ordering = ("data_inicio",)


# -------------------------
# Making Of
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("data",)
    search_fields = ("descricao",)
    ordering = ("-data",)






# -------------------------
# Restaurante
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ("nome", "localizacao", "capacidade")
    search_fields = ("nome", "localizacao")
    ordering = ("nome",)


# -------------------------
# Cliente
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)


# -------------------------
# Prato
class PratoAdmin(admin.ModelAdmin):
    list_display = ("nome", "restaurante")
    search_fields = ("nome",)
    list_filter = ("restaurante",)
    ordering = ("nome",)


# -------------------------
# Reserva
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("cliente", "restaurante", "data", "hora", "numero_pessoas")
    search_fields = ("cliente__nome", "restaurante__nome")
    list_filter = ("restaurante", "data")
    ordering = ("-data", "hora")


# -------------------------
# Utilizador
class UtilizadorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ("nome", "email")
    filter_horizontal = ("favoritas",)
    ordering = ("nome",)


# -------------------------
# Ingrediente
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)


# -------------------------
# Receita
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome", "utilizador")
    search_fields = ("nome", "descricao")
    list_filter = ("utilizador",)
    filter_horizontal = ("ingredientes",)
    ordering = ("nome",)


# -------------------------
# Piscina
class PiscinaAdmin(admin.ModelAdmin):
    list_display = ("nome", "localizacao")
    search_fields = ("nome", "localizacao")
    ordering = ("nome",)


# -------------------------
# Treinador
class TreinadorAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)


# -------------------------
# Nadador
class NadadorAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)


# -------------------------
# Estilo
class EstiloAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)


# -------------------------
# Treino
class TreinoAdmin(admin.ModelAdmin):
    list_display = ("data", "hora", "treinador", "piscina")
    search_fields = ("treinador__nome", "piscina__nome")
    list_filter = ("treinador", "piscina", "data")
    filter_horizontal = ("nadadores", "estilos")
    ordering = ("-data", "hora")


admin.site.register(Restaurante, RestauranteAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Prato, PratoAdmin)
admin.site.register(Reserva, ReservaAdmin)

admin.site.register(Utilizador, UtilizadorAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Receita, ReceitaAdmin)

admin.site.register(Piscina, PiscinaAdmin)
admin.site.register(Treinador, TreinadorAdmin)
admin.site.register(Nadador, NadadorAdmin)
admin.site.register(Estilo, EstiloAdmin)
admin.site.register(Treino, TreinoAdmin)








# -------------------------
# REGISTOS
admin.site.register(Faculdade, FaculdadeAdmin)
admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)
admin.site.register(TFC, TFCAdmin)
admin.site.register(MakingOf, MakingOfAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Formacao, FormacaoAdmin)