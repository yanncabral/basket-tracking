from dataclasses import dataclass
from typing import Optional, Tuple
from shapely.geometry import Point, Polygon

from core.infra.scene_objects.offset import Offset


@dataclass
class Corners:
    top_left: Offset
    top_right: Offset
    bottom_left: Offset
    bottom_right: Offset

    def to_tuple(
        self,
    ) -> Tuple[
        Tuple[float, float],
        Tuple[float, float],
        Tuple[float, float],
        Tuple[float, float],
    ]:
        return (
            self.top_left.to_tuple(),
            self.top_right.to_tuple(),
            self.bottom_left.to_tuple(),
            self.bottom_right.to_tuple(),
        )

    @staticmethod
    def from_rectangle(
        top_left_x: float,
        top_left_y: float,
        bottom_right_x: float,
        bottom_right_y: float,
    ) -> "Corners":
        return Corners(
            top_left=Offset(x=top_left_x, y=top_left_y),
            top_right=Offset(x=bottom_right_x, y=top_left_y),
            bottom_left=Offset(x=top_left_x, y=bottom_right_y),
            bottom_right=Offset(x=bottom_right_x, y=bottom_right_y),
        )

    def to_polygon(self):
        return Polygon(self.to_tuple())

    def is_point_inside(self, point: Offset) -> bool:
        return Point(point.x, point.y).within(self.to_polygon())

    @property
    def width(self) -> float:
        return self.bottom_right.x - self.top_left.x

    @property
    def height(self) -> float:
        return self.bottom_right.y - self.top_left.y

    def copy_with(
        self,
        top_left: Optional[Offset] = None,
        top_right: Optional[Offset] = None,
        bottom_left: Optional[Offset] = None,
        bottom_right: Optional[Offset] = None,
    ) -> "Corners":
        return Corners(
            bottom_left=bottom_left or self.bottom_left,
            bottom_right=bottom_right or self.bottom_right,
            top_left=top_left or self.top_left,
            top_right=top_right or self.top_right,
        )
