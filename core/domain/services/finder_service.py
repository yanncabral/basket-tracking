
from abc import ABC, abstractmethod
from typing import List, Optional
from numpy.typing import ArrayLike

from core.domain.entities.ball import Ball
from core.domain.entities.court import Court
from core.domain.entities.player import Player


class FinderService(ABC):

    @abstractmethod
    def findBall(self, frame: ArrayLike) -> Optional[Ball]:
        pass
        
    @abstractmethod
    def findPlayers(self, frame: ArrayLike) -> Optional[List[Player]]:
        pass
    
    @abstractmethod
    def findCourt(self, frame: ArrayLike) -> Optional[Court]:
        pass