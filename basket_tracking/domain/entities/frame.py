from dataclasses import dataclass
from typing import List
from basket_tracking.domain.entities.ball import Ball

from basket_tracking.domain.entities.player import Player


@dataclass
class Frame:
    """Class for keeping track of elements in a frame."""

    players: List[Player]
    ball: Ball
