import requests
import random
from . import auth, profile, feed
import json


class BeReal():
    def __init__(self, phone_number:str, id_token:str=None, refresh_token:str=None):
        
        self.phone_number = phone_number
        self.device_id = ''.join([random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for _ in range(16)])
        self.base_urls = {"auth": ""}
        self.otp_session = None
        self.id_token = id_token
        self.refresh_token = refresh_token
        
        self.name = None
    
    def send_code(self):
        session = auth.request_code(self.phone_number, self.device_id, self.base_urls["auth"])
        self.otp_session = session["sessionInfo"]
        return self.otp_session
        
    def verify_code(self, code:str):
        res = auth.verify_code(self.otp_session, code)
        self.id_token = res["idToken"]
        self.refresh_token = res["refreshToken"]
        return 
    
    def initialize_client(self):
        codes = auth.get_code(self.refresh_token)
        self.id_token = codes["access_token"]
        self.refresh_token = codes["refresh_token"]
        return codes
    
    def save_session(self):
        return {"id_token": self.id_token, "refresh_token": self.refresh_token}
    
    def resume_session(self, session:str|dict):
        if isinstance(session, str):
            session = json.loads(session)
        self.id_token = session["id_token"]
        self.refresh_token = session["refresh_token"]
        
    def refresh_session(self):
        tokens = auth.refresh_session(self.refresh_token)
        self.id_token, self.refresh_token = tokens
        return tokens
    
    def me(self):
        me = profile.get_profile(self.id_token)
        return me
    
    def get_feed(self):
        my_feed = feed.get_feed(self.id_token)
        return my_feed