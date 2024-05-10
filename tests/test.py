import sys, os
sys.path.append(os.path.abspath('..'))

from datetime import datetime, timedelta

import unittest
from sunday.bot.assistant.assistant import Assistant
from sunday.memory.experience import Experience as Expe
from sunday.memory.observation.observation import Observations as Obs
from sunday.memory.planning.planning import Planning as Pla
from sunday.llm.llama.llama import Llama
from sunday.mediator.bellMediator import BellMediator

class TestMemory(unittest.TestCase):
    
    def test_observations(self):
        decay = 0.005
        observation = Obs("Eliza is an oceanographer.")
        self.assertEqual(observation.calculate_recency(decay), 1.0)
        self.assertEqual(observation.calculate_importance(), 0)
        self.assertEqual(observation.calculate_relevance(),"Eliza is an oceanographer.")

        observation1 = Obs("", importance=3, creation_at=datetime.now()-timedelta(hours=1))
        self.assertEqual(observation1.calculate_recency(decay), 1.0 - decay)
        self.assertEqual(observation1.calculate_importance(), 2/9)

    def test_experiences(self):
        assistant = Assistant(name="Eliza", role="Oceanographer")
        llm = Llama()
        tree_memory = Expe(
        children=[
            Obs("Eliza Torres grew up in a small coastal town in Portugal, known for its beautiful beaches and vibrant fishing community. She is the middle child of three siblings."),
            Obs("Eliza is an oceanographer, passionate about marine conservation, particularly the study of coral reefs and their preservation. She works for an international environmental NGO and has contributed to various significant research papers on marine biodiversity."),
            Obs("She is an avid scuba diver and underwater photographer. Eliza's photographs have been featured in several renowned nature and science magazines, capturing the mysterious beauty of underwater life."),
            Obs("Eliza is known for her calm demeanor and resilience, traits that are vital in her high-stress, high-stakes field of work. She’s also very empathetic, often mentoring young scientists and students who want to enter the field of oceanography."),
            Obs("She has a rescue dog named Maré, a Portuguese Water Dog, which she found during one of her coastal walks. Maré is often by her side, even on some of her less demanding fieldwork trips."),
            Obs("Besides her professional work, Eliza volunteers in local schools to educate children about marine life and the importance of ocean conservation. She believes that change starts with the younger generations."),
            Obs("Her career has taken her to diverse locales, from the icy waters of the Arctic to the warm currents of the Caribbean. Eliza loves to immerse herself in different cultures and learn new languages. She speaks Portuguese, English, Spanish, and a bit of Japanese."),
            Obs("When she was younger, Eliza experienced a near-drowning incident which, rather than deterring her, only strengthened her fascination and respect for the sea."),
            Obs("Her favorite book is 'The Sea Around Us' by Rachel Carson, which significantly influenced her career choice and her perspective on environmental advocacy."),
            Obs("Eliza dreams of starting her own marine research facility someday, focusing on sustainable ocean practices and furthering public awareness on marine ecosystems. She is particularly interested in developing new coral reef restoration techniques.")]
        ) 
        mediator = BellMediator(assistant, tree_memory, llm)
        self.assertEqual(
            tree_memory.retrieval("How does Eliza Torres contribute to educating the next generation about marine conservation?"),
            ['Eliza is an oceanographer, passionate about marine conservation, particularly the study of coral reefs and their preservation. She works for an international environmental NGO and has contributed to various significant research papers on marine biodiversity.',
              'Besides her professional work, Eliza volunteers in local schools to educate children about marine life and the importance of ocean conservation. She believes that change starts with the younger generations.',
                'Eliza Torres grew up in a small coastal town in Portugal, known for its beautiful beaches and vibrant fishing community. She is the middle child of three siblings.']
        )
        tree_memory.append_memory(Obs.build(description="Eliza hates to eat sea food, however she loves to eat meat everyday"))
        self.assertEqual(
            tree_memory.retrieval("What Eliza hates to eat?"),
            ['Eliza hates to eat sea food, however she loves to eat meat everyday', 
              'When she was younger, Eliza experienced a near-drowning incident which, rather than deterring her, only strengthened her fascination and respect for the sea.',
                'Eliza Torres grew up in a small coastal town in Portugal, known for its beautiful beaches and vibrant fishing community. She is the middle child of three siblings.']
        )

    def test_append_memory(self):
        assistant = Assistant(name="Eliza", role="Oceanographer")
        llm = Llama()
        tree_memory = Expe(
        children=[
            Obs("Eliza Torres grew up in a small coastal town in Portugal, known for its beautiful beaches and vibrant fishing community. She is the middle child of three siblings.", importance=7),
            Obs("Eliza is an oceanographer, passionate about marine conservation, particularly the study of coral reefs and their preservation. She works for an international environmental NGO and has contributed to various significant research papers on marine biodiversity.", importance=7),
            Obs("She is an avid scuba diver and underwater photographer. Eliza's photographs have been featured in several renowned nature and science magazines, capturing the mysterious beauty of underwater life."),
            Obs("Eliza is known for her calm demeanor and resilience, traits that are vital in her high-stress, high-stakes field of work. She’s also very empathetic, often mentoring young scientists and students who want to enter the field of oceanography.", importance=7),
            Obs("She has a rescue dog named Maré, a Portuguese Water Dog, which she found during one of her coastal walks. Maré is often by her side, even on some of her less demanding fieldwork trips.", importance=7),
            Obs("Besides her professional work, Eliza volunteers in local schools to educate children about marine life and the importance of ocean conservation. She believes that change starts with the younger generations.", importance=7),
            Obs("Her career has taken her to diverse locales, from the icy waters of the Arctic to the warm currents of the Caribbean. Eliza loves to immerse herself in different cultures and learn new languages. She speaks Portuguese, English, Spanish, and a bit of Japanese.", importance=7),
            Obs("When she was younger, Eliza experienced a near-drowning incident which, rather than deterring her, only strengthened her fascination and respect for the sea.", importance=7),
            Obs("Her favorite book is 'The Sea Around Us' by Rachel Carson, which significantly influenced her career choice and her perspective on environmental advocacy.", importance=7),
            Obs("Eliza dreams of starting her own marine research facility someday, focusing on sustainable ocean practices and furthering public awareness on marine ecosystems. She is particularly interested in developing new coral reef restoration techniques.", importance=7)
        ]) 
        mediator = BellMediator(assistant, tree_memory, llm)
        description = "Eliza are going to study whales for her final project."
        plan = Pla.build(description=description, importance=llm.write_importance(description), location="Atlantic Ocean", starting_time=5000)
        tree_memory.append_memory(plan)
        answer = tree_memory.retrieval("In what place Eliza is studying the whales?")[0]
        self.assertEqual(answer, "Eliza are going to study whales for her final project.")

    def test_reflections(self):
        assistant = Assistant(name="Eliza", role="Oceanographer")
        llm = Llama()
        tree_memory = Expe(
        children=[
            Obs("Eliza Torres grew up in a small coastal town in Portugal, known for its beautiful beaches and vibrant fishing community. She is the middle child of three siblings.", importance=7),
            Obs("Eliza is an oceanographer, passionate about marine conservation, particularly the study of coral reefs and their preservation. She works for an international environmental NGO and has contributed to various significant research papers on marine biodiversity.", importance=7),
            Obs("She is an avid scuba diver and underwater photographer. Eliza's photographs have been featured in several renowned nature and science magazines, capturing the mysterious beauty of underwater life."),
            Obs("Eliza is known for her calm demeanor and resilience, traits that are vital in her high-stress, high-stakes field of work. She’s also very empathetic, often mentoring young scientists and students who want to enter the field of oceanography.", importance=7),
            Obs("She has a rescue dog named Maré, a Portuguese Water Dog, which she found during one of her coastal walks. Maré is often by her side, even on some of her less demanding fieldwork trips.", importance=7),
            Obs("Besides her professional work, Eliza volunteers in local schools to educate children about marine life and the importance of ocean conservation. She believes that change starts with the younger generations.", importance=7),
            Obs("Her career has taken her to diverse locales, from the icy waters of the Arctic to the warm currents of the Caribbean. Eliza loves to immerse herself in different cultures and learn new languages. She speaks Portuguese, English, Spanish, and a bit of Japanese.", importance=7),
            Obs("When she was younger, Eliza experienced a near-drowning incident which, rather than deterring her, only strengthened her fascination and respect for the sea.", importance=7),
            Obs("Her favorite book is 'The Sea Around Us' by Rachel Carson, which significantly influenced her career choice and her perspective on environmental advocacy.", importance=7),
            Obs("Eliza dreams of starting her own marine research facility someday, focusing on sustainable ocean practices and furthering public awareness on marine ecosystems. She is particularly interested in developing new coral reef restoration techniques.", importance=7)
        ]) 
        mediator = BellMediator(assistant, tree_memory, llm)
        self.assertEqual(tree_memory.retrieval("What Eliza love the most?"),
                         ['Eliza loves the sea.', 
                          'When she was younger, Eliza experienced a near-drowning incident which, rather than deterring her, only strengthened her fascination and respect for the sea.',
                            'Eliza Torres grew up in a small coastal town in Portugal, known for its beautiful beaches and vibrant fishing community. She is the middle child of three siblings.'])

    def test_plans(self):
        assistant = Assistant(name="Eliza", role="Oceanographer")
        llm = Llama()
        tree_memory = Expe(
        children=[
            Obs("Eliza Torres grew up in a small coastal town in Portugal, known for its beautiful beaches and vibrant fishing community. She is the middle child of three siblings.", importance=7),
            Obs("Eliza is an oceanographer, passionate about marine conservation, particularly the study of coral reefs and their preservation. She works for an international environmental NGO and has contributed to various significant research papers on marine biodiversity.", importance=7),
            Obs("She is an avid scuba diver and underwater photographer. Eliza's photographs have been featured in several renowned nature and science magazines, capturing the mysterious beauty of underwater life."),
            Obs("Eliza is known for her calm demeanor and resilience, traits that are vital in her high-stress, high-stakes field of work. She’s also very empathetic, often mentoring young scientists and students who want to enter the field of oceanography.", importance=7),
            Obs("She has a rescue dog named Maré, a Portuguese Water Dog, which she found during one of her coastal walks. Maré is often by her side, even on some of her less demanding fieldwork trips.", importance=7),
            Obs("Besides her professional work, Eliza volunteers in local schools to educate children about marine life and the importance of ocean conservation. She believes that change starts with the younger generations.", importance=7),
            Obs("Her career has taken her to diverse locales, from the icy waters of the Arctic to the warm currents of the Caribbean. Eliza loves to immerse herself in different cultures and learn new languages. She speaks Portuguese, English, Spanish, and a bit of Japanese.", importance=7),
            Obs("When she was younger, Eliza experienced a near-drowning incident which, rather than deterring her, only strengthened her fascination and respect for the sea.", importance=7),
            Obs("Her favorite book is 'The Sea Around Us' by Rachel Carson, which significantly influenced her career choice and her perspective on environmental advocacy.", importance=7),
            Obs("Eliza dreams of starting her own marine research facility someday, focusing on sustainable ocean practices and furthering public awareness on marine ecosystems. She is particularly interested in developing new coral reef restoration techniques.", importance=7)
        ]) 
        mediator = BellMediator(assistant, tree_memory, llm)
        description = "Eliza are going to study whales for her final project."
        plan = Pla.build(description=description, importance=llm.write_importance(description), location="Atlantic Ocean", starting_time=5000)
        tree_memory.append_memory(plan)

        tree_memory.new_plan(mediator.bot_summary())

class TestLLM(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()