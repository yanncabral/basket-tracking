
from abc import ABC, abstractmethod
from typing import List, Optional
from basket_tracking.domain.entities.ball import Ball
from basket_tracking.domain.entities.player import Player
from numpy.typing import ArrayLike


class FinderService(ABC):

    @abstractmethod
    def findBall(self, frame: ArrayLike) -> Optional[Ball]:
        pass
        
    @abstractmethod
    def findPlayers(self, frame: ArrayLike) -> Optional[List[Player]]:
        pass
    