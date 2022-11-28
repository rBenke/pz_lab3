import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

class RecGCN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.user_enc = GCNConv(100, 8)
        self.item_enc = GCNConv(100, 8)

    def encode_user(self, x, adj):
        x = self.user_enc(x, adj)
        x = F.tanh(x)
        return x

    def encode_item(self, x, adj):
        x = self.item_enc(x, adj)
        x = F.tanh(x)
        return x

    def decode(self, user, item):
        score = torch.sum(user*item, dim=1)
        return score



