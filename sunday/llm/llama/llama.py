import sys, os

sys.path.append(os.path.dirname(__file__))

import re

from llama_cpp import Llama as LlamaPro

from sunday.llm.llm import LLM
from sunday.mediator.component import Component
from sunday.mediator.mediator import Mediator

class Llama(LLM, Component):

    def __init__(self):
        super().__init__()
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "llama-8b-InsQ2K.gguf")
        # Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
        self.llm:LlamaPro = LlamaPro(
            model_path=path,  # Download the model file first
            n_ctx=1024,  # The max sequence length to use - note that longer sequence lengths require much more resources
            n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
            n_gpu_layers=10,       # The number of layers to offload to GPU, if you have GPU acceleration available
            verbose=False
        )
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
        pattern = r'\d+'
        numbers = re.findall(pattern, self.llm.create_chat_completion(input)["choices"][0]["message"]["content"])
        if numbers:
            return int(numbers[0])
        else:
            return 1
    
    def write_reflection(self, list_memory: list[str]) -> str:
        statements = " ".join([f'{i}. {memory}' for i, memory in enumerate(list_memory, start=1)])
        input = [
            {"role": self.mediator.bot_role(), "content": f"{' '.join(self.mediator.bot_summary())}"},
            {
                "role" : "user",
                "content" : f"Statements about {self.mediator.bot_name()} {statements} " + 
                "What 5 high-level insights can you infer from the above statments? (Divide each insights with a dot)"
            }
        ]
        return self.llm.create_chat_completion(input)["choices"][0]["message"]["content"] 
    
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
        return self.llm.create_chat_completion(input)["choices"][0]["message"]["content"] 
    
    def write_conversation(self, context: str) -> str:
        input = [
            {"role": self.mediator.bot_role(), "content": f"You are {self.mediator.bot_name()}" },
            {
                "role" : "user",
                "content" : f"It is {self.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} {context} " +
                f"What would be the answer according {self.mediator.bot_name()} personality? {self.mediator.bot_name()}:"
            }
        ]
        return self.llm.create_chat_completion(input)["choices"][0]["message"]["content"] 

    def setMediator(self, mediator: Mediator) -> None:
        self.mediator = mediator