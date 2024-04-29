import sys, os
sys.path.append(os.path.dirname(__file__))

from datetime import datetime

from observation.observation import Observations

class Reflection(Observations):

    def __init__(self, description:str, importance:int = 1, creation_at=datetime.now(), pointers:Observations=[]) -> None:
        super().__init__(description=description, importance=importance, creation_at=creation_at)
        self.pointers = pointers

