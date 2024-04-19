from abc import ABC, abstractmethod

class Memory(ABC):

    @abstractmethod
    def retrieval(self, description):
        pass

    @abstractmethod
    def calculate_recency(self, decay):
        pass

    @abstractmethod
    def calculate_importance(self):
        pass

    @abstractmethod
    def calculate_relevance(self, description):
        pass

    @abstractmethod
    def __str__(self):
        pass

