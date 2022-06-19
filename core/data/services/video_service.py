from pathlib import Path
import cv2

from typing import Iterable
from core.domain.entities.scene import Scene
from core.domain.services.video_service import VideoService

from .finder_service import DefaultFinderService

_finder_service = DefaultFinderService()


class DefaultVideoService(VideoService):

    def getScenesFromVideo(self: "DefaultVideoService", video_path: Path) -> Iterable[Scene]:
        cap = cv2.VideoCapture(str(video_path))

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                ball = _finder_service.findBall(frame)
                players = _finder_service.findPlayers(frame)

                if ball is not None and players is not None:
                    # Do not yield if no ball are found
                    yield Scene(players=players, ball=ball)

        cap.release()
            