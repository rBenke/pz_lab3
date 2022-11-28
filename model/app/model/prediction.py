import torch
import torch_geometric
from model.model import RecGCN

def create_embedding(data):
    model = RecGCN()    
    model.load_state_dict(torch.load("/app/model/saved_model"))
    embeddings = model.encode_user(data.x, data.edge_index)
    return embeddings
