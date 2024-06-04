import sys, os
sys.path.append(os.path.dirname(__file__))

from abc import abstractmethod
from sunday.mediator.component import Component

class Bot(Component):
    """Abstract class that declare the methods necessary for all Bot classes"""

    def __init__(self, name="Sunday", personality="Helpful", role="Assistant"):
        """Basic Constructor for Bot class, instantiate the name, personality and role variables"""
        self.name = name
        self.personality = personality
        self.role = role

    @abstractmethod
    def get_name(self) -> str:
        """Get Bot name"""
        pass
    
    @abstractmethod
    def get_personality(self) -> str:
        """Get Bot Personality"""
        pass
    
    @abstractmethod
    def get_role(self) -> str:
        """Get Bot Role"""
        pass
    
    @abstractmethod
    def get_summary(self) -> list[str]: 
        """Get Bot's sumary description from their experience"""
        pass

    @abstractmethod
    def talk(self, petition:str, your_name:str) -> str:
        """Based in Bot experience inference the answer for the request and storage it in memory"""
        pass