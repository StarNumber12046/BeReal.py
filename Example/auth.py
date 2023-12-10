import BeReal
import json

phonenumber = input("Enter your phone number: ")

client = BeReal.BeReal(phonenumber)
client.send_code()
otp = input("You should have received an authentication code. Please check your phone and enter it below.")
client.verify_code(otp)

client.initialize_client()

f = open("creds.json", "w")
f.write(json.dumps(client.save_session()))
f.close()

me = client.me()

print("Username: %s" % me.username)
