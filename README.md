<h1 align="center">BeReal.py</h1>
<p align="center">A Python API wrapper for BeReal</p>

> [!CAUTION]
> This uses only reverse-engineered code. I am not to be held responsible for any consequences of the use of this library. Your account may be banned, you might get ratelimited, use this with caution.

## Installation
> [!WARNING]
> For now the project is NOT on pypi.

``` sh
# Windows:
pip install git+https://gitub.com/StarNumber12046/BeReal.py

# Macos/Linux:
pip3 install git+https://gitub.com/StarNumber12046/BeReal.py
```

## Special thanks
Special thanks to macedonga with [beunblurred](https://github.com/macedonga/beunblurred) for having already done part of the reverse engineering

## Quick example
```py
import BeReal, json

client = BeReal.client("+12345678901")
# Send and verify OTP
client.send_code()
otp = input("You should have received an authentication code. Please check your phone and enter it below.")

# Initialize the client with BeReal-provided tokens
client.initialize_client()

# Save credentials
f = open("creds.json", "w")
f.write(json.dumps(client.save_session()))
f.close()

# Get logged in user
me = client.me()
print(f"Username: {me.username}")
for friend in me.friends:
    print(f"Friend: {friend.username}")
```
