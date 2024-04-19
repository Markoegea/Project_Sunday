import sys, os
sys.path.append(os.path.abspath('..'))
from datetime import datetime

from experience import *

class Observations(Experience):

    def __init__(self, description:str, creation_at=datetime.now(), children = []):
        super().__init__(children)
        self.creation_at = creation_at
        self.description = description
        self.recent_access = creation_at

        self.max_importance = 10
        self.min_importance = 1

        self.importance = 5
        self.recency = 1

    def calculate_recency(self, decay):
        self.recency -= decay
        return self.recency

    def calculate_importance(self):
        return (self.importance - self.min_importance) / (self.max_importance - self.min_importance)

    def calculate_relevance(self, description):
        return self.description
    
    def __str__(self):
        return '%s, created at %s, description %s, recent access %s, importance %d, recency %d' % (super().__str__(), self.creation_at, self.description, self.recent_access, self.importance, self.recency)
    
if __name__ == '__main__':
    tree_memory = Experience(
       [
           Observations("Eliza Torres grew up in a small coastal town in Portugal, known for its beautiful beaches and vibrant fishing community. She is the middle child of three siblings."),
           Observations("Eliza is an oceanographer, passionate about marine conservation, particularly the study of coral reefs and their preservation. She works for an international environmental NGO and has contributed to various significant research papers on marine biodiversity."),
           Observations("She is an avid scuba diver and underwater photographer. Eliza's photographs have been featured in several renowned nature and science magazines, capturing the mysterious beauty of underwater life."),
           Observations("Eliza is known for her calm demeanor and resilience, traits that are vital in her high-stress, high-stakes field of work. She’s also very empathetic, often mentoring young scientists and students who want to enter the field of oceanography."),
           Observations("She has a rescue dog named Maré, a Portuguese Water Dog, which she found during one of her coastal walks. Maré is often by her side, even on some of her less demanding fieldwork trips."),
           Observations("Besides her professional work, Eliza volunteers in local schools to educate children about marine life and the importance of ocean conservation. She believes that change starts with the younger generations."),
           Observations("Her career has taken her to diverse locales, from the icy waters of the Arctic to the warm currents of the Caribbean. Eliza loves to immerse herself in different cultures and learn new languages. She speaks Portuguese, English, Spanish, and a bit of Japanese."),
           Observations("When she was younger, Eliza experienced a near-drowning incident which, rather than deterring her, only strengthened her fascination and respect for the sea."),
           Observations("Her favorite book is 'The Sea Around Us' by Rachel Carson, which significantly influenced her career choice and her perspective on environmental advocacy."),
           Observations("Eliza dreams of starting her own marine research facility someday, focusing on sustainable ocean practices and furthering public awareness on marine ecosystems. She is particularly interested in developing new coral reef restoration techniques.")
        ]) 
    #print(tree_memory.update())
    print(tree_memory.retrieval("How does Eliza Torres contribute to educating the next generation about marine conservation?"))