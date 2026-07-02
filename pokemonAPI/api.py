from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from typing import List
from .schemas import *
from .models import *


api = NinjaAPI(
    title="API RESTful sobre Pokemons",
    description="""
    Esta API RESTful foi desenvolvida com o objetivo de representar uma Pokédex da primeira geração de Pokémon.
    A aplicação permite gerir informações sobre Pokémon, os seus tipos, treinadores e habitats, estabelecendo relações entre
    estas entidades através de uma base de dados relacional. A API disponibiliza operações CRUD e segue os princípios da 
    arquitetura REST, facilitando a integração com aplicações cliente.""",
    version="1.0.0"
)



# ====================
# Pokemon
# ====================


# Listar todos os pokemons
@api.get(
    "pokemons/",
    response={200: List[PokemonOut]},
    tags=["Pokemons"],
    description="Lista todos os pokemons registrados."
)
def listar_pokemons(request,
    nome: str = None,
    numero_pokedex: int = None,
    altura: int = None,
    peso: int = None,
    sort: str = None,
    limit: int = 6,
    offset: int = 0
    ):
    pokemons = Pokemon.objects.all()

    if nome is not None:
        pokemons = pokemons.filter(nome__icontains=nome)

    if numero_pokedex is not None:
        pokemons = pokemons.filter(numero_pokedex=numero_pokedex)

    if altura is not None:
        pokemons = pokemons.filter(altura=altura)

    if peso is not None:
        pokemons = pokemons.filter(peso=peso)

    if sort in (
        "nome", "-nome",
        "numero_pokedex", "-numero_pokedex",
        "altura", "-altura",
        "peso", "-peso"
    ):
        pokemons = pokemons.order_by(sort)

    pokemons = pokemons[offset:offset+limit]

    return 200, pokemons


# Buscar por um pokemon a partir do id
@api.get(
    "pokemons/{pokemon_id}/",
    response={200: PokemonOut, 404: ErrorSchema},
    tags=["Pokemons"],
    description="Busca por um pokemon a partir do id na API."
)
def buscar_pokemon_com_id(request, pokemon_id: int):
    try:
        return 200, Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return 404, {"detail": "Pokemon não encontrado. Id inserido incorretamente ou não está cadastrado um pokemon com esse id"}


# Buscar por um pokemon a partir do numero na pokedex
@api.get(
    "pokemons/pokedex/{pokemon_numero_pokedex}/",
    response={200: PokemonOut, 404: ErrorSchema},
    tags=["Pokemons"],
    description="Busca por um pokemon a partir do número na Pokedex."
)
def buscar_pokemon_com_numero_na_pokedex(request, pokemon_numero_pokedex: int):
    try:
        return 200, Pokemon.objects.get(numero_pokedex=pokemon_numero_pokedex)
    except Pokemon.DoesNotExist:
        return 404, {"detail": "Pokemon não encontrado. Nenhum pokemon com essa numeração."}


# Criar um novo Pokemon
@api.post(
    "pokemons/",
    response={201: PokemonOut, 400: ErrorSchema},
    tags=["Pokemons"],
    description="Cria um novo pokemon na API"
)
def criar_pokemon(request, data: PokemonIn):
    tipagens = []
    habitats = []
    treinador = None

    dados = data.dict()

    dados.pop("tipagens")
    dados.pop("habitats")
    dados.pop("treinador", None)

    if data.treinador is not None:
        treinador, _ = Treinador.objects.get_or_create(
            nome=data.treinador.nome,
            defaults={
                "cidade": data.treinador.cidade,
                "idade": data.treinador.idade
            }
        )

    # Criar Pokémon
    pokemon = Pokemon.objects.create(**dados)

    # Associar treinador
    pokemon.treinador = treinador

    # Tipagens
    for tipo in data.tipagens:
        obj, _ = Tipagem.objects.get_or_create(
            nome=tipo.nome
        )
        tipagens.append(obj)

    pokemon.tipagens.set(tipagens)

    # Habitats
    for habitat in data.habitats:
        obj, _ = Habitat.objects.get_or_create(
            nome=habitat.nome,
            defaults={
                "descricao": habitat.descricao
            }
        )
        habitats.append(obj)

    pokemon.habitats.set(habitats)

    # Guardar alteração do treinador
    pokemon.save()

    return 201, pokemon


# Atualiza dados/informações de um pokemon
@api.put(
    "pokemons/{pokemon_id}",
    response={200: PokemonOut, 400: ErrorSchema, 404: ErrorSchema},
    tags=["Pokemons"],
    description="Atualiza dados de um pokemon na API"
)
def atualizar_pokemon(request, pokemon_id: int, data: PokemonUpdate):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return 404, {"detail": "Pokémon não encontrado. ID inserido incorretamente ou não existe um Pokémon com esse ID."}
    
    pokemon.nome = data.nome
    pokemon.altura = data.altura
    pokemon.peso = data.peso
    pokemon.descricao = data.descricao

    if data.treinador is not None:
        treinador, _ = Treinador.objects.get_or_create(
            nome=data.treinador.nome,
            defaults={
                "cidade": data.treinador.cidade,
                "idade": data.treinador.idade
            }
        )
        pokemon.treinador = treinador
    else:
        pokemon.treinador = None

    tipagens = []
    for tipo in data.tipagens:
        obj, _ = Tipagem.objects.get_or_create(nome=tipo.nome)
        tipagens.append(obj)
    pokemon.tipagens.set(tipagens)

    habitats = []
    for habitat in data.habitats:
        obj, _ = Habitat.objects.get_or_create(
            nome=habitat.nome,
            defaults={
                "descricao": habitat.descricao
            }
        )
        habitats.append(obj)
    pokemon.habitats.set(habitats)

    pokemon.save()

    return 200, pokemon


# Apagar um pokemon
@api.delete(
    "pokemons/{pokemon_id}",
    response={204: None, 404: ErrorSchema},
    tags=["Pokemons"],
    description="Apagar um pokemon na API"
)
def apagar_pokemon(request, pokemon_id: int):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
        pokemon.delete()
        return 204, None 
    except Pokemon.DoesNotExist:
        return 404, {"detail": "Pokemon não encontrado. Id inserido incorretamente ou não está cadastrado um pokemon com esse id."}



# ====================
# Tipagem
# ====================

# Listar todas as Tipagens
@api.get(
    "tipagens/",
    response={200: List[TipagemOut]},
    tags=["Tipagens"],
    description="Lista todas as tipagens registrados."
)
def listar_tipagens(request,
    nome: str = None,
    sort: str = None,
    limit: int = 5,
    offset: int = 0
    ):
    tipagens = Tipagem.objects.all()

    if nome is not None:
        tipagens = tipagens.filter(nome__icontains=nome)

    if sort in ('nome', '-nome'):
        tipagens = tipagens.order_by(sort)

    tipagens = tipagens[offset:offset+limit]

    return 200, tipagens


# Buscar por uma tipagem a partir do id
@api.get(
    "tipagens/{tipagem_id}/",
    response={200: TipagemOut, 404: ErrorSchema},
    tags=["Tipagens"],
    description="Busca por uma tipagem a partir do id na API."
)
def buscar_tipagem(request, tipagem_id: int):
    try:
        return 200, Tipagem.objects.get(id=tipagem_id)
    except Tipagem.DoesNotExist:
        return 404, {"detail": "Tipagem não encontrado. Id inserido incorretamente ou não está cadastrado uma tipagem com esse id."}


# Criar uma nova Tipagem
@api.post(
    "tipagens/",
    response={201: TipagemOut, 400: ErrorSchema},
    tags=["Tipagens"],
    description="Cria uma nova tipagem na API"
)
def criar_tipagem(request, data: TipagemIn):
    return 201, Tipagem.objects.create(**data.dict())


# Atualiza dados/informações de uma tipagem
@api.put(
    "tipagens/{tipagem_id}",
    response={200: TipagemOut, 404: ErrorSchema},
    tags=["Tipagens"],
    description="Atualiza dados de uma tipagem na API"
)
def atualizar_tipagem(request, tipagem_id: int, data: TipagemIn):
    updated = Tipagem.objects.filter(id=tipagem_id).update(**data.dict())

    if not updated:
        return 404, {"message": "Tipagem não encontrado. Id inserido incorretamente ou não está cadastrado uma tipagem com esse id."}

    tipagem = Tipagem.objects.get(id=tipagem_id)

    return 200, tipagem


# Apagar uma tipagem
@api.delete(
    "tipagens/{tipagem_id}/",
    response={204: None, 404: ErrorSchema},
    tags=["Tipagens"],
    description="Apagar uma tipagem"
)
def apagar_tipagem(request, tipagem_id: int):
    tipagem = get_object_or_404(Tipagem, id=tipagem_id)
    tipagem.delete()

    return 204, None



# ====================
# Habitat
# ====================

# Listar todos os habitats
@api.get(
    "habitats/",
    response={200: List[HabitatOut]},
    tags=["Habitats"],
    description="Lista todos os habitats registrados."
)
def listar_habitats(request,
    nome: str = None,
    descricao: str = None,
    sort: str = None,
    limit: int = 5,
    offset: int = 0
    ):
    habitats = Habitat.objects.all()

    if nome is not None:
        habitats = habitats.filter(nome__icontains=nome)

    if descricao is not None:
        habitats = habitats.filter(descricao__icontains=descricao)

    if sort in (
        'nome', '-nome',
        'descricao', '-descricao'
    ):
        habitats = habitats.order_by(sort)

    habitats = habitats[offset:offset+limit]

    return 200, habitats


# Buscar por um habitat a partir do id
@api.get(
    "habitats/{habitat_id}/",
    response={200: HabitatOut, 404: ErrorSchema},
    tags=["Habitats"],
    description="Busca por um habitat a partir do id na API."
)
def buscar_habitat(request, habitat_id: int):
    try:
        return 200, Habitat.objects.get(id=habitat_id)
    except Habitat.DoesNotExist:
        return 404, {"detail": "Habitat não encontrado. Id inserido incorretamente ou não está cadastrado um habitat com esse id."}


# Criar um novo Habitat
@api.post(
    "habitats/",
    response={201: HabitatOut, 400: ErrorSchema},
    tags=["Habitats"],
    description="Cria um novo habitat na API"
)
def criar_habitat(request, data: HabitatIn):
    return 201, Habitat.objects.create(**data.dict())


# Atualiza dados/informações de um habitat
@api.put(
    "habitats/{habitat_id}",
    response={200: HabitatOut, 404: ErrorSchema},
    tags=["Habitats"],
    description="Atualiza dados de um habitat na API"
)
def atualizar_habitat(request, habitat_id: int, data: HabitatIn):
    updated = Habitat.objects.filter(id=habitat_id).update(**data.dict())

    if not updated:
        return 404, {"message": "Habitat não encontrado. Id inserido incorretamente ou não está cadastrado um habitat com esse id."}

    habitat = Habitat.objects.get(id=habitat_id)

    return 200, habitat


# Apagar um habitat
@api.delete(
    "habitats/{habitat_id}/",
    response={204: None, 404: ErrorSchema},
    tags=["Habitats"],
    description="Apagar um habitat"
)
def apagar_habitat(request, habitat_id: int):
    habitat = get_object_or_404(Habitat, id=habitat_id)
    habitat.delete()

    return 204, None



# ====================
# Treinador
# ====================

# Listar todos os treinadores
@api.get(
    "treinadores/",
    response={200: List[TreinadorOut]},
    tags=["Treinadores"],
    description="Lista todos os treinadores registrados."
)
def listar_treinadores(request,
    nome: str = None,
    cidade: str = None,
    idade: int = None,
    sort: str = None,
    limit: int = 5,
    offset: int = 0
    ):
    treinadores = Treinador.objects.all()

    if nome is not None:
        treinadores = treinadores.filter(nome__icontains=nome)

    if cidade is not None:
        treinadores = treinadores.filter(cidade__icontains=cidade)

    if sort in (
        'nome', '-nome',
        'cidade', '-cidade',
        'idade', '-idade'
    ):
        treinadores = treinadores.order_by(sort)

    treinadores = treinadores[offset:offset+limit]

    return 200, treinadores


# Buscar por um treinador a partir do id
@api.get(
    "treinadores/{treinador_id}/",
    response={200: TreinadorOut, 404: ErrorSchema},
    tags=["Treinadores"],
    description="Busca por um treinador a partir do id na API."
)
def buscar_treinador(request, treinador_id: int):
    try:
        return 200, Treinador.objects.get(id=treinador_id)
    except Treinador.DoesNotExist:
        return 404, {"detail": "Treinador não encontrado. Id inserido incorretamente ou não está cadastrado um treinador com esse id."}


# Criar um novo Habitat
@api.post(
    "treinadores/",
    response={201: TreinadorOut, 400: ErrorSchema},
    tags=["Treinadores"],
    description="Cria um novo treinador na API"
)
def criar_treinador(request, data: TreinadorIn):
    return 201, Treinador.objects.create(**data.dict())


# Atualiza dados/informações de um treinador
@api.put(
    "treinadores/{treinador_id}",
    response={200: TreinadorOut, 404: ErrorSchema},
    tags=["Treinadores"],
    description="Atualiza dados de um treinador na API"
)
def atualizar_treinadores(request, treinador_id: int, data: TreinadorIn):
    updated = Treinador.objects.filter(id=treinador_id).update(**data.dict())

    if not updated:
        return 404, {"message": "Treinador não encontrado. Id inserido incorretamente ou não está cadastrado um treinador com esse id."}

    treinador = Treinador.objects.get(id=treinador_id)

    return 200, treinador


# Apagar um treinador
@api.delete(
    "treinadores/{treinador_id}/",
    response={204: None, 404: ErrorSchema},
    tags=["Treinadores"],
    description="Apagar um treinador"
)
def apagar_treinador(request, treinador_id: int):
    treinador = get_object_or_404(Treinador, id=treinador_id)
    treinador.delete()

    return 204, None

    