
from abc import ABC, abstractmethod
import pathlib
from typing import Iterable, Optional

from core.domain.entities.scene import Scene
from core.domain.usecases.get_scenes_from_video import GetScenesFromVideo
from core.infra.scene_objects.corners import Corners


class VideoService(GetScenesFromVideo, ABC):
    pass
