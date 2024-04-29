import sys, os
sys.path.append(os.path.dirname(__file__))
import math
from datetime import datetime

from memory import Memory

class Observations(Memory):

    #TODO: The importance must be created by a llm
    def __init__(self, description:str, importance:int = 1, creation_at=datetime.now()):
        self.__creation_at = creation_at
        self.__recent_access = creation_at

        self.__description = description

        self.__max_importance = 10
        self.__min_importance = 1

        self.__importance = importance
        self.__recency = 1

    def calculate_recency(self, decay):
        recency = datetime.now() - self.__recent_access
        penalty = math.floor((recency.total_seconds() / 3600)) * decay
        self.__recency -= penalty
        return self.__recency

    def calculate_importance(self):
        return (self.__importance - self.__min_importance) / (self.__max_importance - self.__min_importance)

    def calculate_relevance(self):
        return self.__description
    
    def calculate_recent_access(self):
        self.__recent_access = datetime.now()
        return self.__recent_access

    def __str__(self):
        return '%s, created at %s, description %s, recent access %s, importance %d, recency %d' % (super().__str__(), self.__creation_at, self.__description, self.__recent_access, self.__importance, self.__recency)