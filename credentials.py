class Credentials:

    credentials_list = []
    def __init__(self,view_passward,account,login,passward):
        self.view_passward = view_passward
        self.account = account
        self.login = login
        self.passward = passward



    def save_credential(self):
        Credentials.credentials_list.append(self)




