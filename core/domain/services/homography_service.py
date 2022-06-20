from abc import ABC

from core.domain.entities.scene import Scene
from core.infra.scene_objects.corners import Corners


class HomographyService(ABC):

    def applyHomography(self, scene: Scene, from_corners: Corners, to_corners: Corners) -> Scene:
        pass