
from abc import ABC, abstractmethod
from typing import Iterable

from basket_tracking.domain.entities.frame import Frame


class GetFramesFromVideo(ABC):
    
    @abstractmethod
    def getFramesFromVideo(self, video_path: str) -> Iterable[Frame]:
        pass
