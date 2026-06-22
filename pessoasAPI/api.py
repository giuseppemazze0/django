from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from typing import List
from .schemas import PessoaIn, PessoaOut, ErrorSchema
from .models import Pessoa


api = NinjaAPI(
    title = "API RESTful das Pessoas",
    description = "API para gerir pessoas com operações completas sobre os dados",
    version = "1.0.0"
)



# Listar dados - GET - 200 OK
@api.get(
    "pessoa/",
    response={200: List[PessoaOut]},
    tags=["Pessoas"],
    description="Lista todas as pessoas"
)
def listar_pessoas(request, idade: int = None, nome: str = None, sort: str = None, limit: int = 10, offset: int = 0):
    pessoas = Pessoa.objects.all()[offset: offset+limit]

    if sort in ('nome', '-nome', 'idade', '-idade'):
        pessoas = pessoas.order_by(sort)

    if idade is not None:
        pessoas = pessoas.filter(idade=idade)

    if nome is not None:
        pessoas = pessoas.filter(nome__icontains=nome)


    return 200, pessoas




# Buscar um recurso - GET - 200 OK, 404 Not Found
@api.get(
    "pessoas/{pessoa_id}/",
    response={200: PessoaOut, 404: ErrorSchema},
    tags=["Pessoas"],
    description="Buscar por uma pessoa"
)
def buscar_pessoa(request, pessoa_id: int):
    # return 200, get_object_or_404(Pessoa, id=pessoa_id)
    try:
        return 200, Pessoa.objects.get(id=pessoa_id)
    except Pessoa.DoesNotExist:
        return 404, {"detail": "Pessoa não encontrada"}




# Criar novo recurso - POST - 201 Created, 400 Bad Request
@api.post(
    "pessoas/",
    response={201: PessoaOut, 400: ErrorSchema},
    tags=["Pessoas"],
    description="Criar uma nova pessoa"
)
def criar_pessoa(request, data: PessoaIn):
    return 201, Pessoa.objects.create(**data.dict())




# Substituir recurso - PUT - 200 OK, 400 Bad Request, 404 Not Found
@api.put(
    "pessoas/{pessoa_id}/",
    response={200: PessoaOut, 404: ErrorSchema},
    tags=["Pessoas"],
    description="Substitui dados de uma pessoa"
)
def atualizar_pessoa(request, pessoa_id: int, data: PessoaIn):
    #pessoa = get_object_or_404(Pessoa, id=id_pessoa)
    #for attr, value in data.dict().items:
    #    setattr(pessoa, attr, value)
    #pessoa.save()
    #return 200, pessoa

    updated = Pessoa.objects.filter(id=pessoa_id).update(**data.dict())

    if not updated:
        return 404, {"message": "Pessoa não encontrada."}

    pessoa = Pessoa.objects.get(id=pessoa_id)

    return 200, pessoa




#Apagar recurso - DELETE - 204 No Content, 404 Not Found
@api.delete(
    "pessoa/{pessoa_id}/",
    response={204: None, 404: ErrorSchema},
    tags=["Pessoas"],
    description="Apagar uma pessoa"
)
def apagar_pessoa(request, pessoa_id: int):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    pessoa.delete()

    return 204, None