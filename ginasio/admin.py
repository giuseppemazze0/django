from django.contrib import admin
from .models import Ginasio

class GinasioAdmin(admin.ModelAdmin):
    list_display = ("nome", "mensalidade", "cidade",) # campos para aparecem na lista de objetos
    ordering = ("nome", "mensalidade", "cidade",) # permite especificar critério de ordenação
    search_fields = ("nome", "cidade") # cria caixa de pesquisa associada aos campos indicados

admin.site.register(Ginasio, GinasioAdmin)