
from abc import ABC, abstractmethod
from typing import Iterable

from core.domain.entities.scene import Scene


class GetFramesFromVideo(ABC):
    
    @abstractmethod
    def getScenesFromVideo(self, video_path: str) -> Iterable[Scene]:
        pass
