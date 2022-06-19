from abc import ABC, abstractmethod
from dataclasses import dataclass

from numpy.typing import ArrayLike

from core.infra.scene_objects.offset import Offset


@dataclass
class Entity(ABC):
    """Base class for all entities."""
    position: Offset

    @abstractmethod
    def draw(self, frame: ArrayLike) -> ArrayLike:
        pass