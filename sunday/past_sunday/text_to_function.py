import json
from langchain.llms.ctransformers import CTransformers
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def get_function_from_text(text:str):

    print(text)

    template = """
    {text} 
    """
    with open('sunday/functions.json', 'r') as file:
        functions = json.load(file)

    prompt = PromptTemplate(input_variables=['text'], template=template)

    llm = CTransformers(model="TheBloke/dolphin-2.6-mistral-7B-dpo-laser-GGUF",
                        model_file="dolphin-2.6-mistral-7b-dpo-laser.Q4_K_M.gguf", 
                        config={'context_length':-1}, # Change the value to your choice
                        gpu_layers=20, # Use 0 if you don't want to use GPU
                        temperature=0.0) # Use the minimum value to avoid the model imagine things

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    response = llm_chain.run(text=text)

    return response

if __name__ == '__main__':
    print(get_function_from_text('On the scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed) and \
                                 10 is extremely poignant (e.g., a break up, college acceptance), rate the likely poignancy of the following piece of memory. \
                                 Memory: buying groceries at the The Willows Market and Pharmacy Rating:'))