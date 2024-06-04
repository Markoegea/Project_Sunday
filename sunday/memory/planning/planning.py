import sys, os
sys.path.append(os.path.dirname(__file__))

from datetime import datetime

from observation.observation import Observations
from sunday.memory.memory import Memory

class Planning(Observations):

    @staticmethod
    def belong_to(object:Memory) -> bool:
        return isinstance(object, Planning)
    
    @staticmethod
    def build(**kwargs):
        return Planning(**kwargs)

    def __init__(self, description:str, importance:int = 1, creation_at=datetime.now(), location:str = "", starting_time:datetime = datetime.now(), duration:int = 0) -> None:
        """Constructor for Planning class, instantiate the description, importance, creation timestamp, location and starting timestamp"""
        super().__init__(description=description, importance=importance, creation_at=creation_at)
        self.__location = location
        self.__starting_time = starting_time
        self.__duration = duration

    def __str__(self):
        return f'{self.__starting_time.strftime("%d/%m/%Y %H:%M:%S")} \
        at {self.__location} \
        {super().__str__()} \
        for {self.__duration}'