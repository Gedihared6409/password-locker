class User:


    user_list = []

    def __init__(self,username,passward):
        self.username = username
        self.passward = passward

    def save_user(self):
        User.user_list.append(self)
