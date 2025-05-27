"""
Client implementations for different PokeAPI endpoints.
Provides Pokemon and Generation clients.
"""
from .pokemon_client import PokemonClient
from .generation_client import GenerationClient

__all__ = ['PokemonClient', 'GenerationClient'] 