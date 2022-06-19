
from abc import ABC
from core.domain.usecases.videos.get_scenes_from_video import GetScenesFromVideo


class VideoService(GetScenesFromVideo, ABC):
    pass
