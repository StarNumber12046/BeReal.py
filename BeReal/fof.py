# Not implemented
from . import classes
from .constants import API_URL
import json
import requests

def get_fof_feed(authorization: str):
    
    res = requests.get(API_URL + "/feeds/friends-of-friends", headers={"Authorization": "Bearer " + authorization})
    resp = res.json()
    data = resp
    if res.status_code == 401:
        raise Exception("Invalid token. Has it expired?")
    
    next = resp.get("next")
    while next:
        res = requests.get(API_URL + "/feeds/friends-of-friends", headers={"Authorization": "Bearer " + authorization}, params={"page": next})
        resp = res.json()
        if res.status_code == 401:
            raise Exception("Invalid token. Has it expired?")
        next = resp.get("next")
        data['data'].append(resp['data'])
    fixed_data = {"data": []}
    for item in data['data']:
        if isinstance(item, dict):
            fixed_data['data'].append(item)
        elif isinstance(item, list):
            for subitem in item:
                fixed_data['data'].append(subitem)
    return classes.FOFFeed(fixed_data)
    