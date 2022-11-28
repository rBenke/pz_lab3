import pickle
import faiss
import numpy as np
class Search_engine:
    def __init__(self):
        with open("/app/item_embeddings.pickle", "rb") as file:
            data = pickle.load(file)
        d = data.shape[1]
        data = data.detach().numpy()
        self.index = faiss.IndexFlatIP(d)
        self.index.add(data)

    def search(self, vector):
        vector = vector[np.newaxis, :]
        _, best_fit = self.index.search(vector, 10)
        return best_fit
