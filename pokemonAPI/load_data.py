# python pokemonAPI/load_data.py

import os
import json
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()

from decimal import Decimal
from pokemonAPI.models import Pokemon, Tipagem, Habitat, Treinador

def load_data(json_file_path):
    print(f"Lendo dados do arquivo {json_file_path}...")
    
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    print("Carregando Tipagens...")
    tipagens_dict = {}
    for tipagem_data in data['tipagens']:
        # get_or_create evita duplicatas se o script for rodado mais de uma vez
        tipagem, created = Tipagem.objects.get_or_create(nome=tipagem_data['nome'])
        tipagens_dict[tipagem.nome] = tipagem
        if created:
            print(f"  - Tipagem '{tipagem.nome}' criada.")
            
    print("\nCarregando Habitats...")
    habitats_dict = {}
    for habitat_data in data['habitats']:
        habitat, created = Habitat.objects.get_or_create(
            nome=habitat_data['nome'],
            defaults={'descricao': habitat_data['descricao']}
        )
        habitats_dict[habitat.nome] = habitat
        if created:
            print(f"  - Habitat '{habitat.nome}' criado.")
            
    print("\nCarregando Treinadores...")
    treinadores_dict = {}
    for treinador_data in data['treinadores']:
        treinador, created = Treinador.objects.get_or_create(
            nome=treinador_data['nome'],
            defaults={
                'cidade': treinador_data['cidade'],
                'idade': treinador_data['idade']
            }
        )
        treinadores_dict[treinador.nome] = treinador
        if created:
            print(f"  - Treinador '{treinador.nome}' criado.")
            
    print("\nCarregando Pokémons...")
    for pokemon_data in data['pokemons']:
        # Prepara o treinador se existir
        treinador = None
        if pokemon_data['treinador']:
            treinador = treinadores_dict.get(pokemon_data['treinador'])
            
        # Cria ou atualiza o Pokémon
        pokemon, created = Pokemon.objects.update_or_create(
            numero_pokedex=pokemon_data['numero_pokedex'],
            defaults={
                'nome': pokemon_data['nome'],
                'altura': Decimal(str(pokemon_data['altura'])),
                'peso': Decimal(str(pokemon_data['peso'])),
                'descricao': pokemon_data['descricao'],
                'treinador': treinador
            }
        )
        
        # Adiciona as relações ManyToMany (Tipagens)
        pokemon.tipagens.clear() # Limpa as antigas para garantir que ficará exatamente como no JSON
        for tipagem_nome in pokemon_data['tipagens']:
            if tipagem_nome in tipagens_dict:
                pokemon.tipagens.add(tipagens_dict[tipagem_nome])
                
        # Adiciona as relações ManyToMany (Habitats)
        pokemon.habitats.clear() # Limpa as antigas
        for habitat_nome in pokemon_data['habitats']:
            if habitat_nome in habitats_dict:
                pokemon.habitats.add(habitats_dict[habitat_nome])
                
        if created:
            print(f"  - Pokémon #{pokemon.numero_pokedex} {pokemon.nome} criado.")
        else:
            print(f"  - Pokémon #{pokemon.numero_pokedex} {pokemon.nome} atualizado.")
            
    print("\nCarga de dados concluída com sucesso!")

if __name__ == "__main__":
    # Como rodar este script:
    # 1. Coloque este arquivo na raiz do seu projeto Django (junto ao manage.py)
    # 2. Descomente as linhas de configuração do Django no topo deste arquivo
    # 3. Ajuste os imports para apontar para a sua app
    # 4. Execute: python load_data.py
    
    # Exemplo de execução (descomente quando for rodar de verdade):
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pokemon_data.json')
    load_data(json_path)
    print("Este é o script de carregamento. Leia os comentários para integrá-arlo ao seu projeto Django.")
