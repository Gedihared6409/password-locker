import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):


    def setUp(self):
        self.new_credentials = Credentials("aligedi","instagram","ali","aligedi")