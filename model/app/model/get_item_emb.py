import pickle as p
from tqdm import tqdm
import numpy as np 
from torch_geometric.data import Data
import torch
import numpy as np
from model import RecGCN
def save_all_emb(model):
    model.eval()
    embeddings = []
    for _ in range(100):
        data = generate_data()
        embeddings.append(model.encode_item(data.x, data.edge_index))
    embeddings = torch.cat(embeddings)
    embeddings = embeddings.detach().numpy()
    with open("/app/model/item_embeddings.pickle", "wb") as file:
        p.dump(embeddings, file)

def generate_data():
    x = np.random.rand(1_000,100)
    edge_index = np.random.randint(0,999,(2,10_000)) 
    data = Data(x = torch.Tensor(x), edge_index = torch.tensor(edge_index))
    return data

if __name__=="__main__":
    model = RecGCN()
    model.load_state_dict(torch.load("/app/model/saved_model"))
    save_all_emb(model)
