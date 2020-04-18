import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):


    def setUp(self):
        self.new_credentials = Credentials("aligedi","instagram","ali","aligedi")

    def tearDown(self):
        Credentials.credentials_list = []


    def test_init(self):


        self.assertEqual(self.new_credentials.view_passward,"aligedi")
        self.assertEqual(self.new_credentials.account,"instagram")
        self.assertEqual(self.new_credentials.login,"ali")
        self.assertEqual(self.new_credentials.passward,"aligedi")



if __name__ == '__main__':
    unittest.main()
