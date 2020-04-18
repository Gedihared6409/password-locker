class User:


    user_list = []

    def __init__(self,username,passward):
        self.username = username
        self.passward = passward

    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def user_exists(cls,character):
        for user in cls.user_list:
            if user.passward == character:
                return True

        return False


        


