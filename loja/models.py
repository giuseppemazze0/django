from django.db import models



class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    descricao = models.TextField(max_length=300)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="produtos")

    def __str__(self):
        return self.nome



class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.nome



class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos")
    data = models.DateField()
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.codigo} - {self.cliente.nome}"



class PeticaoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="itens")
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}x"



class Loja(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    rua = models.CharField(max_length=100, default="Desconhecido")
    url_site = models.CharField(max_length=200, blank=True)
    produtos = models.ManyToManyField(Produto, related_name="lojas")
    
    def __str__(self):
        return self.nome