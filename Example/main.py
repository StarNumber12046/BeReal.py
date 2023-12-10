import BeReal
import json

phonenumber = input("Enter your phone number: ")

client = BeReal.BeReal(phonenumber)
# client.send_code()
# otp = input("You should have received an authentication code. Please check your phone and enter it below.")
# client.verify_code(otp)

# f = open("creds.json", "w")
# f.write(json.dumps(client.save_session()))
# f.close()

# client.initialize_client()

# client.refresh_session()


f = open("creds.json", "r")
client.resume_session(f.read())
f.close()

me = client.me()

print("Username: %s" % me.username)

for friend in me.friends:
    print("Friend: %s" % friend.username)
