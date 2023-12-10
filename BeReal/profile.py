# This contains functions that should only be used inside the BeReal class. Please instantiate a BeReal class and use its implementation of these functions

from .constants import GOOGLE_API_KEY, HEADERS, API_URL
import requests
from . import classes

def get_profile(auth_token:str) -> classes.Me:
    res = requests.get(API_URL + "/person/me", headers={"Authorization": "Bearer " + auth_token})
    if res.status_code == 401:
        raise Exception("Invalid token. Has it expired?")
    friends_res = requests.get(API_URL + "/relationships/friends", headers={"Authorization": "Bearer " + auth_token})
    if res.status_code == 401:
        raise Exception("Invalid token. Has it expired?")
    return classes.Me(res.json(), friends_res.json()['data'])
