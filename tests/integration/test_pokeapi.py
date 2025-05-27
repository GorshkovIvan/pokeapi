# tests/integration/test_pokeapi.py

import pytest
from src.pokeapi.sdk import PokeAPI
from src.pokeapi.api_clients.pokemon_client import PokemonClient
from src.pokeapi.api_clients.generation_client import GenerationClient
from src.pokeapi.models.pokemon import Pokemon
from src.pokeapi.models.generation import Generation

@pytest.fixture
def api():
    return PokeAPI()

def test_pokemon_client_initialization(api):
    """Test that pokemon client is properly initialized"""
    assert isinstance(api.pokemon, PokemonClient)

def test_generation_client_initialization(api):
    """Test that generation client is properly initialized"""
    assert isinstance(api.generation, GenerationClient)

def test_get_pokemon_by_id(api):
    """Test getting pokemon through main API"""
    pokemon = api.pokemon.get_pokemon(pokemon_id=1)
    assert isinstance(pokemon, Pokemon)
    assert pokemon.name == "bulbasaur"

def test_get_generation_by_id(api):
    """Test getting generation through main API"""
    generation = api.generation.get_generation(generation_id=1)
    assert isinstance(generation, Generation)
    assert generation.name == "generation-i"

def test_pokemon_base_attributes(api):
    """Test that Pokemon base attributes are correct"""
    charizard = api.get_pokemon(pokemon_id=6)
    assert charizard.height == 17  
    assert charizard.weight == 905 
    assert charizard.base_experience == 267
    assert charizard.is_default is True

def test_pokemon_types(api):
    """Test that Pokemon types are correct"""
    gengar = api.get_pokemon(pokemon_id=94)
    types = [t.type.name for t in gengar.types]
    assert len(types) == 2
    assert "ghost" in types
    assert "poison" in types

def test_pokemon_abilities(api):
    """Test that Pokemon abilities are correct"""
    pikachu = api.get_pokemon(name="pikachu")
    abilities = [(a.ability.name, a.is_hidden) for a in pikachu.abilities]
    assert ("static", False) in abilities  # Regular ability
    assert ("lightning-rod", True) in abilities  # Hidden ability

def test_generation_main_region(api):
    """Test that generation's main region is correct"""
    gen2 = api.get_generation(generation_id=2)
    assert gen2.main_region.name == "johto"
    assert len(gen2.version_groups) == 2  # Gold/Silver and Crystal

def test_generation_pokemon_species(api):
    """Test that generation contains correct Pokemon species"""
    gen1 = api.get_generation(generation_id=1)
    species_names = [species.name for species in gen1.pokemon_species]
    assert len(species_names) == 151  # Gen 1 has 151 Pokemon
    assert "bulbasaur" in species_names
    assert "mew" in species_names

def test_generation_type_changes(api):
    """Test that generation contains correct type information"""
    gen6 = api.get_generation(generation_id=6)
    type_names = [t.name for t in gen6.types]
    assert "fairy" in type_names  # Fairy type was introduced in Gen 6
