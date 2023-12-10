# This contains functions that should only be used inside the BeReal class. Please instantiate a BeReal class and use its implementation of these functions

import requests
import json
from . import classes

def get_feed(authorization: str):
    res = requests.get("https://mobile.bereal.com/api/feeds/friends-v1", headers={"Authorization": "Bearer " + authorization})
    return classes.Feed(res.json())