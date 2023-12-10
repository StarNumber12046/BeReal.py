# Not implemented
from . import classes
from .constants import API_URL
import requests

def get_fof_feed(authorization: str):
    res = requests.get(API_URL + "/feeds/friends-of-friends", headers={"Authorization": "Bearer " + authorization})
    resp = res.json()
    if res.status_code == 401:
        raise Exception("Invalid token. Has it expired?")
    return classes.FOFFeed(resp)
    