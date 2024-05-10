import sys, os
sys.path.append(os.path.dirname(__file__))

from abc import ABC, abstractmethod

class Memory(ABC):

    def __init__(self):
        self._max_importance = 10
        self._min_importance = 1

        self._recency = 1

    @staticmethod
    @abstractmethod
    def belong_to(object):
        pass

    @staticmethod
    @abstractmethod
    def build(**kwargs):
        pass

    @abstractmethod
    def calculate_recency(self, decay) -> float:
        pass

    @abstractmethod
    def calculate_importance(self) -> float:
        pass

    @abstractmethod
    def calculate_relevance(self) -> str:
        pass

    @abstractmethod
    def calculate_recent_access(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

