from django.contrib import admin
from .models import Pessoa
from .models import Amigo


# list_display -> campos para aparecem na lista de objetos (Define as colunas que aparecem na lista de objetos no admin)
# ordering -> permite especificar critério de ordenação (Adiciona uma barra de pesquisa no topo)
# search_fields -> cria caixa de pesquisa associada aos campos indicados (Define a ordem padrão da lista)



class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade",)
    ordering = ("nome", "idade",)
    search_fields = ("nome",)



class AmigoAdmin(admin.ModelAdmin):
    list_display = ("nome_grupo",)
    ordering = ("nome_grupo",)
    search_fields = ("nome_grupo",)



admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Amigo, AmigoAdmin)