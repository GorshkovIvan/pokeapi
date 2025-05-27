"""
HTTP GET client implementation for the PokeAPI.
Handles URL building and request execution for GET operations.
"""

from urllib.parse import urlencode
import requests
from typing import Union
from .base import BaseHttpClient
from ..constants import DEFAULT_HEADERS, TIMEOUT, ErrorMessages
from ..exceptions import PokeAPIError

class HttpGetClient(BaseHttpClient):
    """HTTP client implementation for making GET requests to the PokeAPI."""

    def build_url(self, path: str, params: Union[str, dict]) -> str:
        """
        Build URL with proper parameter handling.

        Args:
            path (str): API endpoint path
            params (Union[str, dict]): Either resource ID/name as string or
                query params as dict

        Returns:
            str: The complete URL

        Raises:
            PokeAPIError: If path is empty
        """
        if not path:
            raise PokeAPIError(ErrorMessages.EMPTY_PATH)

        # Handle dictionary params (for pagination)
        if isinstance(params, dict):
            query_string = urlencode(params)
            return f"{self.base_url}{path}?{query_string}"

        # Handle string params (for resource ID/name)
        return f"{self.base_url}{path}/{params}"

    def request(self, method: str, path: str, params: Union[str, dict]):
        """
        Make an HTTP GET request.

        Args:
            method (str): Must be "GET"
            path (str): API endpoint path
            params (Union[str, dict]): Query parameters or resource identifier

        Returns:
            The HTTP response

        Raises:
            PokeAPIError: For various error conditions including invalid method,
                timeout, connection errors, etc.
        """
        if method.upper() != "GET":
            raise PokeAPIError(ErrorMessages.INVALID_METHOD)

        try:
            url = self.build_url(path, params)
            response = requests.get(
                url, headers=DEFAULT_HEADERS, timeout=TIMEOUT
            )
            return self._handle_response(response)
        except requests.exceptions.Timeout:
            raise PokeAPIError(ErrorMessages.TIMEOUT_ERROR)
        except requests.exceptions.ConnectionError:
            raise PokeAPIError(ErrorMessages.CONNECTION_ERROR)
        except Exception as e:
            raise PokeAPIError(ErrorMessages.NETWORK_ERROR.format(str(e)))

    def get(self, path: str, params: Union[str, dict]):
        """
        Convenience method for making GET requests.

        Args:
            path (str): API endpoint path
            params (Union[str, dict]): Query parameters or resource identifier

        Returns:
            The HTTP response
        """
        return self.request("GET", path, params)