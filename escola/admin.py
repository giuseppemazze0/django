from django.contrib import admin
from .models import Escola
from .models import Professor
from .models import Aluno
from .models import Turma


# list_display -> campos para aparecem na lista de objetos (Define as colunas que aparecem na lista de objetos no admin)
# ordering -> permite especificar critério de ordenação (Adiciona uma barra de pesquisa no topo)
# search_fields -> cria caixa de pesquisa associada aos campos indicados (Define a ordem padrão da lista)



class EscolaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "rua")
    ordering = ("nome", "cidade")
    search_fields = ("nome", "cidade")



class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "numero_escola", "email", "data_nascimento")
    ordering = ("nome", "numero_escola")
    search_fields = ("nome", "numero_escola", "email")



class ProfessorAdmin(PessoaAdmin):
    list_display = PessoaAdmin.list_display + ("leciona", "turma")
    ordering = PessoaAdmin.ordering + ("leciona", "turma")
    search_fields = PessoaAdmin.search_fields + ("turma__nome",)



class AlunoAdmin(PessoaAdmin):
    list_display = PessoaAdmin.list_display + ("turma",)
    ordering = PessoaAdmin.ordering + ("turma__nome",)
    search_fields = PessoaAdmin.search_fields + ("turma__nome",)



class TurmaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano_letivo", "escola")
    ordering = ("nome", "ano_letivo", "escola")
    search_fields = ("nome", "escola")



admin.site.register(Escola, EscolaAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Turma, TurmaAdmin)