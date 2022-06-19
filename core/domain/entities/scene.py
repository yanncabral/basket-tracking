from dataclasses import dataclass
from typing import List
from entities import Player, Ball


@dataclass
class Scene:
    """Class for keeping track of elements in a frame."""

    players: List[Player]
    ball: Ball
