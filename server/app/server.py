from typing import Union
from fastapi import FastAPI

from server_utils import get_user_embedding, get_SE_recommendation

serv_app = FastAPI()


@serv_app.get("/get_recommendation/{user_id}")
def get_recommendation(user_id):
    print(user_id)
    user_embedding = get_user_embedding(user_id)
    print(user_embedding)
    recommendations = get_SE_recommendation(user_embedding)
    print(recommendations)
    return recommendations


