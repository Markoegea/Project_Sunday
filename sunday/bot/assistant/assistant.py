#TODO Retrieve with observations to decide whether the agent should continue with their existing plan, or react.

import sys, os

sys.path.append(os.path.dirname(__file__))

from sunday.bot.bot import Bot
from sunday.mediator.component import Component
from sunday.mediator.mediator import Mediator

class Assistant(Bot, Component):

    def __init__(self, name="Sunday", personality="Helpful", role="Assistant"):
        super().__init__(name=name, personality=personality, role=role)
        self.mediator = None

    def get_name(self) -> str:
        return self.name
    
    def get_personality(self) -> str:
        return self.personality
    
    def get_role(self) -> str:
        return self.role
    
    def get_summary(self) -> list[str]: 
        #Agent's sumary description (e.g, name, traits, and a summary of their recent experiences).
        #Get it from the bot 
        traits = [f'Innate traits: {self.personality}']

        #Get it from the experiences
        description = f'Who is {self.name}? What {self.name} likes the most? What is {self.name} experiences?'
        retrieved_sumary = self.mediator.experience_retrieval(description=description)
        return traits + retrieved_sumary

    def talk(self, petition:str, your_name:str) -> str:
        relation_memories = self.mediator.experience_retrieval(f"What is {self.name}'s relationship with the {your_name}?")
        petition_memories = self.mediator.experience_retrieval(petition)
        answer = self.mediator.llama_write_conversation(". ".join(relation_memories + petition_memories))
        self.mediator.experience_new_observation(answer)
        return answer
    
    def setMediator(self, mediator: Mediator) -> None:
        self.mediator = mediator