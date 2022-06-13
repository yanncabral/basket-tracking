from dataclasses import dataclass
from basket_tracking.domain.entities.entity import Entity


@dataclass
class Player(Entity):
    """Player entity."""
    name: str