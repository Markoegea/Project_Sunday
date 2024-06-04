import sys, os
sys.path.append(os.path.dirname(__file__))

from abc import ABC, abstractmethod

class Mediator(ABC):

    @abstractmethod
    def experience_new_observation(self, memory:str) -> None:
        """Add a new observation given the description"""
        pass

    @abstractmethod
    def experience_retrieval(self, description:str) -> list[str]:
        """Retrieval the related list of memories given the description"""
        pass

    @abstractmethod
    def llama_write_importance(self, description:str) -> int:
        """Inference the number of importance of a statement from 1 (very insignificant) to 10 (very important)"""
        pass

    @abstractmethod
    def llama_write_conversation(self, conversation:str) -> str:
        """Inference the answer to a conversation given the context of the conversation"""
        pass
    
    @abstractmethod
    def llama_write_reflection(self, list_memory:list[str]) -> str:
        """Inference a reflection based on a list of past memories"""
        pass

    @abstractmethod
    def llama_write_plan(self, list_memory: list[str]) -> str:
        """Inference a reflection based on a list of past memories"""
        pass

    @abstractmethod
    def bot_name(self) -> str:
        """Get Bot name"""
        pass

    @abstractmethod
    def bot_role(self) -> str:
        """Get Bot Role"""
        pass

    @abstractmethod
    def bot_summary(self) -> str:
        """Get Bot's sumary description from their experience"""
        pass