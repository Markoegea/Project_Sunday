import sys, os

sys.path.append(os.path.dirname(__file__))

from datetime import datetime
from abc import abstractmethod
from sunday.mediator.component import Component

class LLM(Component):

    def __init__(self):
        self.datetime = datetime

    @abstractmethod
    def write_importance(self, description:str) -> int:
        pass

    @abstractmethod
    def write_reflection(self, list_memory:list[str]) -> str:
        pass

    @abstractmethod
    def write_plan(self, list_memory:list[str]) -> str:
        pass

    @abstractmethod
    def write_conversation(self, context:str) -> str:
        pass
