from django.contrib import admin
from .models import Ginasio
from .models import Treinador
from .models import Membro
from .models import SessaoTreino


# list_display -> campos para aparecem na lista de objetos (Define as colunas que aparecem na lista de objetos no admin)
# ordering -> permite especificar critério de ordenação (Adiciona uma barra de pesquisa no topo)
# search_fields -> cria caixa de pesquisa associada aos campos indicados (Define a ordem padrão da lista)



class GinasioAdmin(admin.ModelAdmin):
    list_display = ("nome", "mensalidade", "rua", "cidade")
    ordering = ("nome", "mensalidade", "cidade")
    search_fields = ("nome", "mensalidade", "cidade")



class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone")
    ordering = ("nome",)
    search_fields = ("nome",)



class TreinadorAdmin(PessoaAdmin):
    list_display = PessoaAdmin.list_display + ("especialidade",)
    ordering = PessoaAdmin.ordering + ("especialidade",)
    search_fields = PessoaAdmin.search_fields + ("especialidade",)



class MembroAdmin(PessoaAdmin):
    list_display = PessoaAdmin.list_display + ("data_nascimento",)
    ordering = PessoaAdmin.ordering
    search_fields = PessoaAdmin.search_fields



class SessaoTreinoAdmin(admin.ModelAdmin):
    list_display = ("treinador", "membro", "data", "hora", "ginasio")
    ordering = ("treinador__nome", "data", "hora", "ginasio__nome")
    search_fields = ("treinador__nome", "data", "hora", "ginasio__nome")



admin.site.register(Ginasio, GinasioAdmin)
admin.site.register(Treinador, TreinadorAdmin)
admin.site.register(Membro, MembroAdmin)
admin.site.register(SessaoTreino, SessaoTreinoAdmin)