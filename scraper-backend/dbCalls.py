import requests

def put_tag(tag: str, timestamp: float):
    address = 'http://localhost:3000/tags'
    data = {}
    data['tag']=tag
    data['timestamp']=timestamp
    requests.post(address, data = data)