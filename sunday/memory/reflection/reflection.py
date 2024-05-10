import sys, os
sys.path.append(os.path.dirname(__file__))

from datetime import datetime

from observation.observation import Observations
from sunday.memory.memory import Memory

class Reflection(Observations):

    @staticmethod
    def belong_to(object:Memory) -> bool:
        return isinstance(object, Reflection)
    
    @staticmethod
    def build(**kwargs):
        return Reflection(**kwargs)

    def __init__(self, description:str, importance:int = 1, creation_at=datetime.now(), pointers:list[Memory]=[]) -> None:
        super().__init__(description=description, importance=importance, creation_at=creation_at)
        self.__pointers = pointers

    def __str__(self):
        return super().__str__()
