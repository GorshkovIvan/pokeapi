# tests/unit/test_generation_client.py

import pytest
from src.pokeapi.api_clients.generation_client import GenerationClient
from src.pokeapi.exceptions import PokeAPIError
from src.pokeapi.models.generation import Generation
from src.pokeapi.models.pagination import NamedAPIResourceList

@pytest.fixture
def client():
    """Fixture that provides a GenerationClient instance"""
    return GenerationClient()

def test_get_generation_by_id(client):
    """Test that get_generation returns a Generation object"""
    generation = client.get_generation(generation_id=1)
    assert isinstance(generation, Generation)
    assert generation.name == "generation-i"

def test_get_generation_by_name(client):
    """Test that get_generation returns a Generation object when using name"""
    generation = client.get_generation(name="generation-i")
    assert isinstance(generation, Generation)
    assert generation.id == 1

def test_get_generation_invalid_id(client):
    """Test that negative or zero ID raises an error"""
    with pytest.raises(PokeAPIError) as exc:
        client.get_generation(generation_id=-1)
    assert "Generation ID must be a positive number: -1" in str(exc.value)

def test_get_generation_empty_name(client):
    """Test that empty name/id raises an error"""
    with pytest.raises(PokeAPIError) as exc:
        client.get_generation(name="")
    assert "Generation ID or name cannot be empty" in str(exc.value)

def test_get_generation_no_params(client):
    """Test that not providing any params raises an error"""
    with pytest.raises(PokeAPIError) as exc:
        client.get_generation()
    assert "Generation ID or name cannot be empty" in str(exc.value)

def test_list_generations(client):
    """Test that list_generations returns a NamedAPIResourceList"""
    generation_list = client.list_generations(limit=2)
    assert isinstance(generation_list, NamedAPIResourceList)
    assert len(generation_list.results) == 2

def test_list_generations_pagination(client):
    """Test that list_generations returns a NamedAPIResourceList with pagination"""
    generation_list = client.list_generations(limit=2, offset=2)
    assert isinstance(generation_list, NamedAPIResourceList)
    assert len(generation_list.results) == 2



