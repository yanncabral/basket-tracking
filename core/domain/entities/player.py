from dataclasses import dataclass

from core.domain.entities.entity import Entity


@dataclass
class Player(Entity):
    """Player entity."""
    name: str