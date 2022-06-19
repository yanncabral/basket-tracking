from abc import ABC, abstractmethod

from numpy.typing import ArrayLike

from core.infra.scene_objects.corners import Corners


class DrawRectangleInFrame(ABC):
    
    @abstractmethod
    def drawRectangleInFrame(self, frame: ArrayLike, corners: Corners) -> ArrayLike:
        pass
