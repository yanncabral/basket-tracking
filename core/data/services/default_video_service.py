from pathlib import Path
import cv2

from typing import Iterable, Optional, Tuple

from numpy.typing import ArrayLike
from core.domain.entities.scene import Scene
from core.domain.services.video_service import VideoService
from core.infra.scene_objects.corners import Corners

from .default_finder_service import DefaultFinderService
from .default_image_service import DefaultImageService

_finder_service = DefaultFinderService()
_image_service = DefaultImageService()


class DefaultVideoService(VideoService):

    def getScenesFromVideo(self, video_path: Path, region_of_interest: Optional[Corners]) -> Iterable[Tuple[Scene, ArrayLike]]:
        cap = cv2.VideoCapture(str(video_path))

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                if region_of_interest is not None:
                    frame = _image_service.applyMaskFromCorners(frame, region_of_interest)
                ball = _finder_service.findBall(frame)
                players = _finder_service.findPlayers(frame)
                court = _finder_service.findCourt(frame)

                if ball is not None and players is not None:
                    # Do not yield if no ball are found
                    yield Scene(players=players, ball=ball, court=court), frame

        cap.release()