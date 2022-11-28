from model import RecGCN
import torch 

def train(model):
    pass

if __name__=="__main__":
    model = RecGCN()
    train(model)
    torch.save(model.state_dict(), "/app/model/saved_model")
