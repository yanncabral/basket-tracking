from abc import ABC, abstractmethod

from numpy.typing import ArrayLike

from core.infra.scene_objects.offset import Offset


class DrawCircleInFrame(ABC):
    
    @abstractmethod
    def drawCircleInFrame(self, frame: ArrayLike, center: Offset) -> ArrayLike:
        pass
