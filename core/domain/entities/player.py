from dataclasses import dataclass

from numpy.typing import ArrayLike

from core.domain.entities.entity import Entity
from core.infra.scene_objects.body import Body
from core.infra.scene_objects.corners import Corners
from core.infra.scene_objects.offset import Offset
from core.data.services.default_image_service import DefaultImageService as ImageService

_image_service = ImageService()


@dataclass
class Player(Entity, Body):
    """Player entity."""
    name: str

    @staticmethod
    def from_corners(corners: Corners, name: str) -> 'Player':
        """Create player from corners."""

        return Player(corners=corners, name=name, position=Player._get_foot_position_from_body(corners))

    @staticmethod
    def _get_foot_position_from_body(corners: Corners) -> Offset:
        """Get foot position from body corners."""
        x_left = corners.top_left.x
        x_right = corners.bottom_right.x
        y = corners.bottom_right.y

        x_center = x_left + (x_right - x_left) / 2
        
        return Offset(x=x_center, y=y)

    def draw(self, frame: ArrayLike, type: Union[Literal['circle'], Literal['rectangle']] = 'circle') -> ArrayLike:
        color = (255, 0, 0)
        if type == 'circle':
            return _image_service.drawCircleInFrame(frame=frame, center=self.position, color=color)
        else:
            return _image_service.drawRectangleInFrame(frame=frame, corners=self.corners, color=color)