"""
Base HTTP client functionality for making API requests.
Provides abstract base classes and common error handling.
"""

import requests
from typing import Union
from abc import ABC, abstractmethod
from ..constants import ErrorMessages
from ..exceptions import PokeAPIError

class BaseHttpClient(ABC):
    """Base abstract class for HTTP clients with common functionality."""

    def __init__(self, base_url: str):
        """
        Initialize the HTTP client.

        Args:
            base_url (str): The base URL for all API requests
        """
        self.base_url = base_url

    def _handle_response(self, response: requests.Response) -> requests.Response:
        """
        Handle API response and errors.

        Args:
            response: The HTTP response object

        Returns:
            The response if successful

        Raises:
            PokeAPIError: For various HTTP error conditions
        """
        try:
            response.raise_for_status()
            return response
        except Exception as e:
            if response.status_code == 404:
                raise PokeAPIError(ErrorMessages.RESOURCE_NOT_FOUND)
            elif response.status_code >= 500:
                raise PokeAPIError(ErrorMessages.SERVER_ERROR)
            else:
                raise PokeAPIError(
                    ErrorMessages.NETWORK_ERROR.format(str(e))
                )

    @abstractmethod
    def build_url(self, path: str, params: Union[str, dict]) -> str:
        """
        Build the full URL for the request.

        Args:
            path (str): The API endpoint path
            params (str): Query parameters or resource identifier

        Returns:
            str: The complete URL
        """
        pass

    @abstractmethod
    def request(self, method: str, path: str):
        """
        Make an HTTP request.

        Args:
            method (str): The HTTP method to use
            path (str): The API endpoint path

        Returns:
            The HTTP response
        """
        pass