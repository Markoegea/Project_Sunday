import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from memory import Memory


class Experience(Memory):

    def __init__(self, children = []):
        self.children = children
        self.decay = 0.005
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.alpha = 1
        self.max_retrieval = 3

    def retrieval(self, description):
        result = np.concatenate((self.calculate_recency(self.decay) * self.alpha,
                                self.calculate_importance()* self.alpha,
                                self.calculate_relevance(description)* self.alpha), axis=1)
        result_sum = enumerate(result.sum(axis=1))
        result_sorted = sorted(result_sum, key=lambda x: x[1], reverse=True)
        indexes = result_sorted[:self.max_retrieval]
        return self.get_childs(
            [index for index, value in indexes]
        )

    def calculate_recency(self, decay):
        recency_list = enumerate(reversed(self.children))
        return np.array(
            [
                [child.calculate_recency(decay * i)] for i, child in 
                sorted(recency_list, key= lambda x : x[0], reverse=True)
            ]
        )

    def calculate_importance(self):
        return np.array([[child.calculate_importance()] for child in self.children])

    def calculate_relevance(self, description):
        description_list = [child.calculate_relevance(description) for child in self.children]
        description_list.append(description)

        tfidf_matrix = self.tfidf.fit_transform(description_list)
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        
        sim_scores = cosine_sim[cosine_sim.shape[0] - 1][:cosine_sim.shape[1] - 1]

        return np.expand_dims(sim_scores, axis=1)

    def get_childs(self, indexes):
        nodes = []
        for index in indexes:
            nodes.append(self.children[index].calculate_relevance(''))
        return nodes

    def __str__(self):
        return '%s Tree: has %d children and a decay of %d' % (self.__class__.__name__,len(self.children), self.decay)