from django.contrib import admin
from .models import Categoria
from .models import Produto
from .models import Cliente
from .models import Pedido
from .models import PeticaoItem
from .models import Loja


# list_display -> campos para aparecem na lista de objetos (Define as colunas que aparecem na lista de objetos no admin)
# ordering -> permite especificar critério de ordenação (Adiciona uma barra de pesquisa no topo)
# search_fields -> cria caixa de pesquisa associada aos campos indicados (Define a ordem padrão da lista)



class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)



class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "descricao", "categoria")
    ordering = ("nome", "preco", "categoria")
    search_fields = ("nome", "preco", "categoria", "descricao")



class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    ordering = ("nome",)
    search_fields = ("nome",)



class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "data", "codigo")
    ordering = ("cliente__nome", "data", "codigo")
    search_fields = ("cliente__nome", "data", "codigo")



class PeticaoItemAdmin(admin.ModelAdmin):
    list_display = ("pedido", "produto", "quantidade")
    ordering = ("pedido__codigo", "produto__nome", "quantidade")
    search_fields = ("pedido__codigo", "produto__nome", "quantidade")



class LojaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "rua", "url_site")
    ordering = ("nome", "cidade")
    search_fields = ("nome", "cidade")



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PeticaoItem, PeticaoItemAdmin)
admin.site.register(Loja, LojaAdmin)
