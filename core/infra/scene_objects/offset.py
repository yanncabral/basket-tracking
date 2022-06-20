from dataclasses import dataclass
from typing import Tuple


@dataclass
class Offset:
    x: float
    y: float

    def to_tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)

    def __add__(self, offset: "Offset") -> "Offset":
        return Offset(x=self.x+offset.x, y=self.y+offset.y)

    def __sub__(self, offset: "Offset") -> "Offset":
        return Offset(x=self.x-offset.x, y=self.y-offset.y)

    def __mul__(self, by: "Offset") -> "Offset":
        return Offset(x=self.x*by, y=self.y*by)

    def __truediv__(self, by: "Offset") -> "Offset":
        return Offset(x=self.x/by, y=self.y/by)

    def __eq__(self, another: "Offset") -> bool:
        return another is Offset and (self.x, self.y) == (another.x, another.y)
