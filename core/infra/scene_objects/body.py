from dataclasses import dataclass
from typing import Tuple
from shapely.geometry import Polygon
from core.infra.scene_objects.corners import Corners

from core.infra.scene_objects.offset import Offset


@dataclass
class Body:
    """Base class for all fullbody entities."""
    corners: Corners

    @staticmethod
    def from_corners(top_left_x: float, top_left_y: float, top_right_x: float, top_right_y: float, bottom_left_x: float, bottom_left_y: float, bottom_right_x: float, bottom_right_y: float) -> 'Body':
        return Body(
            corners=Corners(
                top_left=Offset(x=top_left_x,y=top_left_y),
                top_rigth=Offset(x=top_right_x,y=top_right_y),
                bottom_left=Offset(x=bottom_left_x,y=bottom_left_y),
                bottom_right=Offset(x=bottom_right_x,y=bottom_right_y)
            )
        )