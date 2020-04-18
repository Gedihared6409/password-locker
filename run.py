#!/usr/bin/env python3.6

from user import user
from credentials import credentials


def create_user_account(user_name,pass_word):
    new_user = user(user_name,pass_word)
    return new_user
    