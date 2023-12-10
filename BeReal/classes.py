from datetime import datetime
from enum import Enum

def convert_bereal_date(date):
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')

class Person():
    def __init__(self, raw):
        self.id = raw["id"]
        self.username = raw["username"]
        
        profile_pic_obj = raw.get("profile_picture", None)
        if profile_pic_obj is not  None:
            self.profile_picture = profile_pic_obj.get("url", None)

class Me(Person):
    def __init__(self, raw, friends_raw):
        super().__init__(raw)
        self.phone_number = raw["phoneNumber"]
        self.name = raw["fullname"]
        self.birth_date = raw["birthdate"]
        self.bio = raw["biography"]
        self.created_at = convert_bereal_date(raw["createdAt"])
        self.streak = int(raw["streakLength"])
        self.friends = []
        for friend in friends_raw:
            self.friends.append(Person(friend))
        
class Image():
    def __init__(self, raw) -> None:
        self.url = raw["url"]
        self.width = raw["width"]
        self.height = raw["height"]

class Post():
    def __init__(self, raw):
        self.id = raw["id"]
        self.primary_image = Image(raw["primary"])
        self.secondary_image = Image(raw["secondary"])
        self.retake_counter = raw["retakeCounter"]
        self.late_seconds = raw["lateInSeconds"]
        self.is_late = raw["isLate"]
        self.is_main = raw["isMain"]
        self.taken_at = convert_bereal_date(raw["takenAt"])
  
  
    
class Moment():
    def __init__(self, raw):
        self.id = raw["id"]
        self.region = raw["region"]

class Feed():
    def __init__(self, raw):
        self.friends_posts = [FriendPost(post) for post in raw["friendsPosts"]]

class FriendPost():
    def __init__(self,raw:dict):
        self.posts = [Post(post) for post in raw["posts"]]
        self.moment = Moment(raw["moment"])
        self.region = raw["region"]
        self.moment_id = raw["momentId"]
        self.user = Person(raw["user"])
    