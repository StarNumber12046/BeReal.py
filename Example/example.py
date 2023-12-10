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
for post in feed.friends_posts + feed.user_posts:
    print(f"Post by {post.user.username}")
    print("Mutual friends:")
    for mutual in post.user.mutuals:
        print("- %s" % mutual.username)
    for p in post.posts:
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
    print("-----------------")

fof = client.get_fof()
for post in fof.posts:
    print(f"Post by {post.user.username}")
    print("Mutual friends:")
    for mutual in post.user.mutuals:
        print("- %s" % mutual.username)

    print("Post id:",p.id)
    print("Primary image:",p.primary_image.url)
    print("Secondary image:",p.secondary_image.url)
    print("REAL MOJIS")
    for moji in p.real_mojis:
        print(f"{moji.user.username} : {moji.emoji}")

    print("-----------------")
