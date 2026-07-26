from django.conf import settings
from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from typing import List
from .schemas import *
from .models import *
from ninja.security import APIKeyHeader

apiLegal = NinjaAPI(
    title="api RESTful Época Especial",
    description="""
    Esta api disponibiliza endpoints para três domínios distintos:

    - Restaurante: gestão de restaurantes, pratos, clientes e reservas.
    - Receitas: gestão de receitas, ingredientes, utilizadores e favoritos.
    - Natação: gestão de piscinas, treinos, treinadores, nadadores e estilos de natação.

    Todos os endpoints seguem o padrão RESTful e permitem consultar os dados armazenados na aplicação.
    """,
    version="1.0.0",
    urls_namespace="epoca_especial_api"
)


class AuthapiKey(APIKeyHeader):
    param_name = "X-api-Key"

    def authenticate(self, request, key):
        if key == settings.api_KEY:
            return key
        return None


# ====================
# Restaurante
# ====================

@apiLegal.get(
    "restaurantes/",
    response={200: List[RestauranteOut]},
    tags=["Restaurantes"],
    description="Lista todos os restaurantes registrados."
)
def listar_restaurantes(
    request,
    nome: str = None,
    localizacao: str = None,
    sort: str = None,
    limit: int = 5,
    offset: int = 0
):
    restaurantes = Restaurante.objects.all()

    if nome is not None:
        restaurantes = restaurantes.filter(nome__icontains=nome)

    if localizacao is not None:
        restaurantes = restaurantes.filter(localizacao__icontains=localizacao)

    if sort in (
        "nome", "-nome",
        "localizacao", "-localizacao",
        "capacidade", "-capacidade"
    ):
        restaurantes = restaurantes.order_by(sort)

    restaurantes = restaurantes[offset:offset + limit]

    return 200, restaurantes


@apiLegal.get(
    "restaurantes/{restaurante_id}/",
    response={200: RestauranteOut, 404: ErrorSchema},
    tags=["Restaurantes"],
    description="Busca por um restaurante a partir do id na api."
)
def buscar_restaurante(request, restaurante_id: int):
    try:
        return 200, Restaurante.objects.get(id=restaurante_id)
    except Restaurante.DoesNotExist:
        return 404, {
            "detail": "Restaurante não encontrado. Id inserido incorretamente ou não está cadastrado um restaurante com esse id."
        }


@apiLegal.post(
    "restaurantes/",
    response={201: RestauranteOut, 400: ErrorSchema},
    tags=["Restaurantes"],
    description="Cria um novo restaurante na api."
)
def criar_restaurante(request, data: RestauranteIn):
    return 201, Restaurante.objects.create(**data.dict())


@apiLegal.put(
    "restaurantes/{restaurante_id}/",
    response={200: RestauranteOut, 404: ErrorSchema},
    tags=["Restaurantes"],
    description="Atualiza os dados de um restaurante na api.",
    auth=AuthapiKey()
)
def atualizar_restaurante(request, restaurante_id: int, data: RestauranteIn):
    updated = Restaurante.objects.filter(id=restaurante_id).update(**data.dict())

    if not updated:
        return 404, {
            "message": "Restaurante não encontrado. Id inserido incorretamente ou não está cadastrado um restaurante com esse id."
        }

    restaurante = Restaurante.objects.get(id=restaurante_id)

    return 200, restaurante


@apiLegal.delete(
    "restaurantes/{restaurante_id}/",
    response={204: None, 404: ErrorSchema},
    tags=["Restaurantes"],
    description="Apaga um restaurante.",
    auth=AuthapiKey()
)
def apagar_restaurante(request, restaurante_id: int):
    restaurante = get_object_or_404(Restaurante, id=restaurante_id)
    restaurante.delete()

    return 204, None


# ====================
# Utilizador
# ====================

@apiLegal.get(
    "utilizadores/",
    response={200: List[UtilizadorOut]},
    tags=["Utilizadores"],
    description="Lista todos os utilizadores registrados."
)
def listar_utilizadores(
    request,
    nome: str = None,
    email: str = None,
    sort: str = None,
    limit: int = 5,
    offset: int = 0
):
    utilizadores = Utilizador.objects.all()

    if nome is not None:
        utilizadores = utilizadores.filter(nome__icontains=nome)

    if email is not None:
        utilizadores = utilizadores.filter(email__icontains=email)

    if sort in (
        "nome", "-nome",
        "email", "-email"
    ):
        utilizadores = utilizadores.order_by(sort)

    utilizadores = utilizadores[offset:offset + limit]

    return 200, utilizadores


@apiLegal.get(
    "utilizadores/{utilizador_id}/",
    response={200: UtilizadorOut, 404: ErrorSchema},
    tags=["Utilizadores"],
    description="Busca por um utilizador a partir do id na API."
)
def buscar_utilizador(request, utilizador_id: int):
    try:
        return 200, Utilizador.objects.get(id=utilizador_id)
    except Utilizador.DoesNotExist:
        return 404, {"detail": "Utilizador não encontrado."}


@apiLegal.post(
    "utilizadores/",
    response={201: UtilizadorOut, 400: ErrorSchema},
    tags=["Utilizadores"],
    description="Cria um novo utilizador na API."
)
def criar_utilizador(request, data: UtilizadorIn):
    return 201, Utilizador.objects.create(**data.dict())


@apiLegal.put(
    "utilizadores/{utilizador_id}/",
    response={200: UtilizadorOut, 404: ErrorSchema},
    tags=["Utilizadores"],
    description="Atualiza os dados de um utilizador.",
    auth=AuthapiKey()
)
def atualizar_utilizador(request, utilizador_id: int, data: UtilizadorIn):
    updated = Utilizador.objects.filter(id=utilizador_id).update(**data.dict())

    if not updated:
        return 404, {"message": "Utilizador não encontrado."}

    return 200, Utilizador.objects.get(id=utilizador_id)


@apiLegal.delete(
    "utilizadores/{utilizador_id}/",
    response={204: None, 404: ErrorSchema},
    tags=["Utilizadores"],
    description="Apaga um utilizador.",
    auth=AuthapiKey()
)
def apagar_utilizador(request, utilizador_id: int):
    utilizador = get_object_or_404(Utilizador, id=utilizador_id)
    utilizador.delete()

    return 204, None




# ====================
# Ingrediente
# ====================

@apiLegal.get(
    "ingredientes/",
    response={200: List[IngredienteOut]},
    tags=["Ingredientes"],
    description="Lista todos os ingredientes registrados."
)
def listar_ingredientes(
    request,
    nome: str = None,
    sort: str = None,
    limit: int = 5,
    offset: int = 0
):
    ingredientes = Ingrediente.objects.all()

    if nome is not None:
        ingredientes = ingredientes.filter(nome__icontains=nome)

    if sort in ("nome", "-nome"):
        ingredientes = ingredientes.order_by(sort)

    ingredientes = ingredientes[offset:offset + limit]

    return 200, ingredientes


@apiLegal.get(
    "ingredientes/{ingrediente_id}/",
    response={200: IngredienteOut, 404: ErrorSchema},
    tags=["Ingredientes"],
    description="Busca por um ingrediente a partir do id na API."
)
def buscar_ingrediente(request, ingrediente_id: int):
    try:
        return 200, Ingrediente.objects.get(id=ingrediente_id)
    except Ingrediente.DoesNotExist:
        return 404, {"detail": "Ingrediente não encontrado."}


@apiLegal.post(
    "ingredientes/",
    response={201: IngredienteOut, 400: ErrorSchema},
    tags=["Ingredientes"],
    description="Cria um novo ingrediente na API."
)
def criar_ingrediente(request, data: IngredienteIn):
    return 201, Ingrediente.objects.create(**data.dict())


@apiLegal.put(
    "ingredientes/{ingrediente_id}/",
    response={200: IngredienteOut, 404: ErrorSchema},
    tags=["Ingredientes"],
    description="Atualiza os dados de um ingrediente.",
    auth=AuthapiKey()
)
def atualizar_ingrediente(request, ingrediente_id: int, data: IngredienteIn):
    updated = Ingrediente.objects.filter(id=ingrediente_id).update(**data.dict())

    if not updated:
        return 404, {"message": "Ingrediente não encontrado."}

    return 200, Ingrediente.objects.get(id=ingrediente_id)


@apiLegal.delete(
    "ingredientes/{ingrediente_id}/",
    response={204: None, 404: ErrorSchema},
    tags=["Ingredientes"],
    description="Apaga um ingrediente.",
    auth=AuthapiKey()
)
def apagar_ingrediente(request, ingrediente_id: int):
    ingrediente = get_object_or_404(Ingrediente, id=ingrediente_id)
    ingrediente.delete()

    return 204, None



# ====================
# Receita
# ====================

@apiLegal.get(
    "receitas/",
    response={200: List[ReceitaOut]},
    tags=["Receitas"],
    description="Lista todas as receitas registradas."
)
def listar_receitas(
    request,
    nome: str = None,
    sort: str = None,
    limit: int = 5,
    offset: int = 0
):
    receitas = Receita.objects.all()

    if nome is not None:
        receitas = receitas.filter(nome__icontains=nome)

    if sort in ("nome", "-nome"):
        receitas = receitas.order_by(sort)

    receitas = receitas[offset:offset + limit]

    return 200, receitas


@apiLegal.get(
    "receitas/{receita_id}/",
    response={200: ReceitaOut, 404: ErrorSchema},
    tags=["Receitas"],
    description="Busca por uma receita a partir do id na API."
)
def buscar_receita(request, receita_id: int):
    try:
        return 200, Receita.objects.get(id=receita_id)
    except Receita.DoesNotExist:
        return 404, {"detail": "Receita não encontrada."}


@apiLegal.post(
    "receitas/",
    response={201: ReceitaOut, 400: ErrorSchema},
    tags=["Receitas"],
    description="Cria uma nova receita na API."
)
def criar_receita(request, data: ReceitaIn):
    return 201, Receita.objects.create(**data.dict())


@apiLegal.put(
    "receitas/{receita_id}/",
    response={200: ReceitaOut, 404: ErrorSchema},
    tags=["Receitas"],
    description="Atualiza os dados de uma receita.",
    auth=AuthapiKey()
)
def atualizar_receita(request, receita_id: int, data: ReceitaIn):
    updated = Receita.objects.filter(id=receita_id).update(**data.dict())

    if not updated:
        return 404, {"message": "Receita não encontrada."}

    return 200, Receita.objects.get(id=receita_id)


@apiLegal.delete(
    "receitas/{receita_id}/",
    response={204: None, 404: ErrorSchema},
    tags=["Receitas"],
    description="Apaga uma receita.",
    auth=AuthapiKey()
)
def apagar_receita(request, receita_id: int):
    receita = get_object_or_404(Receita, id=receita_id)
    receita.delete()

    return 204, None



# ====================
# Piscina
# ====================

@apiLegal.get(
    "piscinas/",
    response={200: List[PiscinaOut]},
    tags=["Piscinas"],
    description="Lista todas as piscinas registradas."
)
def listar_piscinas(
    request,
    nome: str = None,
    localizacao: str = None,
    sort: str = None,
    limit: int = 5,
    offset: int = 0
):
    piscinas = Piscina.objects.all()

    if nome is not None:
        piscinas = piscinas.filter(nome__icontains=nome)

    if localizacao is not None:
        piscinas = piscinas.filter(localizacao__icontains=localizacao)

    if sort in (
        "nome", "-nome",
        "localizacao", "-localizacao"
    ):
        piscinas = piscinas.order_by(sort)

    piscinas = piscinas[offset:offset+limit]

    return 200, piscinas


@apiLegal.get(
    "piscinas/{piscina_id}/",
    response={200: PiscinaOut, 404: ErrorSchema},
    tags=["Piscinas"],
    description="Busca por uma piscina a partir do id na API."
)
def buscar_piscina(request, piscina_id: int):
    try:
        return 200, Piscina.objects.get(id=piscina_id)
    except Piscina.DoesNotExist:
        return 404, {"detail": "Piscina não encontrada."}


@apiLegal.post(
    "piscinas/",
    response={201: PiscinaOut, 400: ErrorSchema},
    tags=["Piscinas"],
    description="Cria uma nova piscina na API."
)
def criar_piscina(request, data: PiscinaIn):
    return 201, Piscina.objects.create(**data.dict())


@apiLegal.put(
    "piscinas/{piscina_id}/",
    response={200: PiscinaOut, 404: ErrorSchema},
    tags=["Piscinas"],
    description="Atualiza os dados de uma piscina.",
    auth=AuthapiKey()
)
def atualizar_piscina(request, piscina_id: int, data: PiscinaIn):
    updated = Piscina.objects.filter(id=piscina_id).update(**data.dict())

    if not updated:
        return 404, {"message": "Piscina não encontrada."}

    return 200, Piscina.objects.get(id=piscina_id)


@apiLegal.delete(
    "piscinas/{piscina_id}/",
    response={204: None, 404: ErrorSchema},
    tags=["Piscinas"],
    description="Apaga uma piscina.",
    auth=AuthapiKey()
)
def apagar_piscina(request, piscina_id: int):
    piscina = get_object_or_404(Piscina, id=piscina_id)
    piscina.delete()

    return 204, None




# ====================
# Treinador
# ====================

@apiLegal.get(
    "treinadores/",
    response={200: List[TreinadorOut]},
    tags=["Treinadores"],
    description="Lista todos os treinadores registrados."
)
def listar_treinadores(request, nome: str = None, sort: str = None, limit: int = 5, offset: int = 0):
    treinadores = Treinador.objects.all()

    if nome is not None:
        treinadores = treinadores.filter(nome__icontains=nome)

    if sort in ("nome", "-nome"):
        treinadores = treinadores.order_by(sort)

    treinadores = treinadores[offset:offset+limit]

    return 200, treinadores


@apiLegal.get(
    "treinadores/{treinador_id}/",
    response={200: TreinadorOut, 404: ErrorSchema},
    tags=["Treinadores"],
    description="Busca por um treinador a partir do id na API."
)
def buscar_treinador(request, treinador_id: int):
    try:
        return 200, Treinador.objects.get(id=treinador_id)
    except Treinador.DoesNotExist:
        return 404, {"detail": "Treinador não encontrado."}


@apiLegal.post(
    "treinadores/",
    response={201: TreinadorOut},
    tags=["Treinadores"],
    description="Cria um novo treinador na API."
)
def criar_treinador(request, data: TreinadorIn):
    return 201, Treinador.objects.create(**data.dict())


@apiLegal.put(
    "treinadores/{treinador_id}/",
    response={200: TreinadorOut, 404: ErrorSchema},
    tags=["Treinadores"],
    description="Atualiza os dados de um treinador.",
    auth=AuthapiKey()
)
def atualizar_treinador(request, treinador_id: int, data: TreinadorIn):
    updated = Treinador.objects.filter(id=treinador_id).update(**data.dict())

    if not updated:
        return 404, {"message": "Treinador não encontrado."}

    return 200, Treinador.objects.get(id=treinador_id)


@apiLegal.delete(
    "treinadores/{treinador_id}/",
    response={204: None, 404: ErrorSchema},
    tags=["Treinadores"],
    description="Apaga um treinador.",
    auth=AuthapiKey()
)
def apagar_treinador(request, treinador_id: int):
    treinador = get_object_or_404(Treinador, id=treinador_id)
    treinador.delete()

    return 204, None




# ====================
# Treino
# ====================

@apiLegal.get(
    "treinos/",
    response={200: List[TreinoOut]},
    tags=["Treinos"],
    description="Lista todos os treinos registrados."
)
def listar_treinos(
    request,
    data: date = None,
    sort: str = None,
    limit: int = 5,
    offset: int = 0
):
    treinos = Treino.objects.all()

    if data is not None:
        treinos = treinos.filter(data=data)

    if sort in (
        "data", "-data",
        "hora", "-hora"
    ):
        treinos = treinos.order_by(sort)

    treinos = treinos[offset:offset+limit]

    return 200, treinos


@apiLegal.get(
    "treinos/{treino_id}/",
    response={200: TreinoOut, 404: ErrorSchema},
    tags=["Treinos"],
    description="Busca por um treino a partir do id na API."
)
def buscar_treino(request, treino_id: int):
    try:
        return 200, Treino.objects.get(id=treino_id)
    except Treino.DoesNotExist:
        return 404, {"detail": "Treino não encontrado."}


@apiLegal.post(
    "treinos/",
    response={201: TreinoOut},
    tags=["Treinos"],
    description="Cria um novo treino na API."
)
def criar_treino(request, data: TreinoIn):
    return 201, Treino.objects.create(**data.dict())


@apiLegal.put(
    "treinos/{treino_id}/",
    response={200: TreinoOut, 404: ErrorSchema},
    tags=["Treinos"],
    description="Atualiza os dados de um treino.",
    auth=AuthapiKey()
)
def atualizar_treino(request, treino_id: int, data: TreinoIn):
    updated = Treino.objects.filter(id=treino_id).update(**data.dict())

    if not updated:
        return 404, {"message": "Treino não encontrado."}

    return 200, Treino.objects.get(id=treino_id)


@apiLegal.delete(
    "treinos/{treino_id}/",
    response={204: None, 404: ErrorSchema},
    tags=["Treinos"],
    description="Apaga um treino.",
    auth=AuthapiKey()
)
def apagar_treino(request, treino_id: int):
    treino = get_object_or_404(Treino, id=treino_id)
    treino.delete()

    return 204, None