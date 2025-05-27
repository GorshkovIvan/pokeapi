"""
Base resource models for the PokeAPI.
Defines common structures used across different API responses.
"""

from pydantic import BaseModel, ConfigDict

class NamedAPIResource(BaseModel):
    """Represents a resource that can be obtained from the PokeAPI."""
    name: str
    url: str

    model_config = ConfigDict(from_attributes=True) 