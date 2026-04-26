import requests
from config import WEBHOOK

def send(msg):
    data = {"msgtype": "text", "text": {"content": msg}}
    requests.post(WEBHOOK, json=data)

