
from abc import ABC, abstractmethod
from typing import Iterable

from core.domain.entities.scene import Scene
from core.domain.usecases.get_scenes_from_video import GetScenesFromVideo


class VideoService(GetScenesFromVideo, ABC):

    @abstractmethod
    def getScenesFromVideo(self, video_path: str) -> Iterable[Scene]:
        pass
