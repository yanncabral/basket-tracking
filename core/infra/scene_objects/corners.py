from dataclasses import dataclass
from typing import Tuple

from core.infra.scene_objects.offset import Offset


@dataclass
class Corners:
    top_left: Offset
    top_right: Offset
    bottom_left: Offset
    bottom_right: Offset

    def to_tuple(self) -> Tuple[Tuple[float, float], Tuple[float, float], Tuple[float, float], Tuple[float, float]]:
        return (self.top_left.to_tuple(), self.top_right.to_tuple(), self.bottom_left.to_tuple(), self.bottom_right.to_tuple())

    @staticmethod
    def from_rectangle(top_left_x: float, top_left_y: float, bottom_right_x: float, bottom_right_y: float) -> 'Corners':
        return Corners(
            top_left=Offset(x=top_left_x, y=top_left_y),
            top_right=Offset(x=bottom_right_x, y=top_left_y),
            bottom_left=Offset(x=top_left_x, y=bottom_right_y),
            bottom_right=Offset(x=bottom_right_x, y=bottom_right_y)
        )