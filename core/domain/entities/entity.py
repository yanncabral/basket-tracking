from dataclasses import dataclass
from typing import Tuple

from core.infra.scene_objects.offset import Offset


@dataclass
class Entity:
    """Base class for all entities."""
    position: Offset