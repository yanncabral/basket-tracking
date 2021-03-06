from dataclasses import dataclass
from typing import Iterable, List, Literal, Union

from numpy.typing import ArrayLike
from core.domain.entities.court import Court

from core.domain.entities.player import Player
from core.domain.entities.ball import Ball

@dataclass
class Scene:
    """Class for keeping track of all required elements in a frame."""

    players: List[Player]
    ball: Ball
    court: Court
    
    def draw_players(self, frame: ArrayLike, type: Union[Literal['circle'], Literal['rectangle']] = 'circle') -> ArrayLike:
        for player in self.players_inside_court:
            frame = player.draw(frame=frame, type=type)

        return frame

    def draw_ball(self, frame: ArrayLike) -> ArrayLike:
        return self.ball.draw(frame)

    def draw_frame(self, frame: ArrayLike) -> ArrayLike:
        frame = self.draw_players(frame=frame)
        frame = self.draw_ball(frame=frame)
        
        return frame

    @property
    def players_inside_court(self) -> Iterable[Player]:
        return (player for player in self.players if self.court.corners.is_point_inside(player.position))