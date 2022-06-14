
from abc import ABC, abstractmethod
from typing import Iterable

from basket_tracking.domain.entities.scene import Frame, Scene


class GetFramesFromVideo(ABC):
    
    @abstractmethod
    def getScenesFromVideo(self, video_path: str) -> Iterable[Scene]:
        pass
