import requests as r
from config import model_ip, search_engine_ip

def get_user_embedding(user_id):
    message = r.get("http://" + str(model_ip) + f"/get_embedding/{user_id}")
    if message.status_code==200:
        print("text: ", message.text)
        return message.text
    else:
        print(message)
        return None

def get_SE_recommendation(embedding):
    print("GET RECOMMENDATION")
    print("http://" + str(search_engine_ip) + f"/get_recommendations/{str(embedding)}")
    message = r.get("http://" + str(search_engine_ip) + f"/get_recommendations/{str(embedding)}")
    print(message)
    if message.status_code==200:
        print(message.text)
        return message.text
    else:
        print(message)
        return None

    return []
