import sys, os
sys.path.append(os.path.dirname(__file__))

from abc import abstractmethod
from sunday.mediator.component import Component

class Bot(Component):

    def __init__(self, name="Sunday", personality="Helpful", role="Assistant"):
        self.name = name
        self.personality = personality
        self.role = role

    @abstractmethod
    def get_name(self) -> str:
        pass
    
    @abstractmethod
    def get_personality(self) -> str:
        pass
    
    @abstractmethod
    def get_role(self) -> str:
        pass
    
    @abstractmethod
    def get_summary(self) -> list[str]: 
        pass

    @abstractmethod
    def talk(self, petition:str, your_name:str) -> str:
        pass