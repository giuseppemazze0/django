from ninja import Schema
from typing import List, Optional

class TipagemIn(Schema):
    nome: str

class TipagemOut(TipagemIn):
    id: int



class HabitatIn(Schema):
    nome: str
    descricao: str

class HabitatOut(HabitatIn):
    id: int



class TreinadorIn(Schema):
    nome: str
    cidade: str
    idade: int

class TreinadorOut(TreinadorIn):
    id: int



class PokemonIn(Schema):
    nome: str
    numero_pokedex: int
    altura: float
    peso: float
    descricao: str
    tipagens: List[TipagemIn]
    habitats: List[HabitatIn]
    treinador: Optional[TreinadorIn] = None

class PokemonOut(PokemonIn):
    id: int
    tipagens: List[TipagemOut]
    habitats: List[HabitatOut]
    treinador: Optional[TreinadorOut] = None

# Nao tem o campo numero_pokedex
class PokemonUpdate(Schema):
    nome: str
    altura: float
    peso: float
    descricao: str
    tipagens: List[TipagemIn]
    habitats: List[HabitatIn]
    treinador: Optional[TreinadorIn] = None

#class PokemonCreate(Schema):
#    nome: str
#    numero_pokedex: int
#    altura: float
#    peso: float
#    descricao: str
#    tipagens_ids: List[int]
#    habitats_ids: List[int]
#    treinador_id: int



class ErrorSchema(Schema):
    detail: str