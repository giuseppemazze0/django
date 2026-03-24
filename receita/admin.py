from django.contrib import admin
from .models import Ingrediente
from .models import Receita
from .models import Utilizador

# list_display -> campos para aparecem na lista de objetos (Define as colunas que aparecem na lista de objetos no admin)
# ordering -> permite especificar critério de ordenação (Adiciona uma barra de pesquisa no topo)
# search_fields -> cria caixa de pesquisa associada aos campos indicados (Define a ordem padrão da lista)



class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "unidade")
    ordering = ("nome", "unidade")
    search_fields = ("nome",)



class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao", "nacionalidade", "tempo_preparo")
    ordering = ("nome", "nacionalidade", "tempo_preparo")
    search_fields = ("nome", "descricao", "nacionalidade", "tempo_preparo")



class UtilizadorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email",)
    ordering = ("nome",)
    search_fields = ("nome",)



admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Utilizador, UtilizadorAdmin)