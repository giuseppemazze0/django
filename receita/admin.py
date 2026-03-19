from django.contrib import admin
from .models import Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tempoPreparo", "nacionalidade") # campos para aparecem na lista de objetos
    ordering = ("nome", "nacionalidade",) # permite especificar critério de ordenação
    search_fields = ("nome", "nacionalidade") # cria caixa de pesquisa associada aos campos indicados

admin.site.register(Receita, ReceitaAdmin)