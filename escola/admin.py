from django.contrib import admin
from .models import Escola

class EscolaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nivelEnsino", "telefone", "cidade") # campos para aparecem na lista de objetos
    ordering = ("nome", "cidade") # permite especificar critério de ordenação
    search_fields = ("nome", "cidade") # cria caixa de pesquisa associada aos campos indicados

admin.site.register(Escola, EscolaAdmin)