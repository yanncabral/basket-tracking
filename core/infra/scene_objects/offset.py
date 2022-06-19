from dataclasses import dataclass
from typing import Tuple


@dataclass
class Offset:
    x: float
    y: float

    def to_tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)