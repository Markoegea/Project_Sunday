import sys, os
sys.path.append(os.path.dirname(__file__))

from abc import ABC, abstractmethod

from sunday.mediator.mediator import Mediator

class Component(ABC):
    """Abstract class that declare the methods necessary for all components to comunicate between each others"""

    @abstractmethod
    def setMediator(self, mediator:Mediator) -> None:
        """Set the mediator"""
        pass