from ninja import Schema
from typing import List, Optional
from datetime import date, time

class RestauranteIn(Schema):
    nome: str
    localizacao: str
    capacidade: int

class RestauranteOut(RestauranteIn):
    id: int


class ClienteIn(Schema):
    nome: str


class ClienteOut(ClienteIn):
    id: int

class PratoIn(Schema):
    nome: str
    restaurante_id: int


class PratoOut(PratoIn):
    id: int

class ReservaIn(Schema):
    data: date
    hora: time
    numero_pessoas: int
    restaurante_id: int
    cliente_id: int


class ReservaOut(ReservaIn):
    id: int


    
class ErrorSchema(Schema):
    detail: str


class UtilizadorIn(Schema):
    nome: str
    email: str


class UtilizadorOut(UtilizadorIn):
    id: int


class IngredienteIn(Schema):
    nome: str


class IngredienteOut(IngredienteIn):
    id: int


class ReceitaIn(Schema):
    nome: str
    descricao: str
    utilizador_id: int


class ReceitaOut(ReceitaIn):
    id: int




class PiscinaIn(Schema):
    nome: str
    localizacao: str


class PiscinaOut(PiscinaIn):
    id: int


class TreinadorIn(Schema):
    nome: str


class TreinadorOut(TreinadorIn):
    id: int


class NadadorIn(Schema):
    nome: str


class NadadorOut(NadadorIn):
    id: int


class EstiloIn(Schema):
    nome: str


class EstiloOut(EstiloIn):
    id: int


class TreinoIn(Schema):
    data: date
    hora: time
    piscina_id: int
    treinador_id: int


class TreinoOut(TreinoIn):
    id: int