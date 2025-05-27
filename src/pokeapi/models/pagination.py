"""
Models for paginated responses from the PokeAPI.
Defines structures for handling paginated lists of resources.
"""

from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from .api_resource import NamedAPIResource

class NamedAPIResourceList(BaseModel):
    """Represents a paginated list of API resources with navigation links."""
    count: int
    next: Optional[str] = None
    previous: Optional[str] = None
    results: List[NamedAPIResource]

    model_config = ConfigDict(from_attributes=True)