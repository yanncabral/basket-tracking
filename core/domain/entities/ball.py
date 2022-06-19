from dataclasses import dataclass

from numpy.typing import ArrayLike
from core.domain.entities.entity import Entity
from core.data.services.default_image_service import DefaultImageService as ImageService

_image_service = ImageService()

@dataclass
class Ball(Entity):
    """Ball entity."""
    def draw(self, frame: ArrayLike) -> ArrayLike:
        return _image_service.drawCircleInFrame(frame=frame, center=self.position)