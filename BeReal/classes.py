from datetime import datetime

def convert_bereal_date(date):
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')

class Person():
    def __init__(self, raw):
        self.id:str = raw["id"]
        self.username:str = raw["username"]
        # Add a Person as relationship->commonFriends[]
        self.mutuals:list[Person] = [Person(friend) for friend in raw["relationship"]["commonFriends"]] if "relationship" in raw else []
        profile_pic_obj = raw.get("profile_picture", None)
        if profile_pic_obj is not None:
            self.profile_picture:str = profile_pic_obj.get("url", None)

class Me(Person):
    def __init__(self, raw, friends_raw):
        super().__init__(raw)
        self.phone_number:str = raw["phoneNumber"]
        self.name:str = raw["fullname"]
        self.birth_date:str = convert_bereal_date(raw["birthdate"])
        self.bio:str = raw["biography"]
        self.created_at = convert_bereal_date(raw["createdAt"])
        self.streak:int = raw["streakLength"]
        self.friends:list[Person] = []
        for friend in friends_raw:
            self.friends.append(Person(friend))
        
class Image():
    def __init__(self, raw) -> None:
        self.url:str = raw["url"]
        self.width:int = raw["width"]
        self.height:int = raw["height"]

class Post():
    def __init__(self, raw):
        self.id = raw["id"]
        self.primary_image = Image(raw["primary"])
        self.secondary_image = Image(raw["secondary"])
        self.retake_counter:int = raw["retakeCounter"]
        self.late_seconds:int = raw["lateInSeconds"]
        self.is_late:bool = raw["isLate"]
        self.is_main:bool = raw["isMain"]
        self.taken_at = convert_bereal_date(raw["takenAt"])
        self.real_mojis = [RealMoji(moji) for moji in raw["realMojis"]] if "realMojis" in raw else []
        self.comments = [Comment(comment) for comment in raw["comments"]] if "comments" in raw else []
  
  
    
class Moment():
    def __init__(self, raw):
        self.id:str = raw["id"]
        self.region:str = raw["region"]

class Feed():
    def __init__(self, raw,):
        self.friends_posts = [FriendPost(post) for post in raw["friendsPosts"]]
        self.user_posts = [FriendPost(raw['userPosts'])]

class Comment():
    def __init__(self, raw):
        self.id:str = raw["id"]
        self.content:str = raw['content']
        self.posted_at = convert_bereal_date(raw["postedAt"])
        self.author = Person(raw["user"])

class RealMoji():
    def __init__(self, raw):
        self.emoji:str = raw["emoji"]
        self.is_instant:bool = raw["isInstant"]
        self.posted_at = convert_bereal_date(raw["postedAt"])
        self.user = Person(raw["user"])
        self.media = Image(raw["media"])
        self.type  = raw["type"]

class FriendPost():
    def __init__(self,raw:dict):
        self.posts = [Post(post) for post in raw["posts"]]
        self.moment = Moment(raw["moment"]) if "moment" in raw.keys() else Moment({"id": raw['momentId'], "region": ""})
        self.region:str = raw["region"]
        self.moment_id:str = raw["momentId"]
        self.caption = raw["caption"] if "caption" in raw.keys() else ""
        self.user = Person(raw["user"])

class FOFRealMoji():
    def __init__(self, raw):
        self.id:str = raw["id"]
        self.emoji:str = raw["emoji"]
        self.media = Image(raw["media"])
        self.user = Person(raw["user"])
        self.is_instant:bool = raw["isInstant"]
        self.posted_at = convert_bereal_date(raw["postedAt"])

class FOFPost():
    def __init__(self, raw):
        self.taken_at = convert_bereal_date(raw["postedAt"])
        self.id:str = raw["id"]
        self.user = Person(raw["user"])
        self.moment = Moment(raw["moment"])
        self.primary_image = Image(raw["primary"])
        self.secondary_image = Image(raw["secondary"])
        self.real_mojis = [FOFRealMoji(moji) for moji in raw["realmojis"]["sample"]]
        
        

class FOFFeed():
    def __init__(self, raw) -> None:
        self.posts = [FOFPost(post) for post in raw["data"]]