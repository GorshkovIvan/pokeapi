"""
Models for Pokemon data from the PokeAPI.
Defines structures for Pokemon and their associated attributes.
"""

from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from .api_resource import NamedAPIResource

class PokemonAbility(BaseModel):
    """Represents a Pokemon's ability with its slot and hidden status."""
    is_hidden: bool
    slot: int
    ability: Optional[NamedAPIResource] = None 
    model_config = ConfigDict(from_attributes=True)

class PokemonType(BaseModel):
    """Represents one of a Pokemon's types and its slot position."""
    slot: int
    type: NamedAPIResource

class PokemonFormType(BaseModel):
    """Represents a Pokemon form's type and its slot position."""
    slot: int
    type: NamedAPIResource

class PokemonTypePast(BaseModel):
    """Represents a Pokemon's type in a previous generation."""
    generation: NamedAPIResource
    types: List[PokemonType]

class PokemonAbilityPast(BaseModel):
    """Represents a Pokemon's abilities in a previous generation."""
    generation: NamedAPIResource
    abilities: Optional[List[PokemonAbility]] = None

class PokemonHeldItemVersion(BaseModel):
    """Represents details about a held item in a specific game version."""
    version: NamedAPIResource
    rarity: int

class PokemonHeldItem(BaseModel):
    """Represents an item that can be held by a Pokemon across different versions."""
    item: NamedAPIResource
    version_details: List[PokemonHeldItemVersion]

class PokemonMoveVersion(BaseModel):
    """Represents how a Pokemon learns a move in a specific version group."""
    move_learn_method: NamedAPIResource
    version_group: NamedAPIResource
    level_learned_at: int
    order: Optional[int] = None

class PokemonMove(BaseModel):
    """Represents a move that a Pokemon can learn and how it learns it across versions."""
    move: NamedAPIResource
    version_group_details: List[PokemonMoveVersion]

class PokemonStat(BaseModel):
    """Represents one of a Pokemon's base stats and effort values."""
    stat: NamedAPIResource
    effort: int
    base_stat: int

class PokemonSprites(BaseModel):
    """Represents all available sprite images for a Pokemon."""
    front_default: Optional[str]
    front_shiny: Optional[str]
    front_female: Optional[str]
    front_shiny_female: Optional[str]
    back_default: Optional[str]
    back_shiny: Optional[str]
    back_female: Optional[str]
    back_shiny_female: Optional[str]

class PokemonCries(BaseModel):
    """Represents the sound files for a Pokemon's cry."""
    latest: str
    legacy: str

class VersionGameIndex(BaseModel):
    """Represents a Pokemon's index number within a specific game version."""
    game_index: int
    version: NamedAPIResource

class Pokemon(BaseModel):
    """Represents a Pokemon with all its attributes, stats, moves, and other details."""
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    abilities: List[PokemonAbility]
    forms: List[NamedAPIResource]
    game_indices: List[VersionGameIndex]
    held_items: List[PokemonHeldItem]
    location_area_encounters: str
    moves: List[PokemonMove]
    past_types: List[PokemonTypePast]
    past_abilities: List[PokemonAbilityPast]
    sprites: PokemonSprites
    cries: PokemonCries
    species: NamedAPIResource
    stats: List[PokemonStat]
    types: List[PokemonType]
    model_config = ConfigDict(from_attributes=True)