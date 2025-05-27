"""
Models for Pokemon generation data from the PokeAPI.
Defines structures for generations and their associated resources.
"""

from typing import List
from pydantic import BaseModel, ConfigDict
from .api_resource import NamedAPIResource

class Name(BaseModel):
    """Represents a localized name and its language."""
    name: str
    language: NamedAPIResource
    model_config = ConfigDict(from_attributes=True)

class Generation(BaseModel):
    """Represents a Pokemon generation with its region, species, moves and other attributes."""
    id: int
    name: str
    abilities: List[NamedAPIResource]
    names: List[Name]
    main_region: NamedAPIResource
    moves: List[NamedAPIResource]
    pokemon_species: List[NamedAPIResource]
    types: List[NamedAPIResource]
    version_groups: List[NamedAPIResource]
    model_config = ConfigDict(from_attributes=True)
