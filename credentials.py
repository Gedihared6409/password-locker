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
                return True
        return False



