# tests/integration/test_pokemon_client.py

import pytest
from src.pokeapi.api_clients.pokemon_client import PokemonClient
from src.pokeapi.exceptions import PokeAPIError
from src.pokeapi.models.pokemon import Pokemon
from src.pokeapi.models.pagination import NamedAPIResourceList

@pytest.fixture
def client():
    """Fixture that provides a PokemonClient instance"""
    return PokemonClient()

def test_get_pokemon_by_id(client):
    """Test that get_pokemon returns a Pokemon object"""
    pokemon = client.get_pokemon(pokemon_id=1)
    assert isinstance(pokemon, Pokemon)
    assert pokemon.name == "bulbasaur"

def test_get_pokemon_by_name(client):
    """Test that get_pokemon returns a Pokemon object when using name"""
    pokemon = client.get_pokemon(name="pikachu")
    assert isinstance(pokemon, Pokemon)
    assert pokemon.name == "pikachu"

def test_get_pokemon_invalid_id(client):
    """Test that negative or zero ID raises an error"""
    with pytest.raises(PokeAPIError) as exc:
        client.get_pokemon(pokemon_id=-1)
    assert "Pokemon ID must be a positive number: -1" in str(exc.value)

def test_get_pokemon_empty_name(client):
    """Test that empty name/id raises an error"""
    with pytest.raises(PokeAPIError) as exc:
        client.get_pokemon(name="")
    assert "Pokemon ID or name cannot be empty" in str(exc.value)

def test_get_pokemon_no_params(client):
    """Test that not providing any params raises an error"""
    with pytest.raises(PokeAPIError) as exc:
        client.get_pokemon()
    assert "Pokemon ID or name cannot be empty" in str(exc.value)

def test_list_pokemon(client):
    """Test that list_pokemon returns a NamedAPIResourceList"""
    pokemon_list = client.list_pokemon(limit=1)
    assert isinstance(pokemon_list, NamedAPIResourceList)
    assert len(pokemon_list.results) == 1


# test pagination and limits for the list_pokemon method and list_generations method
def test_list_pokemon_pagination(client):
    """Test that list_pokemon returns a NamedAPIResourceList with pagination"""
    pokemon_list = client.list_pokemon(limit=1, offset=1)
    assert isinstance(pokemon_list, NamedAPIResourceList)
    assert len(pokemon_list.results) == 1

def test_list_pokemon_limit(client):
    """Test that list_pokemon returns a NamedAPIResourceList with limit"""
    pokemon_list = client.list_pokemon(limit=1)
    assert isinstance(pokemon_list, NamedAPIResourceList)
    assert len(pokemon_list.results) == 1


def test_list_pokemon_limit_and_offset(client):
    """Test that list_pokemon returns a NamedAPIResourceList with limit and offset"""
    pokemon_list = client.list_pokemon(limit=1, offset=1)
    assert isinstance(pokemon_list, NamedAPIResourceList)
    assert len(pokemon_list.results) == 1





