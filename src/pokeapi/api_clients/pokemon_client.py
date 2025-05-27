"""
Client for interacting with the Pokemon endpoints of the PokeAPI.
Provides methods to fetch individual Pokemon and list all Pokemon.
"""

from ..connection.get import HttpGetClient
from ..models.pokemon import Pokemon
from ..constants import BASE_URL, POKEMON_ENDPOINT, ErrorMessages
from ..exceptions import PokeAPIError
from ..models.pagination import NamedAPIResourceList


class PokemonClient(HttpGetClient):
    """A client for interacting with Pokemon endpoints."""

    def __init__(self):
        super().__init__(BASE_URL)
        self.pokemon_path = POKEMON_ENDPOINT

    def get_pokemon(
        self, pokemon_id: int = None, name: str = None
    ) -> Pokemon:
        """
        Get a specific Pokemon by ID or name.

        Args:
            pokemon_id (int, optional): The ID of the Pokemon to get.
            name (str, optional): The name of the Pokemon to get.

        Returns:
            Pokemon: The requested Pokemon data.

        Raises:
            PokeAPIError: If neither id nor name is provided, or if id is not positive,
                         or if id is provided as string.
        """
        if pokemon_id is not None and not isinstance(pokemon_id, int):
            raise PokeAPIError(
                ErrorMessages.POKEMON_ID_WRONG_TYPE.format(pokemon_id)
            )

        if pokemon_id is None and (name is None or name == ""):
            raise PokeAPIError(ErrorMessages.EMPTY_POKEMON_ID)

        if pokemon_id is not None:
            if pokemon_id <= 0:
                raise PokeAPIError(
                    ErrorMessages.INVALID_POKEMON_ID.format(pokemon_id)
                )
            id_or_name = str(pokemon_id)
        else:
            id_or_name = name

        try:
            response = self.get(self.pokemon_path, id_or_name)
            return Pokemon(**response.json())
        except ValueError:
            raise PokeAPIError(ErrorMessages.INVALID_JSON_RESPONSE)

    def list_pokemon(
        self, limit: int = 20, offset: int = 0
    ) -> NamedAPIResourceList:
        """
        Get a paginated list of Pokemon.

        Args:
            limit (int, optional): Number of Pokemon to return. Defaults to 20.
            offset (int, optional): Starting position in the list. Defaults to 0.

        Returns:
            NamedAPIResourceList: Paginated list of Pokemon resources.

        Raises:
            PokeAPIError: If limit or offset is negative.
        """
        if limit < 0:
            raise PokeAPIError(ErrorMessages.INVALID_LIMIT)
        if offset < 0:
            raise PokeAPIError(ErrorMessages.INVALID_OFFSET)

        try:
            params = {'limit': limit, 'offset': offset}
            response = self.get(self.pokemon_path, params)
            return NamedAPIResourceList(**response.json())
        except ValueError:
            raise PokeAPIError(ErrorMessages.INVALID_JSON_RESPONSE)
        

