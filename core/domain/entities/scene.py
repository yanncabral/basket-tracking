from dataclasses import dataclass
from typing import List, Optional

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
    frame: ArrayLike
    
    def draw_players(self, frame: Optional[ArrayLike] = None) -> ArrayLike:
        if frame is None:
            frame = self.frame.copy()
        players_inside_court = (player for player in self.players if self.court.corners.is_point_inside(player.position))
        for player in players_inside_court:
            frame = player.draw(frame)

        return frame

    def draw_ball(self, frame: Optional[ArrayLike] = None) -> ArrayLike:
        if frame is None:
            frame = self.frame.copy()

        return self.ball.draw(frame)

    def draw_frame(self) -> ArrayLike:
        frame = self.draw_players()
        frame = self.draw_ball(frame=frame)
        
        return frame