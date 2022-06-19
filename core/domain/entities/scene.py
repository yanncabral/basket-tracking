from dataclasses import dataclass
from typing import List

from core.domain.entities import Player, Ball

@dataclass
class Scene:
    """Class for keeping track of all required elements in a frame."""

    players: List[Player]
    ball: Ball
