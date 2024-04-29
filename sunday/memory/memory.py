from abc import ABC, abstractmethod

class Memory(ABC):

    @abstractmethod
    def calculate_recency(self, decay):
        pass

    @abstractmethod
    def calculate_importance(self):
        pass

    @abstractmethod
    def calculate_relevance(self):
        pass

    def calculate_recent_access(self):
        raise NotImplementedError()

    @abstractmethod
    def __str__(self):
        pass

