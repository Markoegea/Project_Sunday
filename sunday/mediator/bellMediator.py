from mediator import Mediator

from sunday.bot.bot import Bot
from sunday.memory.experience import Experience
from sunday.llm.llm import LLM

class BellMediator(Mediator):

    def __init__(self, bot:Bot, experience:Experience, llm:LLM) -> None:
        self.bot = bot
        self.experience = experience
        self.llm = llm
        self.bot.setMediator(self)
        self.experience.setMediator(self)
        self.llm.setMediator(self)

    def experience_new_observation(self, memory_description:str) -> None:
        self.experience.new_observation(memory_description)

    def experience_retrieval(self, description:str) -> list[str]:
        return self.experience.retrieval(description=description)

    def llama_write_importance(self, description:str) -> int:
        return self.llm.write_importance(description=description)

    def llama_write_conversation(self, conversation:str) -> str:
        return self.llm.write_conversation(context=conversation)
    
    def llama_write_reflection(self, list_memory:list[str]) -> str:
        return self.llm.write_reflection(list_memory=list_memory)

    def llama_write_plan(self, list_memory: list[str]) -> str:
        return self.llm.write_plan(list_memory=list_memory)

    def bot_name(self) -> str:
        return self.bot.get_name()

    def bot_role(self) -> str:
        return self.bot.get_role()

    def bot_summary(self) -> str:
        return self.bot.get_summary()