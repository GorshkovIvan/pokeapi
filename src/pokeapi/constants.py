"""
Constants used throughout the PokeAPI SDK.
Defines API endpoints, error messages, and configuration values.
"""

from typing import Final

# API Configuration
BASE_URL: Final = "https://pokeapi.co/api/v2"
POKEMON_ENDPOINT: Final = "/pokemon"
GENERATION_ENDPOINT: Final = "/generation"

# HTTP Settings
TIMEOUT: Final = 30
DEFAULT_HEADERS: Final = {
    "Accept": "application/json",
    "User-Agent": "PokeSDK/1.0"
}


# Error Messages
class ErrorMessages:
    NETWORK_ERROR = "Network error occurred: {}"
    RESOURCE_NOT_FOUND = "The requested resource was not found"
    SERVER_ERROR = "A server error occurred"
    EMPTY_PATH = "Path cannot be empty"
    INVALID_METHOD = "Only GET method is supported"
    TIMEOUT_ERROR = "Request timed out"
    CONNECTION_ERROR = "Failed to connect to server"
    EMPTY_POKEMON_ID = "Pokemon ID or name cannot be empty"
    INVALID_POKEMON_ID = "Pokemon ID must be a positive number: {}"
    INVALID_JSON_RESPONSE = "Invalid JSON response from server"
    INVALID_LIMIT = "Limit must be a positive number"
    INVALID_OFFSET = "Offset must be a positive number"
    EMPTY_GENERATION_ID = "Generation ID or name cannot be empty"
    INVALID_GENERATION_ID = "Generation ID must be a positive number: {}"
    GENERATION_ID_WRONG_TYPE = "Generation ID must be an integer. Did you mean to use name='{}'?"
    POKEMON_ID_WRONG_TYPE = "Pokemon ID must be an integer. Did you mean to use name='{}'?"