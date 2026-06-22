from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from typing import List
from .schemas import *
from .models import *


api = NinjaAPI(
    title="API RESTful sobre Pokemons",
    description="API para gerir pokemons",
    version="1.0.0"
)


@api.get(
    "pokemons",
    response={200: List[PokemonOut]},
    tags=["Pokemons"],
    description="Lista todos os pokemons"
)
def listar_pokemons(request):
    pokemons = Pokemon.objects.all()

    return 200, pokemons