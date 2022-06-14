
from abc import ABC, abstractmethod
from typing import Iterable

from basket_tracking.domain.entities.scene import Frame
from basket_tracking.domain.usecases.get_frames_from_video import GetFramesFromVideo


class VideoService(GetFramesFromVideo, ABC):

    @abstractmethod
    def getFramesFromVideo(self, video_path: str) -> Iterable[Frame]:
        pass
