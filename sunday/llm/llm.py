import sys, os

sys.path.append(os.path.dirname(__file__))

from datetime import datetime
from abc import abstractmethod
from sunday.mediator.component import Component

class LLM(Component):
    """Abstract class that declare the methods necessary for all LLM classes"""


    def __init__(self):
        """Basic Constructor for LLM class, instantiate the current datetime"""
        self.datetime = datetime

    @abstractmethod
    def write_importance(self, description:str) -> int:
        """Inference the number of importance of a statement from 1 (very insignificant) to 10 (very important)"""
        pass

    @abstractmethod
    def write_reflection(self, list_memory:list[str]) -> str:
        """Inference a reflection based on a list of past memories"""
        pass

    @abstractmethod
    def write_plan(self, list_memory:list[str]) -> str:
        """Inference the plan for the day based on a list of past memories"""
        pass

    @abstractmethod
    def write_conversation(self, context:str) -> str:
        """Inference the answer to a conversation given the context of the conversation"""
        pass
