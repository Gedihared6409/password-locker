#!/usr/bin/env python3.6

from user import user
from credentials import credentials


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


