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
            {"role": self.mediator.bot_role(), "content": f"{' '.join(self.mediator.bot_summary())}"},
            {
                "role": "user",
                "content": "On the scale of 1 to 10, where 1 is purely mundane " + 
                "(e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance), " +
                f"rate the likely poignancy of the following piece of memory. " + 
                f"Memory: {description} Rating:"
            }
        ]
        print("Write importance:", input)
        return 8
    
    def write_reflection(self, list_memory: list[str]) -> str:
        statements = " ".join([f'{i}. {memory}' for i, memory in enumerate(list_memory, start=1)])
        input = [
            {"role": self.mediator.bot_role(), "content": f"{' '.join(self.mediator.bot_summary())}"},
            {
                "role" : "user",
                "content" : f"Statements about {self.mediator.bot_name()} {statements} " + 
                "What 5 high-level insights can you infer from the above statments? (example format: insight (because of 1, 5, 3))"
            }
        ]
        print("Write reflection:", input)
        return "Eliza loves the sea. (because 1, 2, 7)"
    
    def write_plan(self, list_memory: list[str]) -> str:
        statements = " ".join(list_memory)
        input = [
            {"role": self.mediator.bot_role(), "content": f"You are {self.mediator.bot_name()}" },
            {
                "role" : "user",
                "content" : f"Name: {self.mediator.bot_name()} {statements} " +
                f"Today is {self.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}. " +
                f"Here is {self.mediator.bot_name()} plan today in broad strokes: 1)"
            }
        ]
        print("Write plan:", input)
        return input
    
    def write_conversation(self, context: str) -> str:
        input = [
            {"role": self.mediator.bot_role(), "content": f"You are {self.mediator.bot_name()}" },
            {
                "role" : "user",
                "content" : f"It is {self.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} {context} " +
                f"Should {self.mediator.bot_name()} react to the interaction, and if so, what would be an appropriate answer?"
            }
        ]
        print("Write conversation:", input)
        return input 
    
    def setMediator(self, mediator: Mediator) -> None:
        self.mediator = mediator