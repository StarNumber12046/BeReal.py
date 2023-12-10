class Person():
    def __init__(self, raw):
        self.id = raw["id"]
        self.username = raw["username"]
        
        profile_pic_obj = raw.get("profile_picture", None)
        if profile_pic_obj is not  None:
            self.profile_picture = profile_pic_obj.get("url", None)

class Me(Person):
    def __init__(self, raw):
        super().__init__(raw)
        self.phone_number = raw["phoneNumber"]
        self.name = raw["fullname"]
        self.birth_date = raw["birthdate"]
        