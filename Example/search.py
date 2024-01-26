import BeReal
import json
import sys

client = BeReal.BeReal("")

f = open("creds.json", "r")
client.resume_session(json.loads(f.read()))
f.close()

me = client.me()
client.search("starnumber")