
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterable, Optional, Tuple
from numpy.typing import ArrayLike

from core.domain.entities.scene import Scene
from core.infra.scene_objects.corners import Corners


class GetScenesFromVideo(ABC):
    
    @abstractmethod
    def getScenesFromVideo(self, video_path: Path, region_of_interest: Optional[Corners]) -> Iterable[Tuple[Scene, ArrayLike]]:
        pass
