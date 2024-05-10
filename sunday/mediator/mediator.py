import sys, os
sys.path.append(os.path.dirname(__file__))

from abc import ABC, abstractmethod

class Mediator(ABC):

    @abstractmethod
    def experience_new_observation(self, memory:str) -> None:
        pass

    @abstractmethod
    def experience_retrieval(self, description:str) -> list[str]:
        pass

    @abstractmethod
    def llama_write_importance(self, description:str) -> int:
        pass

    @abstractmethod
    def llama_write_conversation(self, conversation:str) -> str:
        pass
    
    @abstractmethod
    def llama_write_reflection(self, list_memory:list[str]) -> str:
        pass

    @abstractmethod
    def llama_write_plan(self, list_memory: list[str]) -> str:
        pass

    @abstractmethod
    def bot_name(self) -> str:
        pass

    @abstractmethod
    def bot_role(self) -> str:
        pass

    @abstractmethod
    def bot_summary(self) -> str:
        pass