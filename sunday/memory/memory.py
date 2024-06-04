import sys, os
sys.path.append(os.path.dirname(__file__))

from abc import ABC, abstractmethod

class Memory(ABC):
    """Abstract class that declare the methods necessary for all Memory classes and the min-max importance of a memory"""
    MAX_IMPORTANCE = 10
    MIN_IMPORTANCE = 1
    
    def __init__(self):
        """Basic Constructor for Memory class, instantiate the recency of the memory"""
        self._recency = 1

    @staticmethod
    @abstractmethod
    def belong_to(object) -> bool:
        """Check if the given Memory object, is a instance of this class."""
        pass

    @staticmethod
    @abstractmethod
    def build(**kwargs):
        """Create a instance of this class with the desired arguments"""
        pass

    @abstractmethod
    def calculate_recency(self, decay) -> float:
        """Return the recency of the memory"""
        pass

    @abstractmethod
    def calculate_importance(self) -> float:
        """Return the min-max importance of the memory"""
        pass

    @abstractmethod
    def calculate_relevance(self) -> str:
        """Return the memory description"""
        pass

    @abstractmethod
    def calculate_recent_access(self):
        """Update the recent access of the memory to the present time"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

