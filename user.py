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

    @classmethod
    def find_by_username(cls,name):
        for user in cls.user_list:
            if user.username == name:
                return True

        return False
class Credentials:

    credentials_list = []
    def __init__(self,view_passward,account,login,passward):
        self.view_passward = view_passward
        self.account = account
        self.login = login
        self.passward = passward



    def save_credential(self):
        Credentials.credentials_list.append(self)

    def del_credential(self):
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list
        
    @classmethod
    def find_by_account(cls,account):
        for creden in cls.credentials_list:
            if creden.account == account:
                return creden
        return False

    @classmethod
    def credentials_exist(cls,view_passward):
        for creden in cls.credentials_list:
            if creden.view_passward == view_passward:
                return True
        return False


        


