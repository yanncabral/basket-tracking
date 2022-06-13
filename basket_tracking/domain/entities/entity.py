from dataclasses import dataclass
from typing import Tuple


@dataclass
class Entity:
    """Base class for all entities."""
    position: Tuple[float, float]