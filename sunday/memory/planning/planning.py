import sys, os
sys.path.append(os.path.dirname(__file__))

from datetime import datetime

from observation.observation import Observations

class Planning(Observations):

    def __init__(self, description:str, importance:int = 1, creation_at=datetime.now(), location:str = "", starting_time:datetime = datetime.now(), duration:int = 0) -> None:
        super().__init__(description=description, importance=importance, creation_at=creation_at)
        self.location = location
        self.starting_time = starting_time
        self.duration = duration