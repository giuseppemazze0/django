from django.contrib import admin
from .models import Loja

class LojaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade",) # campos para aparecem na lista de objetos
    ordering = ("nome", "cidade") # permite especificar critério de ordenação
    search_fields = ("nome", "cidade") # cria caixa de pesquisa associada aos campos indicados

admin.site.register(Loja, LojaAdmin)
