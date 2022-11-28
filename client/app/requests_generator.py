import requests as r
import random
import time

SERVER_IP = "172.18.0.3"

def send_request():
    try:
        resp = r.get("http://" + SERVER_IP+"/get_recommendation/1234")
        print("RESPONSE: ", resp.text)
    except Exception as e:
        print(e)

if __name__=="__main__":
    while True:
        send_request()
        time.sleep(1)
