from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade",) # campos para aparecem na lista de objetos
    ordering = ("nome", "idade",) # permite especificar critério de ordenação
    search_fields = ("nome",) # cria caixa de pesquisa associada aos campos indicados

admin.site.register(Pessoa, PessoaAdmin)