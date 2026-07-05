from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="desenvolvedor"),

    path('tfcs/', views.tfcs_view, name="tfcs"),

    path('faculdade/', views.faculdade_view, name="faculdade"),

    path('sobre_aplicacao/', views.sobre_aplicacao_view, name="sobre_aplicacao"),

    path('projetos/', views.projetos_view, name="projetos"),
    path('projeto/novo/', views.novo_projeto_view, name="novo_projeto"),
    path('projeto/<int:projeto_id>/editar/', views.editar_projeto_view, name="editar_projeto"),
    path('projeto/<int:projeto_id>/apagar/', views.apagar_projeto_view, name="apagar_projeto"),

    path('tecnologias/', views.tecnologias_view, name="tecnologias"),
    path('tecnologia/nova/', views.nova_tecnologia_view, name="nova_tecnologia"),
    path('tecnologia/<int:tecnologia_id>/editar/', views.editar_tecnologia_view, name="editar_tecnologia"),
    path('tecnologia/<int:tecnologia_id>/apagar/', views.apagar_tecnologia_view, name="apagar_tecnologia"),

    path('competencias/', views.competencias_view, name="competencias"),
    path('competencia/nova/', views.nova_competencia_view, name="nova_competencia"),
    path('competencia/<int:competencia_id>/editar/', views.editar_competencia_view, name="editar_competencia"),
    path('competencia/<int:competencia_id>/apagar/', views.apagar_competencia_view, name="apagar_competencia"),

    path('formacoes/', views.formacoes_view, name="formacoes"),
    path('formacao/nova/', views.nova_formacao_view, name="nova_formacao"),
    path('formacao/<int:formacao_id>/editar/', views.editar_formacao_view, name="editar_formacao"),
    path('formacao/<int:formacao_id>/apagar/', views.apagar_formacao_view, name="apagar_formacao"),
]