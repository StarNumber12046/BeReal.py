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

today = datetime.now()

datestring = today.strftime("%Y%m%d%H")  # Date to the desired string format
Path(datestring).mkdir(parents=True, exist_ok=True)   # Create folder
os.chdir(datestring)


for friend in me.friends:
    print("Friend: %s" % friend.username)

feed = client.get_feed()
for post in feed.friends_posts + feed.user_posts:
    print(f"Post by {post.user.username}")
    print("Mutual friends:")
    for mutual in post.user.mutuals:
        print("- %s" % mutual.username)
    for index, p in enumerate(post.posts):
        print("Post id:",p.id)
        print("Primary image:",p.primary_image.url)
        print("Secondary image:",p.secondary_image.url)
        print("Retake counter:",p.retake_counter)
        print("REAL MOJIS")
        for moji in p.real_mojis:
            print(f"{moji.user.username} : {moji.emoji}")
        print("COMMENTS")
        for commment in p.comments:
            print(f"{commment.author.username} : {commment.content}")
        print("-----     -----     -----")
        fp = open(f"{post.user.username}_{index}_primary.webp", "wb")
        resp = requests.get(p.primary_image.url)
        fp.write(resp.content)
        fp = open(f"{post.user.username}_{index}_secondary.webp", "wb")
        resp = requests.get(p.secondary_image.url)
        fp.write(resp.content)
    print("-----------------")

fof = client.get_fof()
for post in fof.posts:
    print(f"Post by {post.user.username}")
    print("Mutual friends:")
    fp = open(f"{post.user.username}_0_primary.webp", "wb")
    resp = requests.get(post.primary_image.url)
    fp.write(resp.content)
    fp = open(f"{post.user.username}_0_secondary.webp", "wb")
    resp = requests.get(post.secondary_image.url)
    fp.write(resp.content)
    
    for mutual in post.user.mutuals:
        print("- %s" % mutual.username)

    print("Post id:",post.id)
    print("Primary image:",post.primary_image.url)
    print("Secondary image:",post.secondary_image.url)
    print("REAL MOJIS")
    for moji in post.real_mojis:
        print(f"{moji.user.username} : {moji.emoji}")

    print("-----------------")
