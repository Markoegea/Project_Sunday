import sys, os

sys.path.append(os.path.dirname(__file__))

from sunday.llm.llm import LLM
from sunday.mediator.component import Component
from sunday.mediator.mediator import Mediator

#TODO: Implement model
#TODO: Test the input
#model name 1 meta-llama/Meta-Llama-3-8B-Instruct
class Llama(LLM, Component):

    def __init__(self):
        super().__init__()
        self.mediator = None

    def write_importance(self, description: str) -> int:
        input = [
            {"role": self.mediator.bot_role(), "content": f"{'. '.join(self.mediator.bot_summary())}."},
            {
                "role": "user",
                "content": f"On the scale of 1 to 10, where 1 is purely mundane \
                (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance), \
                rate the likely poignancy of the following piece of memory. Memory: {description} \
                Rating:"
            }
        ]
        return 8
    
    def write_reflection(self, list_memory: list[str]) -> str:
        statements = "\n".join([f'{i}. {memory}' for i, memory in enumerate(list_memory, start=1)])
        input = [
            {"role": self.mediator.bot_role(), "content": "You are a detective" },
            {
                "role" : "user",
                "content" : f"Statements about {self.mediator.bot_name()} \n {statements} \n \
                What 5 high-level insights can you infer from the above statments?"
            }
        ]
        return "Eliza loves the sea. (because 1, 2, 7)"
    
    def write_plan(self, list_memory: list[str]) -> str:
        statements = ". ".join(list_memory)
        input = [
            {"role": self.mediator.bot_role(), "content": f"You are {self.mediator.bot_name()}" },
            {
                "role" : "user",
                "content" : f"Name: {self.mediator.bot_name()} \n {statements} \n \
                    Today is {self.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}. Here is {self.mediator.bot_name()}'s plan today in broad strokes: 1)"
            }
        ]
        return input
    
    def write_conversation(self, context: str) -> str:
        input = [
            {"role": self.mediator.bot_role(), "content": f"You are {self.mediator.bot_name()}" },
            {
                "role" : "user",
                "content" : f"It is {self.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} \
                {context} \n Should {self.mediator.bot_name()} react to the interaction, and if so, what would be an appropriate answer?"
            }
        ]
        return input 
    
    def setMediator(self, mediator: Mediator) -> None:
        self.mediator = mediator