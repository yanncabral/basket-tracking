from dataclasses import dataclass

from core.domain.entities.entity import Entity
from core.infra.scene_objects.body import Body


@dataclass
class Court(Body):
    """Base class for all entities."""


