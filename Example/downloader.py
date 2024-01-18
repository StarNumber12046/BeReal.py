import BeReal
import json
import requests
import os
from pathlib import Path
from datetime import datetime

folder = "BeReal_dl"

client = BeReal.BeReal("")

f = open("creds.json", "r")
client.resume_session(json.loads(f.read()))
f.close()

me = client.me()

print("Username: %s" % me.username)

os.chdir(folder)

feed = client.get_feed()
for post in feed.friends_posts + feed.user_posts:
    for index, p in enumerate(post.posts):
        datestring = p.taken_at.strftime("%Y%m%d")  # Date to the desired string format
        Path(datestring).mkdir(parents=True, exist_ok=True)   # Create folder
        os.chdir(datestring)
        primary_name = f"{post.user.username}_{index}_primary.webp"
        secondary_name = f"{post.user.username}_{index}_secondary.webp"
        if not os.path.exists(primary_name):
            print(f"Downloading primary image for post {index} of {post.user.username}")
            fp = open(f"{post.user.username}_{index}_primary.webp", "wb")
            resp = requests.get(p.primary_image.url)
            fp.write(resp.content)
        if not os.path.exists(secondary_name):
            print(f"Downloading secondary image for post {index} of {post.user.username}")
            fp = open(f"{post.user.username}_{index}_secondary.webp", "wb")
            resp = requests.get(p.secondary_image.url)
            fp.write(resp.content)
        os.chdir("..")


fof = client.get_fof()
for post in fof.posts:
    datestring = post.taken_at.strftime("%Y%m%d")  # Date to the desired string format
    Path(datestring).mkdir(parents=True, exist_ok=True)   # Create folder
    os.chdir(datestring)
    primary_name = f"{post.user.username}_{index}_primary.webp"
    secondary_name = f"{post.user.username}_{index}_secondary.webp"
    if not os.path.exists(primary_name):
        print(f"Downloading primary image for post of {post.user.username}")
        fp = open(f"{post.user.username}_{index}_primary.webp", "wb")
        resp = requests.get(post.primary_image.url)
        fp.write(resp.content)
    if not os.path.exists(secondary_name):
        print(f"Downloading secondary image for post of {post.user.username}")
        fp = open(f"{post.user.username}_{index}_secondary.webp", "wb")
        resp = requests.get(post.secondary_image.url)
        fp.write(resp.content)
    os.chdir("..")
    
