from abc import ABC

from core.domain.entities.scene import Scene
from core.infra.scene_objects.corners import Corners


class HomographyService(ABC):

    def applyHomography(scene: Scene, from_corners: Corners, to_corners) -> Scene:
        pass