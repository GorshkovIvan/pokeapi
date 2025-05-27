"""
Custom exceptions for the PokeAPI SDK.
Defines error types specific to API operations and validation.
"""

class PokeAPIError(Exception):
    """Base exception for PokeAPI errors"""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
