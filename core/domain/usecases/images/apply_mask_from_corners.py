from abc import ABC, abstractmethod

from numpy.typing import ArrayLike

from core.infra.scene_objects.corners import Corners


class ApplyMaskFromCorners(ABC):
    
    @abstractmethod
    def applyMaskFromCorners(self, frame: ArrayLike, region_of_interest: Corners) -> ArrayLike:
        pass
