#!/usr/bin/env python3.6

from user import User
from credentials import Credentials


def create_user_account(user_name,pass_word):
    new_user = User(user_name,pass_word)
    return new_user

def save_user_account(user):
    user.save_user()

def check_existing_user(character):
    return User.user_exists(character)

def create_credentials(view_password,account,login_name,pass_word)
    new_credential = Credential(view_password,account,login_name,pass_word)
    return new_credential

def save_credentials(credential):
    credential.save_credential()
    
def del_credential(credential):
    credential.del_credential()

def check_existing_credentials(account):
    return Credential.credential_exist(account)

def find_credential(account):
    return Credential.find_by_account(account)

def display_credentials():
    return Credential.display_credentials()

def main():
    print("Hello! Welcome to the Password Locker. What is your name?")
    your_name = input()
    print("\n")
    print(f"Hello {your_name}!! What would you like to do?")
# while True:
    print("\nUse these short codes below:")
    print("-" * 30)
    print("\n ca - create an account, cc - create credentials, gp - generate password, cp - create own password, dc - display credentials, rc - delete credentials, ex - exit password locker")






if __name__ == '__main__':
    main()
