import sys, os

from sunday.mediator.mediator import Mediator
sys.path.append(os.path.dirname(__file__))

from re import match
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from memory import Memory

from observation.observation import Observations
from reflection.reflection import Reflection
from planning.planning import Planning

from sunday.mediator.component import Component

class Experience(Component):

    def __init__(self, children:list[Memory] = []):
        self.__children:list[Memory] = children

        self.__decay = 0.005

        self.__max_importance = 5
        self.__max_memory_reflection = 100

        self.__alpha = 1
        self.__max_retrieval = 3

        self.__recent_importance = self._get_children_importance().sum()
        self.__tfidf = TfidfVectorizer(stop_words='english')

        self.mediator = None

    def retrieval(self, description:str) -> list[str]:
        self.__description = description
        self.new_reflection()

        if (len(self.__children) == 0):
            return ["No Memories to retrieve."]
        
        result = np.concatenate((self._get_children_recency(self.__decay) * self.__alpha,
                                self._get_children_importance() * self.__alpha,
                                self._get_children_relevance() * self.__alpha), axis=1)
        result_sum = enumerate(result.sum(axis=1))
        result_sorted = sorted(result_sum, key=lambda x: x[1], reverse=True)
        indexes = result_sorted[:self.__max_retrieval]
        
        return self.__access_childs(
            [index for index, value in indexes]
        )

    def _get_children_recency(self, decay):
        return np.array([[child.calculate_recency(decay)] for child in self.__children])

    def _get_children_importance(self):
        return np.array([[child.calculate_importance()] for child in self.__children])

    def _get_children_relevance(self):
        description_list = [child.calculate_relevance() for child in self.__children]
        description_list.append(self.__description)

        tfidf_matrix = self.__tfidf.fit_transform(description_list)
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        
        sim_scores = cosine_sim[cosine_sim.shape[0] - 1][:cosine_sim.shape[1] - 1]

        return np.expand_dims(sim_scores, axis=1)

    def append_memory(self, memory:Memory) -> None:
        self.__recent_importance += memory.calculate_importance()
        self.__children.append(memory)

    def new_observation(self, description:str) -> None:
        observation = Observations.build(
            description=description, 
            importance=self.mediator.llama_write_importance(description)
        )
        self.append_memory(observation)

    def new_reflection(self) -> None:
        if self.__recent_importance >= self.__max_importance:
            self.__recent_importance = 0

            raw_reflection:str = self.mediator.llama_write_reflection(self.__get_memories_description())
            
            reflection = ''
            for s in raw_reflection:
                if match(r'[\(]|[\d]', s):
                    break
                reflection += s
            reflection = reflection.strip()
            
            list_pointers = [int(d) for d in raw_reflection if match(r'[\d]', d)]
            observation_pointer = [self.__children[i].__str__() for i in list_pointers]

            self.append_memory(Reflection.build(
                description=reflection, 
                importance=self.mediator.llama_write_importance(reflection), 
                pointers=observation_pointer
            ))

    def new_plan(self, agent_summary:list[str]):
        #A list of the previous plans
        previous_plan = [plan for plan in self.__children if Planning.belong_to(plan)]
        previous_plan_description = [f'{i}) {plan}' for i, plan in enumerate(self.__get_memories_description(previous_plan), start=1)]

        raw_plan:str = self.mediator.llama_write_plan(agent_summary + previous_plan_description)

        #TODO Format location and starting time
        self.append_memory(Planning.build(
            description=raw_plan, 
            importance=self.mediator.llama_write_importance(raw_plan), 
            location="", 
            starting_time=0
        ))

    def __get_memories_description(self, memories:list[Memory]= None) -> list[str]:
        memories = self.__children if memories == None else memories
        childre_desc = [memory.calculate_relevance() for memory in memories]
        if len(memories) >= self.__max_memory_reflection:
            return childre_desc[-self.__max_memory_reflection:]
        else:
            return childre_desc

    def __access_childs(self, indexes) -> list[str]:
        nodes = []
        for index in indexes:
            self.__children[index].calculate_recent_access()
            nodes.append(self.__children[index].calculate_relevance())
        return nodes

    def setMediator(self, mediator: Mediator) -> None:
        self.mediator = mediator

    def __str__(self):
        return '%s Tree: has %d children and a decay of %d' % (self.__class__.__name__,len(self.__children), self.__decay)