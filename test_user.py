import unittest
from user import User

class Testuser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("ali","aligedi")


    def tes_init(sef):


        self.assertEqual(self.new_user.username,"ali")
        self.assertEqual(self.new_user.passward,"aligedi")

    def test_save_user(self):



        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    


if __name__ == '__main__':
    unittest.main()