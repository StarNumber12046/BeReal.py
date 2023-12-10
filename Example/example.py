import BeReal
import json

client = BeReal.BeReal("")

f = open("creds.json", "r")
client.resume_session(json.loads(f.read()))
f.close()

me = client.me()

print("Username: %s" % me.username)

for friend in me.friends:
    print("Friend: %s" % friend.username)

feed = client.get_feed()
for post in feed.friends_posts:
    print(f"Post by {post.user.username}")
    for p in post.posts:
        print("Primary image:",p.primary_image.url)
        print("Secondary image:",p.secondary_image.url)
    print("-----------------")