import BeReal
import json

f = open("creds.json", "r")
client = BeReal.BeReal("")
client.resume_session(json.loads(f.read()))
f.close()

client.refresh_session()

me = client.me()

print(f"Refreshed token for {me.username}")

f = open("creds.json", "w")
f.write(json.dumps(client.save_session()))
f.close()
