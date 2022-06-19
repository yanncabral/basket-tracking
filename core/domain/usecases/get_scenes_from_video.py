
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterable

from core.domain.entities.scene import Scene


class GetScenesFromVideo(ABC):
    
    @abstractmethod
    def getScenesFromVideo(self, video_path: Path) -> Iterable[Scene]:
        pass
