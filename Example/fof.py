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

fof = client.get_fof()
for post in fof.posts:
    print(f"Post by {post.user.username} - ID: {post.user.id}")
    print("Mutual friends:")
    for mutual in post.user.mutuals:
        print("- %s" % mutual.username)

    print("Post id:",post.id)
    print("Primary image:",post.primary_image.url)
    print("Secondary image:",post.secondary_image.url)
    print("REAL MOJIS")
    for moji in post.real_mojis:
        print(f"{moji.user.username}")

    print("-----------------")
