"""
Main SDK interface for interacting with the PokeAPI.
Provides a simplified interface for accessing Pokemon and Generation data.
"""

from ..api_clients.pokemon_client import PokemonClient
from ..api_clients.generation_client import GenerationClient
from ..models.pokemon import Pokemon
from ..models.generation import Generation
from ..models.pagination import NamedAPIResourceList


class PokeAPI:
    """
    Main entry point for the Pokemon API SDK.
    Provides access to all API functionality through a single interface.

    Usage:
        api = PokeAPI()
        
        # Pokemon operations
        pikachu = api.pokemon.get_pokemon("pikachu")
        pokemon_list = api.pokemon.list_pokemon(limit=5)
        
        # Generation operations
        gen1 = api.generation.get_generation("1")
        generations = api.generation.list_generations()
    """

    def __init__(self):
        """Initialize the PokeAPI with Pokemon and Generation clients."""
        self.pokemon = PokemonClient()
        self.generation = GenerationClient()

    def get_pokemon(
        self, pokemon_id: int = None, name: str = None
    ) -> Pokemon:
        """
        Get a specific Pokemon by ID or name.

        Args:
            pokemon_id (int, optional): The ID of the Pokemon to get
            name (str, optional): The name of the Pokemon to get

        Returns:
            Pokemon: The requested Pokemon data
        """
        return self.pokemon.get_pokemon(pokemon_id, name)

    def list_pokemon(
        self, limit: int = 20, offset: int = 0
    ) -> NamedAPIResourceList:
        """
        Get a paginated list of Pokemon.

        Args:
            limit (int, optional): Number of Pokemon to return. Defaults to 20
            offset (int, optional): Starting position in the list. Defaults to 0

        Returns:
            NamedAPIResourceList: Paginated list of Pokemon resources
        """
        return self.pokemon.list_pokemon(limit, offset)

    def get_generation(
        self, generation_id: int = None, name: str = None
    ) -> Generation:
        """
        Get a specific Pokemon generation by ID or name.

        Args:
            generation_id (int, optional): The ID of the generation to get
            name (str, optional): The name of the generation to get

        Returns:
            Generation: The requested generation data
        """
        return self.generation.get_generation(generation_id, name)

    def list_generations(
        self, limit: int = 20, offset: int = 0
    ) -> NamedAPIResourceList:
        """
        Get a paginated list of Pokemon generations.

        Args:
            limit (int, optional): Number of generations to return. Defaults to 20
            offset (int, optional): Starting position in the list. Defaults to 0

        Returns:
            NamedAPIResourceList: Paginated list of generation resources
        """
        return self.generation.list_generations(limit, offset)
    
    