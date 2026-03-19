from django.contrib import admin
from .models import AplicacaoDoQuizz

class AplicacaoDoQuizzAdmin(admin.ModelAdmin):
    list_display = ("nome", "quantPerguntas", "descricao",) # campos para aparecem na lista de objetos
    ordering = ("nome", "quantPerguntas") # permite especificar critério de ordenação
    search_fields = ("nome",) # cria caixa de pesquisa associada aos campos indicados

admin.site.register(AplicacaoDoQuizz, AplicacaoDoQuizzAdmin)
