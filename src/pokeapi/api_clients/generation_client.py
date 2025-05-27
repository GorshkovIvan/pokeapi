"""
Client for interacting with the Generation endpoints of the PokeAPI.
Provides methods to fetch individual generations and list all generations.
"""

from ..connection.get import HttpGetClient
from ..models.generation import Generation
from ..constants import BASE_URL, GENERATION_ENDPOINT, ErrorMessages
from ..exceptions import PokeAPIError
from ..models.pagination import NamedAPIResourceList


class GenerationClient(HttpGetClient):
    """A client for interacting with Pokemon generation endpoints."""

    def __init__(self):
        super().__init__(BASE_URL)
        self.generation_path = GENERATION_ENDPOINT

    def get_generation(
        self, generation_id: int = None, name: str = None
    ) -> Generation:
        """
        Get a specific Pokemon generation by ID or name.

        Args:
            generation_id (int, optional): The ID of the generation to get.
            name (str, optional): The name of the generation to get.

        Returns:
            Generation: The requested generation data.

        Raises:
            PokeAPIError: If neither id nor name is provided, or if id is not positive,
                         or if id is provided as string.
        """
        if generation_id is not None and not isinstance(generation_id, int):
            raise PokeAPIError(
                ErrorMessages.GENERATION_ID_WRONG_TYPE.format(generation_id)
            )

        if generation_id is None and (name is None or name == ""):
            raise PokeAPIError(ErrorMessages.EMPTY_GENERATION_ID)

        if generation_id is not None:
            if generation_id <= 0:
                raise PokeAPIError(
                    ErrorMessages.INVALID_GENERATION_ID.format(generation_id)
                )
            id_or_name = str(generation_id)
        else:
            id_or_name = name

        try:
            response = self.get(self.generation_path, id_or_name)
            return Generation(**response.json())
        except ValueError:
            raise PokeAPIError(ErrorMessages.INVALID_JSON_RESPONSE)

    def list_generations(
        self, limit: int = 20, offset: int = 0
    ) -> NamedAPIResourceList:
        """
        Get a paginated list of Pokemon generations.

        Args:
            limit (int, optional): Number of generations to return. Defaults to 20.
            offset (int, optional): Starting position in the list. Defaults to 0.

        Returns:
            NamedAPIResourceList: Paginated list of generation resources.

        Raises:
            PokeAPIError: If limit or offset is negative.
        """
        if limit < 0:
            raise PokeAPIError(ErrorMessages.INVALID_LIMIT)
        if offset < 0:
            raise PokeAPIError(ErrorMessages.INVALID_OFFSET)

        try:
            params = {'limit': limit, 'offset': offset}
            response = self.get(self.generation_path, params)
            return NamedAPIResourceList(**response.json())
        except ValueError:
            raise PokeAPIError(ErrorMessages.INVALID_JSON_RESPONSE)
