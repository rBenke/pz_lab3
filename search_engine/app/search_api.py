from typing import Union

from fastapi import FastAPI
from search_engine import Search_engine
import numpy as np

search_e = Search_engine()
search_app = FastAPI()


@search_app.get("/get_recommendations/{client_emb}")
def get_recommendations(client_emb):
    print(client_emb)
    client_emb = np.array(eval(client_emb))
    best_fits = search_e.search(client_emb)
    #print(type(best_fits[0].tolist()))
    return best_fits[0].tolist()

