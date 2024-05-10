import sys, os
sys.path.append(os.path.dirname(__file__))

from abc import ABC, abstractmethod

from sunday.mediator.mediator import Mediator

class Component(ABC):

    @abstractmethod
    def setMediator(self, mediator:Mediator) -> None:
        pass