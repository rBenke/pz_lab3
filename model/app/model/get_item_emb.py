import pickle as p
from tqdm import tqdm
import numpy as np 
from ogb.nodeproppred import PygNodePropPredDataset
from torch_geometric.loader import NeighborLoader
import torch_geometric.transforms as T
import torch
from model import RecGCN
from torch_geometric.utils import index_to_mask
def save_all_emb(model, loader):
    model.eval()
    embeddings = []
    for data in tqdm(loader):
        embeddings.append(model.encode_item(data.x, data.adj_t))
    embeddings = torch.cat(embeddings)
    embeddings = embeddings.detach().numpy()
    with open("/app/item_embeddings.pickle", "wb") as file:
        p.dump(embeddings, file)

def load_data():
    dataset = PygNodePropPredDataset(name = "ogbn-products", root="/app/model/data")
    dataloader = NeighborLoader(
        dataset[0],
        num_neighbors=[-1],
        batch_size=10_000,
        transform = T.ToSparseTensor(),
        input_nodes = index_to_mask(torch.Tensor(range(2_000_000, dataset[0]["num_nodes"])).to(dtype = torch.long), size = dataset[0]["num_nodes"])
    )
   #index_to_mask(dataset.get_idx_split()['train'],size = 3000000 ) 
    return dataloader

if __name__=="__main__":
    model = RecGCN()
    model.load_state_dict(torch.load("/app/model/saved_model"))
    loader = load_data()
    save_all_emb(model, loader)
