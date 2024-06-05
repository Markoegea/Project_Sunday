import sys, os
sys.path.append(os.path.dirname(__file__))

import math
from datetime import datetime

from memory import Memory

class Observations(Memory):

    @staticmethod
    def belong_to(object:Memory) -> bool:
        return isinstance(object, Observations)
    
    @staticmethod
    def build(**kwargs):
        return Observations(**kwargs)

    def __init__(self, description:str, importance:int = 1, creation_at=datetime.now()):
        """Constructor for Observations class, instantiate the description, importance and creation timestamp"""
        super().__init__()
        self.__creation_at = creation_at
        self.__recent_access = creation_at
        self.__description = description
        self.__importance = importance

    def calculate_recency(self, decay):
        recency = datetime.now() - self.__recent_access
        penalty = math.floor((recency.total_seconds() / 3600)) * decay
        self._recency -= penalty
        return self._recency

    def calculate_importance(self):
        return (self.__importance - Memory.MIN_IMPORTANCE) / (Memory.MAX_IMPORTANCE - Memory.MIN_IMPORTANCE)

    def calculate_relevance(self):
        return self.__description
    
    def calculate_recent_access(self):
        self.__recent_access = datetime.now()
        return self.__recent_access

    def __str__(self):
        return '%s' % (self.__description)